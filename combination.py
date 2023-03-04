total = int(input("Total "))
organ = int(input("Organização "))

def fatorial(num):
	fat = 1
	while(num > 1):
		fat *= num
		num -= 1
	return fat

arranjo = fatorial(total) / fatorial(total - organ)

print("O arranjo é %d" %(arranjo))