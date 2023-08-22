def fat(num):
	if (num == 1):
		return 1
	else:
		return num * fat(num - 1)

def arj(total, organ):
	return fat(total) / fat(total - organ)

# print("O fatorial é %d" %(fat(21)*fat(3)))

num = int(input())
print("O Fatorial é %d" % (fat(num)))