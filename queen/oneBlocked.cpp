#include <utility>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <random>
#include <set>

using namespace std; //fight me


int randomzoro(int numberofbords){
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1,numberofbords);
    int randomX=dis(gen);
    return randomX;
}


int main(int argc, char **argv){
    set<pair<int ,int> > myset; 
    if(argc!=3){
        cout<<"usage: "<<"./blocked <number_of_blocked> <range>\n";
        return -2;
    }
    ofstream f;
    f.open("blocked.lp", ofstream::out | ofstream::trunc);
    if(f.is_open()){
    int number=atoi(argv[1]);
    for(int i=0;i<number;++i){
        if(myset.size()>=(atoi(argv[2])*atoi(argv[2])-1))
            return -1;
        pair<int, int> Mybord;
        int bourds=atoi(argv[2]);
        Mybord.first=randomzoro(bourds);
        Mybord.second=randomzoro(bourds);
        if(myset.count(Mybord)){
            --i;
            continue;
        }
        else
            myset.insert(Mybord);
        f<<"blocked("<<Mybord.first<<","<<Mybord.second<<").\n";
    }
    f.close();
    }
    return 1;
}
