#include <iostream>
using namespace std;

#define BUFF_LEN 1024

void ping(const char host[BUFF_LEN])
{   
    string ping = "ping -c 2 ";
    ping.append(host);
    system(ping.c_str());  
}