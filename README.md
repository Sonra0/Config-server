# Config your server

You can have many packages to optimize your linux server and config vpn tunnel and tools. 

![photo](https://github.com/Sonra0/Config-server/blob/master/screen.png)

## Getting Started

you can clone this project in your system and don't forget to do 'git submodule init' and 'git submodule update' . 
then run main.py by python3

### Prerequisites

The things you need before run the script.

* you have to run as root
* install git
* install curl
* install python3

### Installation

A step by step guide that will tell you how to get the development environment up and running.

> make sure you are root !
> do all commands in /root/ !
```bash
apt-get -y install git
apt-get install curl
sudo git clone --recurse-submodules https://github.com/Sonra0/Config-server.git
cd Config-server
python3 main.py
```

### run by 1 command : 

```bash
cd /root/ && sudo apt-get -y install git && sudo apt-get -y install python3 && sudo apt-get -y install curl && sudo git clone --recurse-submodules https://github.com/Sonra0/Config-server.git && cd Config-server && python3 main.py
```

### After it's installed for the first time you can run it by :
```bash
cd /root/Config-server/ && python3 main.py
```

## A few examples of useful tasks :

- #### Iran firewall : ignore all requests from anywhere except from iran and your white ip list ( your destination server and etc. )

- SSL certificate

- Install Mhsanaei x-ui

- Install Alireza x-ui

- Install and config tunnels like Rathole and Chisel from Azumi

- Linux optimizers

- UFW install and setup

- Change your SSH port

- Backup your x-ui database and send it to your telegram bot

## I used below repositories in my script :
* [Alireza panel](https://github.com/alireza0/x-ui)
* [Rathole](https://github.com/Azumi67/Rathole_reverseTunnel)
* [Chisel](https://github.com/Azumi67/Chisel_multipleServers)
* [ssh_change_port](https://gist.github.com/worldadventurer/842f1a10762cba0ce27dc8f99a835377)
* [sanaei panel](https://github.com/MHSanaei/3x-ui)
* [OPIRAN linux optimizer](https://github.com/opiran-club/VPS-Optimizer/tree/4f2d14d0b2fc62af2b8d63e57e5c6a428f76ea89)
* [hawshemi linux optimizer](https://github.com/hawshemi/Linux-Optimizer)
