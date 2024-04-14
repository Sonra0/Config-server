#!/bin/bash
# Copied from https://github.com/FreePBXHosting/freepbx-scripts/tree/master/sshport
#
# To run the script, login as root via SSH and run the following command: 
# bash <(curl -Ls https://gist.github.com/worldadventurer/842f1a10762cba0ce27dc8f99a835377/raw)
#
#############################################
# FreePBXHosting.com - @freepbxhosting      #
# VERSION 1.6       UPDATED JUN 25 2015     #
# DESC: CHANGES SSH PORT AND RESTARTS SSH   #
#############################################

# Prompt user for desired port
echo ""
echo -n "Please enter the port you would like SSH to run on > "
while read SSHPORT; do
        if [[ "$SSHPORT" =~ ^[0-9]{2,5}$ || "$SSHPORT" = 22 ]]; then
                if [[ "$SSHPORT" -ge 1024 && "$SSHPORT" -le 65535 || "$SSHPORT" = 22 ]]; then
                        # Create backup of current SSH config
                        NOW=$(date +"%m_%d_%Y-%H_%M_%S")
                        cp /etc/ssh/sshd_config /etc/ssh/sshd_config.inst.bckup.$NOW
                        # Apply changes to sshd_config
                        sed -i -e "/Port /c\Port $SSHPORT" /etc/ssh/sshd_config
                        echo -e "Restarting SSH in 5 seconds. Please wait.\n"
                        sleep 5
                        # Restart SSH service
                        service sshd restart
                        echo ""
                        echo -e "The SSH port has been changed to $SSHPORT. Please login using that port to test BEFORE ending this session.\n"
                        exit 0
                else
                        echo -e "Invalid port: must be 22, or between 1024 and 65535."
                        echo -n "Please enter the port you would like SSH to run on > "
                fi
        else
                echo -e "Invalid port: must be numeric!"
                echo -n "Please enter the port you would like SSH to run on > "
        fi
done

echo ""

