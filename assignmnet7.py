
def sum_func():
	li=[ i**2 if i % 2 == 1 else -i**2 for i in range(1,11)]
	return sum(li)

print sum_func() 



