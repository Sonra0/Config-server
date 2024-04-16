def firewall():
    root = subprocess.run(['cd'])
    mk = subprocess.run(['mkdir',"iptables_rules"])
    if mk.returncode == 0:
        print("\nmkdir done .\n")
    else:
        print("\nmkdir failed\n")
    cd = subprocess.run(['cd', "iptables_rules"])
    if cd.returncode == 0:
        print("\ncd done .\n")
    else:
        print("\ncd failed\n")
    save = subprocess.run(["sudo","iptables-save",'>','iptables-backup.txt'])
    if save.returncode == 0:
        print("\nsave done .\n")
    else:
        print("\nsave failed\n")
    mv = subprocess.run(['mv', "/root/Config-server/firewall.txt",'/root/iptables_rules/'])
    if mv.returncode == 0:
        print("\nmove done .\n")
    else:
        print("\nmove failed\n")
