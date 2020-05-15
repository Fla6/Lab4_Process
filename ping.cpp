#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
#include "ping.h"
using namespace std;

int main()
{
    char host[BUFF_LEN] = { 0, };
    cout << "Enter IP: ";
    cin.get(host, BUFF_LEN);
    cout << endl;
    pid_t pid;
    switch (pid = fork())
    {
    case -1:
        cerr << "Error\n";
        exit(1);
    
    case 0:
        cout << "Child\n" << endl;
        //sleep(1);
        cout << "Process id: " << getpid() << endl << endl;
        ping(host);
        cout << endl << "Child done\n";
        exit(0);

    default:
        cout << "Parent\n";
        wait(0);
        cout << "Parent done\n";
    }
    return 0;
}