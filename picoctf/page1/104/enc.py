flag = input()
ans = ""
for s in flag:
	ans += chr(ord(s) >> 8)
	ans += chr(255 & ord(s))
print(ans)
