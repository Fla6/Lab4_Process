import os,time
from multiprocessing import Process

def ipping (ip):
    proc = os.getpid()
    print("\n", 'Process id: {}'.format(proc), "\n")
    os.system('nmap -sP {}'.format(ip))
    

if __name__ == "__main__":
    ip = []
    ipip = input('Write IP: ')
    ip.append(ipip)
    procs = []

    for index, ip in enumerate(ip):
        proc = Process(target=ipping, args=(ip,))
        time.sleep(2)
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()