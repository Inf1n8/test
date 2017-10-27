print('DECIMAL TO IEEE 754 FLOATING POINT CONVERSION\n')
rep='y'
while(rep=='y'):
	num=float(input("\nEnter decimal number:"))
	if(num>0):
		x=0
	else:
		x=1
		num=num*-1
	div=int(num)
	dec=num-int(num)
	rem=''
	while(div>0):
		y=int(div/2)
		rem+=str(div%2)
		div=y
	rem=rem[::-1]
	i=8
	rem1=''
	while(i>0):
		i-=1
		dec=dec*2
		rem1+=str(int(dec))
		dec=dec-int(dec)
	fp=rem+rem1
	E=127+len(rem)-1
	rem=''
	while(E>0):
		y=int(E/2)
		rem+=str(E%2)
		E=y		
	rem=rem[::-1]
	fp=fp[1:len(fp)]
			
	if(len(fp)<23):
		fp+='0'*(23-len(fp))
	print('IEEE 754 floating point single precision:',x,rem,fp)	
	rep=input("\nDo u want to continue?(y/n)")
