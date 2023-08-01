def fat(num):
	fat = 1
	while(num > 1):
		fat *= num
		num -= 1
	return fat

def arj(total, organ):
	return fat(total) / fat(total - organ)

print("O fatorial é %d" %(fat(21)*fat(3)))