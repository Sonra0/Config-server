import subprocess
import sys
from ufwset import ufwrun
from ssl import takessl
def chisel():
    from Chisel_multipleServers import chisel
if __name__ == '__main__':
    while True :
        subprocess.run(['curl', "-s","https://raw.githubusercontent.com/shinya/pokemon-terminal-art/main/256color/silver/001.txt"])
        print("\n1. Linux optimizer ")
        print("2. Tunnel server ")
        print("3. Install X-ui panel")
        print("4. Config ufw")
        print("5. Change ssh port")
        print("6. SSL certificate")
        print("0. Exit")
        print("\nEnter your number:",end=" ")
        num = int(input())
        if num == 1:
            print("\n1. Hawshemi optimizer")
            print("2. OPIRAN optimizer")
            print("0. Exit")
            print("\nEnter your number:",end=" ")
            num2 = int(input())
            if num2 == 1 :
                chmod_process = subprocess.run(["chmod", '+x', '/Linux-Optimizer/linux-optimizer.sh',],capture_output=True, text=True)
                if chmod_process.returncode == 0:
                    print("\nChmod successful.\n")
                else:
                    print("\nChmod failed\n")
                run_process = subprocess.run(['bash',"./Linux-Optimizer/linux-optimizer.sh"])
            if num2 == 2:
                chmod_process = subprocess.run(["chmod", '+x', '/VPS-Optimizer/optimizer.sh'],capture_output=True, text=True)
                if chmod_process.returncode == 0:
                    print("\nChmod successful.\n")
                else:
                    print("\nChmod failed\n")
                run_process = subprocess.run(['bash', "./VPS-Optimizer/optimizer.sh"])
            if num2 == 0:
                continue
        if num == 2 :
            print("\n1. Rathole")
            print("2. Chisel")
            print("0. Exit")
            print("\nEnter your number:", end=" ")
            num2 = int(input())
            if num2 == 1 :
                print("\n1. Compile Rathole")
                print("2. Setup Rathole")
                print("0. Exit")
                print("\nEnter your number:",end=" ")
                num3=int(input())
                if num3 == 1 :
                    chmod_process = subprocess.run(["chmod", '+x', '/Rathole_reverseTunnel/install.sh'],capture_output=True, text=True)
                    if chmod_process.returncode == 0:
                        print("\nchmod successful.\n")
                    else:
                        print("\nchmod failed\n")
                    run_process = subprocess.run(['bash', "./Rathole_reverseTunnel/install.sh"])
                if num3 == 2 :
                    chmod_process = subprocess.run(["chmod", '+x', '/Rathole_reverseTunnel/go.sh'],capture_output=True, text=True)
                    if chmod_process.returncode == 0:
                        print("\nchmod successful.\n")
                    else:
                        print("\nchmod failed\n")
                    run_process = subprocess.run(['bash', "./Rathole_reverseTunnel/go.sh"])
                if num3 == 0 :
                    continue
            if num2 == 2 :
                chisel()
            if num2 == 0 :
                continue
        if num == 3 :
            print("\n1. Mhsanaei")
            print("0. Exit")
            print("\nEnter your number:",end=" ")
            num2 = int(input())
            if num2 == 1 :
                print("enter your version:( example: 2.2.1 ):",end=' ')
                version = 'v'+input()
                chmod_process = subprocess.run(["chmod", '+x', './3x-ui/install.sh'], capture_output=True,text=True)
                if chmod_process.returncode == 0:
                    print("\nchmod successful.\n")
                else:
                    print("\nchmod failed\n")
                run_process = subprocess.run(['bash', "./3x-ui/install.sh",version ])
            if num2 == 0 :
                continue
        if num == 4 :
            ufwrun()
        if num == 5 :
            chmod_process = subprocess.run(["chmod", '+x', 'change-ssh-port.sh'], capture_output=True, text=True)
            if chmod_process.returncode == 0:
                print("\nchmod successful.\n")
            else:
                print("\nchmod failed\n")
            run_process = subprocess.run(['bash', "change-ssh-port.sh"])
        if num == 6 :
            takessl()
        if num == 0:
            break
