import subprocess
import os
import shutil
def backup_do():
    os.chdir('/root/')
    try :
        shutil.rmtree('/root/backup-xui/', ignore_errors=True)
    finally:
        return_code = os.mkdir("/root/backup-xui/")
        if return_code == 0 :
            print("\n/root/backup-xui/ file created !")
        else :
            print("\nunable to create /root/backup-xui/")
        return_code = shutil.copyfile("/root/Config-server/backup.py", "/root/backup-xui/backup.py")
        if return_code == 0 :
            print("\n/root/Config-server/backup.py copied !")
        else :
            print("\nunable to copy /root/Config-server/backup.py")
        return_code = shutil.copyfile("/root/Config-server/data.py", "/root/backup-xui/data.py")
        if return_code == 0 :
            print("\n/root/Config-server/data.py copied !")
        else :
            print("\nunable to copy /root/Config-server/data.py")
        p1 = subprocess.run(["apt", '-y', 'update'])
        if p1.returncode = 0 :
            print("\napt update done")
        else :
            print("\nunable to do update")
        p1 = subprocess.run(["apt", 'install', 'python3'])
        if p1.returncode = 0 :
            print("\npython3 installed")
        else :
            print("\nunable to install python3")
        p1 = subprocess.run(["apt", 'install', 'cron'])
        if p1.returncode = 0 :
            print("\ncron installed")
        else :
            print("\nunable to install cron")
        p1 = subprocess.run(["apt", 'install', 'python3-pip'])
        if p1.returncode = 0 :
            print("\npython3-pip installed")
        else :
            print("\nunable to install python3-pip")
        p1 = subprocess.run(["pip", 'install', 'pyTelegramBotAPI'])
        if p1.returncode = 0 :
            print("download pyTelegramBotAPI done")
        else :
            print("unable to download pyTelegramBotAPI")
        script_path = '/root/backup-xui/backup.py'
        cron_job = f'\n0 * * * * /usr/bin/python3 {script_path}\n'
        try :
            with open('/etc/cron.d/mycron', 'w') as file:
                file.write(cron_job)
            print("\nCronjob created")
        except :
            print ("\ncronjob failed")
        subprocess.run(["python3", "/root/backup-xui/backup.py"])
