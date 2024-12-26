#include <iostream>

int main(void) {
    int limit = 4000000;
    int total = 0;
    int a = 1;
    int b = 2;

    while (a <= limit) {
        if (a % 2 == 0) {
            total += a;
        }
        int temp = a + b;
        a = b;
        b = temp;
    }

    std::cout << total << std::endl;
    return 0;
}