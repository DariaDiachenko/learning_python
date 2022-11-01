from typing import List

import numpy as np


def task4_1():
    nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

    print(nat.replace('Fast', 'Gigabit')[40:55])


task4_1()


def task4_2():
    mac = "AAAA:BBBB:CCCC"

    print(mac.replace(':', '.'))


task4_2()


def task4_3():
    config = "switchport trunk allowed vlan 1,3,10,20,30,100"
    result = config.split()
    vlans = result[-1].split(',')
    print(vlans)


task4_3()


def task4_4():
    vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
    result = sorted(vlans)
    print(list(np.unique(result)))


task4_4()


def task4_5():
    command1 = "switchport trunk allowed vlan 1,2,3,5,8"
    command2 = "switchport trunk allowed vlan 1,3,8,9"
    vlan1 = command1.split()[-1].split(",")
    vlan2 = command2.split()[-1].split(",")
    result = np.intersect1d(vlan1, vlan2)
    print(result)


task4_5()


def task4_6():
    ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
    list1 = ospf_route.replace(',', '').replace('via', '').split()

    for x in range(len(list1)):
        cat_list = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
        print("{:<20}".format(cat_list[x]), list1[x])


task4_6()


def task4_7():
    mac = "AAAA:BBBB:CCCC"
    x = ' '.join(format(ord(x), 'b') for x in mac)
    print(x)


task4_7()


def task4_8():
    ip = "192.168.3.1"
    list1 = [int(x) for x in ip.split('.')]
    ip_template = '''
    {0:<10}{1:<10}{2:<10}{3:<10}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''
    print(ip_template.format(*list1))


task4_8()
