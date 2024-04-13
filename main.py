import subprocess
import sys
def chisel():
    from Chisel_multipleServers import chisel
if __name__ == '__main__':
    while True :
        print("\n1. Linux Hawshemi optimizer ")
        print("2. Linux OPIRAN optimizer ")
        print("3. chisel tunnel ")
        print("4. rathole tunnel ")
        print("5. install mhsanaei")
        print("6. config ufw")
        print("0. exit")
        print("\nenter your number:",end=" ")
        num = int(input())
        if num == 1:
            chmod_process = subprocess.run(["chmod", '+x', '/Linux-Optimizer/linux-optimizer.sh',],capture_output=True, text=True)
            if chmod_process.returncode == 0:
                print("\nchmod successful.\n")
            else:
                print("\nchmod failed\n")
            run_process = subprocess.run(['bash',"./Linux-Optimizer/linux-optimizer.sh"])
        if num == 2:
            chmod_process = subprocess.run(["chmod", '+x', '/VPS-Optimizer/optimizer.sh'],capture_output=True, text=True)
            if chmod_process.returncode == 0:
                print("\nchmod successful.\n")
            else:
                print("\nchmod failed\n")
            run_process = subprocess.run(['bash', "./VPS-Optimizer/optimizer.sh"])
        if num == 3:
            chisel()
        if num ==4 :
            print("\n1. compile rathole")
            print("2. setup rathole")
            print("0. exit")
            print("\nenter your number:",end=" ")
            num2=int(input())
            if num2 == 1 :
                chmod_process = subprocess.run(["chmod", '+x', '/Rathole_reverseTunnel/install.sh'],capture_output=True, text=True)
                if chmod_process.returncode == 0:
                    print("\nchmod successful.\n")
                else:
                    print("\nchmod failed\n")
                run_process = subprocess.run(['bash', "./Rathole_reverseTunnel/install.sh"])
            if num2 == 2 :
                chmod_process = subprocess.run(["chmod", '+x', '/Rathole_reverseTunnel/go.sh'],capture_output=True, text=True)
                if chmod_process.returncode == 0:
                    print("\nchmod successful.\n")
                else:
                    print("\nchmod failed\n")
                run_process = subprocess.run(['bash', "./Rathole_reverseTunnel/go.sh"])
            if num2 == 0 :
                continue
        if num == 5 :
            print("enter your version:( example: 2.2.1 ):",end=' ')
            version = 'v'+input()
            chmod_process = subprocess.run(["chmod", '+x', './3x-ui/install.sh'], capture_output=True,text=True)
            if chmod_process.returncode == 0:
                print("\nchmod successful.\n")
            else:
                print("\nchmod failed\n")
            run_process = subprocess.run(['bash', "./3x-ui/install.sh",version ])
        if num == 6 :
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
        if num == 0:
            break