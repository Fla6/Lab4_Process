#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
#include "ping.h"
#include <fstream>
using namespace std;

int main()
{
    ifstream fout;
    fout.open("input2.txt");
    char host[BUFF_LEN] = { 0, };
    pid_t pid;
    while (!fout.eof())
    {
        fout >> host;
        switch (pid = fork())
        {
        case -1:
            cerr << "Error\n";
            exit(1);
            
        case 0:
            cout << "Child\n" << endl;
            sleep(1);
            cout << "Process id: " << getpid() << endl << endl;
            ping(host);
            cout << endl << "Child done\n";
            exit(0);

        default:
            cout << "Parent\n";
            wait(0);
            cout << "Parent done\n\n";
        }
    }    
    return 0;
}