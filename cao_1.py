import sys
rep='y'
print("IEEE 754 FLOATING POINT TO DECIMAL NUMBER")
while(rep=='y'):
	fp=input("\nEnter the IEEE 754 floating point no:")
	fp=fp.replace(" ","")
	if(len(fp)<32 or len(fp)>32):
		print("Enter 32 bit number")
		sys.exit()
	else:
		if(int(fp[0])==0):
			x='+'
		else:
			x='-'
		fp=fp[1:len(fp)]
		exp=fp[0:8]
		mantissa=fp[8:]
		E=0
		j=7
		for i in range(0,len(exp)):
			E+=int(exp[i])*(2**j)
			j=j-1
		e=E-127
		i_p='1'+mantissa[0:e]
		d_p=mantissa[e:]
		i_n=0
		d_n=0
		for i in range(0,len(i_p)):
			i_n+=int(i_p[i])*(2**(len(i_p)-1-i))
		for i in range(0,len(d_p)):
			d_n+=int(d_p[i])*(2**-(i+1))
		num=x+str(i_n+d_n)		
		print("Decimal number: ",num)
		rep=input('\nDo u want to continue?(y/n) ')
