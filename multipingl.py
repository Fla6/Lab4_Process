#import os
#ip = input('Write IP: ')
#response = os.system("ping -c 3 " + ip)
#if response == 0:
#    pingstatus = "Network Active"
#    print(pingstatus)
#else:
#    pingstatus = "Network Error"
#    print(pingstatus)



import os, pingl
from multiprocessing import Process


if __name__ == "__main__":
    with open('input.txt') as file:
        dump = file.read()
        dump = dump.splitlines()

        
    for ip in dump:
        #a = os.system('ping -c 2 {}'.format(ip))
        a = pingl.ipping(ip)
        # if a == 0:
        #     pingstatus = "Network Active"
        #     print(pingstatus, "\n")
        # else:
        #     pingstatus = "Network Error"
        #     print(pingstatus, "\n")