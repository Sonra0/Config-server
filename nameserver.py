def dns():
    print("1. Google DNS")
    print("2. Cloudflare DNS")
    print("3. Shecan DNS")
    print("4. Electro DNS")
    print("0. Exit")
    print("ENTER YOUR NUMBER :",end="")
    num2 = int(input())
    if num2 == 1 :
        file = open('/etc/resolv.conf', 'w')
        file.write("nameserver 8.8.8.8\nnameserver 8.8.4.4")
        file.close()
        print("DNS sets successfully")
    if num2 == 2 :
        file = open('/etc/resolv.conf', 'w')
        file.write("nameserver 1.1.1.2\nnameserver 1.0.0.2")
        file.close()
        print("DNS sets successfully")
    if num2 == 3 :
        file = open('/etc/resolv.conf', 'w')
        file.write("nameserver 178.22.122.100\nnameserver 185.51.200.2")
        file.close()
        print("DNS sets successfully")
    if num2 == 4 :
        file = open('/etc/resolv.conf', 'w')
        file.write("nameserver 78.157.42.100\nnameserver 78.157.42.101")
        file.close()
        print("DNS sets successfully")
    else :
        continue