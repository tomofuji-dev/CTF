origin = "ocip{FTC0l_I4_t5m_ll0m_y_y3n2fc10a10ÿì}"
ans = ""
for i in range(0, len(origin), 4):
	ans += origin[i:i+4][::-1]
print(ans)