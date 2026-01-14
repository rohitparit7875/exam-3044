#include <stdio.h>

int main() {
    int a = 5, b = 8, c = 3;

    if (a > b && a > c)
        printf("A is largest");
    else if (b > c)
        printf("B is largest");
    else
        printf("C is largest");

    return 0;
}
