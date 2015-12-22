
import sys

def get_max_of_n(file,n):
	result=[0]*n
	with open(file,'r') as f:
		li=[ int(line.strip()) for line in f ]			
		while n > 0 :
			result[n-1]=max(li)
			li.remove(max(li))
			n = n - 1
   	return result

#print get_max_of_n('sample.txt',4)
if len(sys.argv) == 2:
	print get_max_of_n(sys.argv[1],3)
else:
	print "No input file"



