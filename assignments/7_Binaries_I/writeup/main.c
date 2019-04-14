/*
 * Name: *Mitchell Lui*
 * Section: *0101*
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: *Mitchell Lui*
 */

/* your code goes here */


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
