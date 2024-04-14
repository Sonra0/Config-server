import subprocess
import sys
from ufwset import ufwrun
from ssl import takessl
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
        print("7. change ssh port")
        print("8. take ssl")
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
            ufwrun()
        if num == 7 :
            chmod_process = subprocess.run(["chmod", '+x', 'change-ssh-port.sh'], capture_output=True, text=True)
            if chmod_process.returncode == 0:
                print("\nchmod successful.\n")
            else:
                print("\nchmod failed\n")
            run_process = subprocess.run(['bash', "change-ssh-port.sh"])
        if num == 8 :
            takessl()
        if num == 0:
            break
