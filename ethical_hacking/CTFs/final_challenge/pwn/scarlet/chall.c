#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
    int a, b, c;
    char buf[0x16];

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    puts("Welcome to the Scattered Shell Surge, where the shell is scattered and the surge is real.");
    read(0, buf, 0x44);

    strcpy(buf, "Bye now");
    a = 1;
    b = 2;
    c = 3;

    puts("Thanks for playing!");
    puts(buf);
    return 0;
}