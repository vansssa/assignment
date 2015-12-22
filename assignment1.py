
def is_perfect(num):
	return sum([ i for i in range(1, num) if num%i == 0 ]) == num 
	#result=0
	#for i in listnumber:
	#	if num%i==0:
	#		result=i+result
	#return result==num

print is_perfect(6)
print is_perfect(8)

