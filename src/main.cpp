#include <iostream>



int main(int argc, char* argv[])
{
    #ifdef DEBUG
        std::cout<<"Hello from debug mode"<<std::endl;
    #else 
        std::cout<<"Hello from release mode"<<std::endl;
    #endif 

    #ifdef _WIN32
        std::cout<<"You are running this program on windows."<<std::endl;
    #else
        std::cout<<"You are running this program on linux."<<std::endl;
    #endif // DEBUG


}
