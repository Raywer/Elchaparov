from ipaddress import *
ip_узла1='157.127.182.76'
ip_узла2='151.127.190.80'
for mask in range(33):
    net_1 = ip_network(f'{ip_узла1}/{mask},0')
    net_2 = ip_network(f'{ip_узла2}/{mask},0')
    if net_1 != net_2:
        print(mask)