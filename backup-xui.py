import subprocess
def backup():
    subprocess.run(['sudo', "apt", "-y","update"])
