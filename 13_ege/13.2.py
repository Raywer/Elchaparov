from ipaddress import *
ip_сети='220.128.96.0'
ip_узла='220.128.112.142'
for mask in range(33):
    net = ip_network(f'{ip_узла}/{mask},0')
    if ip_сети in str(net):
        print(net.netmask)

