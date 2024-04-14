import subprocess
def takessl():
    disable_process = subprocess.run(['sudo', "ufw", 'disable'])
    if disable_process.returncode == 0 :
        print("\nufw disabled successful\n")
    else:
        print("\nunable to disable ufw\n")
    curl_process = subprocess.run(['sudo', "apt-get", '-y', 'install', 'curl'])
    if curl_process.returncode == 0 :
        print("\ncurl installed successful\n")
    else:
        print("\nunable to install curl !\n")
    command1_process = subprocess.run(['sudo', "curl", 'https://get.acme.sh','|','sh'])
    if command1_process.returncode == 0 :
        print("\ncommand1 was successful\n")
    else:
        print("\nunable to do command1\n")
    command2_process = subprocess.run(['sudo', "~/.acme.sh/acme.sh", '--set-default-ca','--server','letsencrypt'])
    if command2_process.returncode == 0 :
        print("\ncommand2 was successful\n")
    else:
        print("\nunable to do command2\n")
    command3_process = subprocess.run(['sudo', "~/.acme.sh/acme.sh", '--register-account', '-m', 'mannemikhambasham@gmail.com'])
    if command3_process.returncode == 0 :
        print("\ncommand3 was successful\n")
    else:
        print("\nunable to do command3\n")
    print("enter your sub-domain :",end="")
    domain=input()
    command4_process = subprocess.run(['sudo', "~/.acme.sh/acme.sh", '--issue', '-d', domain , "--standalone"])
    if command4_process.returncode == 0 :
        print("\ncommand4 was successful\n")
    else:
        print("\nunable to do command4\n")
    command5_process = subprocess.run(['sudo', "~/.acme.sh/acme.sh", '--installcert', '-d', domain, "--key-file","/root/private.key","--fullchain-file","/root/cert.crt"])
    if command5_process.returncode == 0 :
        print("\ncommand5 was successful\n")
    else:
        print("\nunable to do command5\n")
    enable_process = subprocess.run(['sudo', "ufw", 'enable'])
    if enable_process.returncode == 0:
        print("\nufw enabled successful\n")
    else:
        print("\nunable to enable ufw\n")