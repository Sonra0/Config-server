import subprocess
import os
import shutil
def backup():
    os.chdir('/root/')
    try :
        shutil.rmtree('/root/backup-xui/', ignore_errors=True)
    finally:
        os.mkdir("/root/backup-xui/")
        shutil.copyfile("/root/Config-server/backup.py", "/root/backup-xui/backup.py")
        subprocess.run(["apt", '-y', 'update'])
        subprocess.run(["apt", 'install', 'python3'])
        subprocess.run(["apt", 'install', 'cron'])
        subprocess.run(["apt", 'install', 'python3-pip'])
        subprocess.run(["apt", 'install', 'pyTelegramBotAPI'])
        print("\nEnter your telegram bot token :",end="")
        token = input()
        print("\nEnter your telegram account chat id :", end="")
        chat_id = input()
        script_path = '/root/backup-xui/backup.py'
        cron_job = f'\n0 * * * * /usr/bin/python3 {script_path}\n'
        try :
            with open('/etc/cron.d/mycron', 'w') as file:
                file.write(cron_job)
        except :
            print ("cronjob failed")
        subprocess.run(["python3", "backup.py"])
