#include <stdio.h>
char str[] = "fsdz Fdhvdu_flskhu_lv_fodvvlfdo_flskhu";


int main() {
    size_t i = 0;
    while (str[i]) {
        printf("%c", str[i++] - 3);
    }
}
