import os,time
from multiprocessing import Process

def ipping (ip):
    os.system('ping -c 2 {}'.format(ip))
    proc = os.getpid()
    print('Process id: {}'.format(proc), "\n")

if __name__ == "__main__":
    ip = ["127.0.0.1", "ya.ru", "173.194.73.101"]
    #ip = input('Write IP: ')
    procs = []

    for index, ip in enumerate(ip):
        proc = Process(target=ipping, args=(ip,))
        time.sleep(2)
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
    #ipping(ip)