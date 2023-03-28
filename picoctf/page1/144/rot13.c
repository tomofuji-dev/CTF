#include <stdio.h>
int main(int argc, char* argv[]) {
    char* s = argv[1];
    while (*s != '\0') {
	if (('a' <= *s && *s <= 'z') || ('A' <= *s && *s <= 'Z')) {
	    if ('a' <= *s && *s <= 'z')
		printf("%c", 'a' + (*s + 13 - 'a') % 26);
	    else {
		printf("%c", 'A' + (*s + 13 - 'A') % 26);
	    }
	}
	else {
	    printf("%c", *s);
	}
	s++;
    }
    printf("\n");
    return 0;
}

