import subprocess
import os
import shutil
def firewall():
    os.chdir('/root/')
    try :
        shutil.rmtree('/root/iptables_rules/ > /dev/null')
    finally:
        os.mkdir("iptables_rules")
        os.chdir('/root/iptables_rules')
        shutil.copyfile("/root/Config-server/firewall.txt" , "/root/iptables_rules/firewall.txt")
        print("how many white ip do you have ? ",end="")
        a = int(input())
        for i in range (a) :
            print("enter your ",i+1," ip :",end='')
            q = input()
            f = open("firewall.txt",'a')
            f.write("\n" + q)
            f.close()
        install = subprocess.run(["apt",'install','iptables','ipset','-y'])
        if install.returncode == 0 :
            print("\niptables installed.")
        else :
            print("\nunable to install iptables")
        install2 = subprocess.run(["apt",'install','iptables-persistent'])
        if install2.returncode == 0 :
            print("\niptables-persistent installed.")
        else :
            print("\nunable to install iptables-persistent")
        service_run = subprocess.run(["service",'iptables','start'])
        if service_run.returncode == 0 :
            print("\niptables runned.")
        else :
            print("\nunable to run iptables")
        u = open("apply.sh",'a')
        u.write("\n#!/bin/bash")
        u.write("\niptables -F")
        print("Enter your ssh port : ",end="")
        ssh = input()
        u.write("\niptables -A INPUT -p tcp --dport "+ ssh +" -j ACCEPT")
        print("How many white IP do you have ? ",end="")
        num = int(input())
        for i in range(num):
            print('Enter your', i + 1, 'IP :', end='')
            ip = input()
            u.write("\niptables -A INPUT -s " + ip + " -j ACCEPT")
            u.write("\niptables -A OUTPUT -s " + ip + " -j ACCEPT")
        u.write("\nipset create whitelist hash:net")
        u.write("\nwhile read line; do ipset add whitelist $line; done < /root/iptables_rules/firewall.txt")
        u.write("\niptables -A INPUT -m set --match-set whitelist src -j ACCEPT")
        u.write("\niptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")
        u.write("\niptables -I INPUT 1 -i lo -j ACCEPT")
        u.write("\niptables -A INPUT -j DROP")
        u.close()
        chmod = subprocess.run(["chmod", "+x", "apply.sh"])
        if chmod.returncode == 0:
            print("Chmod done")
        else:
            print("chmod failed")
        run = subprocess.run(["bash", "apply.sh"])
        if run.returncode == 0:
            print("apply runned")
        else:
            print("unable to run apply")
        tada = open("/etc/rc.local", 'a')
        tada.write("#!/bin/sh")
        tada.write("\nchmod +x /root/iptables_rules/apply.sh")
        tada.write("\nbash /root/iptables_rules/apply.sh")
        tada.close()
        chown = subprocess.run(["chown", "root", '/etc/rc.local'])
        if chown.returncode == 0:
            print("chown Done")
        else:
            print("unable to chown")
        chmod = subprocess.run(["chmod", "755", '/etc/rc.local'])
        if chmod.returncode == 0:
            print("chmod Done")
        else:
            print("unable to mod")
        start = subprocess.run(["bash", "/etc/rc.local", "start"])
        if start.returncode == 0:
            print("Started")
        else:
            print("unable to Start")