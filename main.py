import subprocess
while True :
    print("1. Linux Hawshemi optimizer ")
    print("2. Linux OPIRAN optimizer ")
    print("3. chisel tunnel ")
    print("4. rathole compile ")
    print("5. rathole install ")
    print("0. exit")
    print("\n enter your number :",end="")
    num = int(input())
    if num == 1:
        subprocess.run(["chmod",'+x','main.py'])
        subprocess.run(["chmod", '+x', '/Linux-Optimizer/linux-optimizer.sh'])
        subprocess.run(['bash',"./Linux-Optimizer/linux-optimizer.sh"])
    if num == 0:
        break