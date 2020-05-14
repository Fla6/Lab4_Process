import os, time
from multiprocessing import Process
from pingl import ipping

if __name__ == "__main__":
    with open('input2.txt') as file:
        dump = file.read()
        dump = dump.splitlines()

    procs = []
    list = []
    for ip in dump:
        list.append(ip)

    for index, ip in enumerate(list):
        proc = Process(target=ipping, args=(ip,))
        procs.append(proc)
        time.sleep(3)
        proc.start()

    for proc in procs:
        proc.join()