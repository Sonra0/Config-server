import subprocess
def ufwrun():
    install_process = subprocess.run(['apt-get', "-y", "install",'ufw'])
    if install_process.returncode == 0:
        print("\nufw installed successful\n")
    else:
        print("\nunable to install ufw\n")
    reset_process = subprocess.run(["echo","y","|","sudo",'ufw', "reset"])
    if reset_process.returncode == 0 :
        print("\nufw reset successful\n")
    else:
        print("\nunable to reset ufw\n")
    open_process_443 = subprocess.run(["sudo","ufw","allow","443"])
    open_process_8080 = subprocess.run(["sudo","ufw","allow","8080"])
    open_process_2096 = subprocess.run(["sudo","ufw","allow","2096"])
    open_process_32324 = subprocess.run(["sudo","ufw","allow","32324"])
    open_process_22 = subprocess.run(["sudo","ufw","allow","22"])
    if open_process_443.returncode == 0 :
        print("\nport 443 opened successful\n")
    else :
        print("\nunable to open port 443\n")
    if open_process_8080.returncode == 0 :
        print("\nport 8080 opened successful\n")
    else :
        print("\nunable to open port 8080\n")
    if open_process_2096.returncode == 0 :
        print("\nport 2096 opened successful\n")
    else :
        print("\nunable to open port 2096\n")
    if open_process_32324.returncode == 0 :
        print("\nport 32324 opened successful\n")
    else :
        print("\nunable to open port 32324\n")
    if open_process_22.returncode == 0 :
        print("\nport 22 opened successful\n")
    else :
        print("\nunable to open port 22\n")
    enable_process = subprocess.run(["sudo", "ufw", "enable"])
    if enable_process.returncode == 0 :
       print("\nufw enabled successful\n")
    else :
        print("\nunable to start ufw\n")
    autostart_process = subprocess.run(["sudo", "systemctl", "enable",'ufw'])
    if autostart_process.returncode == 0 :
        print("\nauto start enabled\n")
    else :
        print("\nunable to auto start!\n")
