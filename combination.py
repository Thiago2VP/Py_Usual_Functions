def fatorial(num):
	fat = 1
	while(num > 1):
		fat *= num
		num -= 1
	return fat

def arranjo(total, organ):
	return fatorial(total) / fatorial(total - organ)

print("O fatorial é %d" %(fatorial(21)*fatorial(3)))