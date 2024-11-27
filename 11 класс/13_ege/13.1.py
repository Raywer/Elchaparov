from ipaddress import *
mask='255.255.248.0'
ip='135.12.171.214'
net = ip_network(f'{ip}/{mask},0')
print(net)
