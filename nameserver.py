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