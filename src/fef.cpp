#include <iostream>
#include <string>

enum Color 
    {
        red,
        yellow,
    };

int main(int argc, char **argv) {

    Color a = red;
    std::cout << typeid((a)).name();



    return 0;
}