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
        print("0. exit")
        print("\nenter your number:",end=" ")
        num = int(input())
        if num == 1:
            subprocess.run(["chmod", '+x', '/Linux-Optimizer/linux-optimizer.sh'])
            subprocess.run(['bash',"./Linux-Optimizer/linux-optimizer.sh"])
        if num == 2:
            subprocess.run(["chmod", '+x', '/VPS-Optimizer/optimizer.sh'])
            subprocess.run(['bash', "./VPS-Optimizer/optimizer.sh"])
        if num == 3:
            chisel()
        if num ==4 :
            print("\n1. compile rathole")
            print("2. setup rathole")
            print("0. exit")
            print("\nenter your number:",end=" ")
            num2=int(input())
            if num2 == 1 :
                subprocess.run(["chmod", '+x', '/Rathole_reverseTunnel/install.sh'])
                subprocess.run(['bash', "./Rathole_reverseTunnel/install.sh"])
            if num2 == 2 :
                subprocess.run(["chmod", '+x', '/Rathole_reverseTunnel/go.sh'])
                subprocess.run(['bash', "./Rathole_reverseTunnel/go.sh"])
            if num2 == 0 :
                continue
        if num == 0:
            break