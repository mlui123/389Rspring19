# Writeup 7 - Binaries I

Name: *Mitchell Lui*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Mitchell Lui*

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
#include <stdio.h>

int main () {
    int a = 0xfeedface;
    int b = 0x1ceb00da;

    printf("a = %d\n", a);
    printf("b = %d\n", b);

    a = b^a;
    b = b^a;
    a = b^a;

    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;
}

```

### Part 2 (10 Pts)

*We start by printing 2 hex values. Then we perform a few xor operations on the hex values which swaps the values and finally we print the updated hex values.*
