#include <stdio.h>
int main(void)
{
	int		iVar1;
	int*	puVar2;
	int		local_84;
	int		local_7c[14];
	int		local_44[14];

	local_7c[0] = 0x7a;
	local_7c[1] = 0x69;
	local_7c[2] = 0x78;
	local_7c[3] = 0x6e;
	local_7c[4] = 0x62;
	local_7c[5] = 0x6f;
	local_7c[6] = 0x7c;
	local_7c[7] = 0x6b;
	local_7c[8] = 0x77;
	local_7c[9] = 0x78;
	local_7c[10] = 0x74;
	local_7c[11] = 0x38;
	local_7c[12] = 0x38;
	local_7c[13] = 100;
	for (local_84 = 0; local_84 < 0xe; local_84 = local_84 + 1) {
		local_44[local_84] = local_7c[local_84] ^ 0x19;
		// printf("local_7c: %c\n", local_7c[local_84]);
		// printf("local_44: %c\n", local_44[local_84]);
		// printf("%c", local_7c[local_84]);
        printf("%c", local_44[local_84]);
	}

	return 0;
}
