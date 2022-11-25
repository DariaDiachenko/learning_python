import re


def my_fun():
    value = input("Please enter IP address:\n")
    # print('You entered {value}')
    match = re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", value)
    if match:
        print('IP: ', match.group())
    else:
        print('You entered incorrect IP')


my_fun()
