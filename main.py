import subprocess

from ufwset import ufwrun
from ssl import takessl
from backup_xui import backup_do
from firewall_iran import firewall
from nameserver import dns
from socat import socat_tunnel
def chisel():
    from Chisel_multipleServers import chisel  # noqa
def socat_run2():
    from socat_tunnel import socat_run

def hawshemi():
    chmod_process = subprocess.run(["chmod", '+x', '/Linux-Optimizer/linux-optimizer.sh', ], capture_output=True,
                                   text=True)
    if chmod_process.returncode == 0:
        print("\nChmod successful.\n")
    else:
        print("\nChmod failed\n")
    run_process = subprocess.run(['bash', "./Linux-Optimizer/linux-optimizer.sh"])


def op_iran():
    chmod_process = subprocess.run(["chmod", '+x', '/VPS-Optimizer/optimizer.sh'], capture_output=True, text=True)
    if chmod_process.returncode == 0:
        print("\nChmod successful.\n")
    else:
        print("\nChmod failed\n")
    run_process = subprocess.run(['bash', "./VPS-Optimizer/optimizer.sh"])


def rathole_compile():
    chmod_process = subprocess.run(["chmod", '+x', '/Rathole_reverseTunnel/install.sh'], capture_output=True, text=True)
    if chmod_process.returncode == 0:
        print("\nchmod successful.\n")
    else:
        print("\nchmod failed\n")
    run_process = subprocess.run(['bash', "./Rathole_reverseTunnel/install.sh"])


def rathole_install():
    chmod_process = subprocess.run(["chmod", '+x', '/Rathole_reverseTunnel/go.sh'], capture_output=True, text=True)
    if chmod_process.returncode == 0:
        print("\nchmod successful.\n")
    else:
        print("\nchmod failed\n")
    run_process = subprocess.run(['bash', "./Rathole_reverseTunnel/go.sh"])


def run_private():
    chmod_process = subprocess.run(["chmod", '+x', '/root/Config-server/PrivateIP_TCP-UDP_Tunnel/Private.sh'],
                                   capture_output=True, text=True)
    if chmod_process.returncode == 0:
        print("\nchmod successful.\n")
    else:
        print("\nchmod failed\n")
    run_process = subprocess.run(['bash', "/root/Config-server/PrivateIP_TCP-UDP_Tunnel/Private.sh"])


def run_gost():
    chmod_process = subprocess.run(["chmod", '+x', '/root/Config-server/Gost-ip6/Gost.sh'], capture_output=True,
                                   text=True)
    if chmod_process.returncode == 0:
        print("\nchmod successful.\n")
    else:
        print("\nchmod failed\n")
    run_process = subprocess.run(['bash', "/root/Config-server/Gost-ip6/Gost.sh"])


def install_mh():
    print("enter your version:( example: 2.2.1 ):", end=' ')
    version = 'v' + input()
    chmod_process = subprocess.run(["chmod", '+x', './3x-ui/install.sh'], capture_output=True, text=True)
    if chmod_process.returncode == 0:
        print("\nchmod successful.\n")
    else:
        print("\nchmod failed\n")
    run_process = subprocess.run(['bash', "./3x-ui/install.sh", version])


def install_alireza():
    print("enter your version:( example: 2.2.1 ):", end=' ')
    version = input()
    run_process = subprocess.run(['bash', "./x-ui/install.sh", version])


def change_ssh():
    chmod_process = subprocess.run(["chmod", '+x', 'change-ssh-port.sh'], capture_output=True, text=True)
    if chmod_process.returncode == 0:
        print("\nchmod successful.\n")
    else:
        print("\nchmod failed\n")
    run_process = subprocess.run(['bash', "change-ssh-port.sh"])


if __name__ == '__main__':
    while True:
        subprocess.run(['curl', "-s",
                        "https://raw.githubusercontent.com/shinya/pokemon-terminal-art/main/256color/silver/001.txt"])
        print("\n1. Linux optimizer ")
        print("2. Tunnel server ")
        print("3. Install x-ui panel")
        print("4. Config UFW")
        print("5. Change SSH port")
        print("6. SSL certificate")
        print("7. Iran firewall")
        print("8. X-UI Backup")
        print("9. Change NameServer")
        print("0. Exit")
        print("\nEnter your number:", end=" ")
        num = int(input())
        if num == 1:
            print("\n1. Hawshemi optimizer")
            print("2. OPIRAN optimizer")
            print("0. Exit")
            print("\nEnter your number:", end=" ")
            num2 = int(input())
            if num2 == 1:
                hawshemi()
            if num2 == 2:
                op_iran()
            if num2 == 0:
                continue
        if num == 2:
            print("\n1. Rathole")
            print("2. Chisel")
            print("3. Gost + PrivateIP")
            print("4. Socat")
            print("0. Exit")
            print("\nEnter your number:", end=" ")
            num2 = int(input())
            if num2 == 1:
                print("\n1. Compile Rathole")
                print("2. Setup Rathole")
                print("0. Exit")
                print("\nEnter your number:", end=" ")
                num3 = int(input())
                if num3 == 1:
                    rathole_compile()
                if num3 == 2:
                    rathole_install()
                if num3 == 0:
                    continue
            if num2 == 2:
                chisel()
            if num2 == 3:
                print("\n1. PrivateIP")
                print("2. Gost")
                print("0. Exit")
                print("\nEnter your number: ", end='')
                num3 = int(input())
                if num3 == 1:
                    run_private()
                if num3 == 2:
                    run_gost()
                if num3 == 0:
                    continue
            if num2 == 4:
                socat_run2()
            if num2 == 0:
                continue
        if num == 3:
            print("\n1. Mhsanaei")
            print("2. Alireza")
            print("0. Exit")
            print("\nEnter your number:", end=" ")
            num2 = int(input())
            if num2 == 1:
                install_mh()
            if num2 == 2:
                install_alireza()
            if num2 == 0:
                continue
        if num == 4:
            ufwrun()
        if num == 5:
            change_ssh()
        if num == 6:
            takessl()
        if num == 7:
            firewall()
        if num == 8:
            backup_do()
        if num == 9:
            dns()
        if num == 0:
            break
