#include <stdio.h>

int isPalindrome(int num) {
    int original = num, reversed = 0, rem;

    while (num > 0) {
        rem = num % 10;
        reversed = reversed * 10 + rem;
        num /= 10;
    }

    return (original == reversed);
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);

    if (isPalindrome(n))
        printf("%d is a Palindrome Number\n", n);
    else
        printf("%d is Not a Palindrome Number\n", n);

    return 0;
}
