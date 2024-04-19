import subprocess
def socat_run():
    print("run this script in server iran\nenter any key to continue",end='')
    a = input()
    subprocess.run(["apt", 'update','-y'])
    c1 = subprocess.run(["apt", 'install', 'socat', '-y'])
    if c1.returncode == 0 :
        print("socat installed")
    else:
        print("unable to install socat")
    print("\nEnter your port:",end="")
    port = input()
    print("\nEnter your des ip :", end="")
    ip = input()
    f = open("/usr/lib/systemd/system/socat.service",'w')
    f.write("####\n[Unit]\nDescription=Socat tunnel for network daemons\nAfter=network.target\nAfter=syslog.target\n\n[Install]\nWantedBy=multi-user.target\nAlias=socat.target\n\n[Service]\nType=forking\nExecStart=/usr/bin/socat TCP4-LISTEN:"+port+" TCP4:"+ip+":"+port+"\nExecStop=/usr/bin/pkill socat\n\nTimeoutSec=600\nRestart=always\nPrivateTmp=false\n#####")
    f.close()
    restart = subprocess.run(["systemctl", 'restart', 'socat.service'])
    if restart.returncode == 0 :
        print("socat restarted")
    else:
        print("unable to restart socat")
    enable = subprocess.run(["systemctl", 'enable', 'socat.service'])
    if enable.returncode == 0 :
        print("socat enabled")
    else:
        print("unable to start socat")
socat_run()
