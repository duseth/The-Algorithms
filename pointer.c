#include <stdio.h>
#include <string.h>
int main() {
char str_a[20];
char *pointer;
char *pointer2;
// A 20-element character array
// A pointer, meant for a character array
// And yet another one
strcpy(str_a, "Hello, world!\n");
pointer = str_a; // Set the first pointer to the start of the array.
printf(pointer);
pointer2 = pointer + 2;
printf(pointer2);
strcpy(pointer2, "y you
printf(pointer);
// Set the second one 2 bytes further in.
// Print it.
guys!\n"); // Copy into that spot.
// Print again.
}
