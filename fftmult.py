import math
import cmath

def fft(a,x):
	n = len(a)
	if(n <= 0):
		print "\nERROR going to use FFT on list of size <=0"
		quit()
	A = [complex] * n 
	if (n==1):
		A[0] = a[0]
		return A
	if(x == 1):
		wn = complex(cmath.rect(1, 2*cmath.pi/n))
	else:
		wn = complex(1,0)/complex(cmath.rect(1, 2*cmath.pi/n))
	w = complex(1,0)
	n_2 = n/2
	a_even = [complex] * n_2 
	a_odd = [complex] * n_2
	for i in range(0,n_2):
		a_even[i] = a[i*2]
		a_odd[i] = a[i*2+1]
	A_even = fft(a_even,x)
	A_odd = fft(a_odd,x)
	for k in range(0,n_2):
		A[k] = A_even[k] + (A_odd[k] * w)
		A[k+n_2] = A_even[k] - (A_odd[k] * w)
		w = w * wn
	return A

# def ifft(A):
# 	a = fft(A)
# 	n = len(A)
# 	n_2 = n/2
# 	for i in range(0,n):
# 		a[i] = a[i]/n
# 	for i in range(1,n_2):
# 		a[i],a[n-i] = a[n-i],a[i]
# 	return a

def nextPowerofTwo(n):
	k = 1
	while(True):
		if(k>=n):
			return k
		k = k * 2
def max(a,b):
	if(a>=b):
		return a
	return b
def paddWithZero(a,N,paddingElt):
	n = len(a)
	if(n == 0):
		return
	eSize = N-n
	# print eSize
	if(eSize == 0):
		return
	b = [type(a[0])] * eSize
	for i in range(0,eSize):
		b[i] = paddingElt
	c = a+b
	return c

def recombine(c,B):
	n = len(c)
	print "\nn = ",n
	print "\nB = ",B
	d = [type(c[0])] * n
	carry = 0
	for i in range(0,n):
		d[i] = c[i] + carry
		if(d[i]>=B):
			carry = d[i]//B
			d[i] = d[i]%B
		else:
			carry = 0
	if(carry!=0):
		print("\nERROR TOO MUCH CARRY")
		quit()
	return d

def fftmult(a,b,Base):
	n1 = len(a)
	n2 = len(b)
	a.reverse()
	b.reverse()
	n = max(n1,n2)
	n = nextPowerofTwo(n)
	# print "\nn1 = ",n1," n2 = ",n2," n = ",n
	x = paddWithZero(a,2*n,complex(0,0))
	y = paddWithZero(b,2*n,complex(0,0))
	# print "\nx = ",x
	# print "\ny = ",y
	A = fft(x,1)
	B = fft(y,1)
	C = [complex] * 2 * n
	for i in range(0,2*n):
		C[i] = A[i] * B[i]
	# print "\nA = ",A
	# print "\nB = ",B
	# print "\nC = ",C
	c = fft(C,0)
	# print "\nc = ",c
	d = [int] * 2 * n
	for i in range(0,2*n):
		d[i] = int(round(c[i].real/(2*n)))
	# print "\nd = ",d
	e = recombine(d,Base)
	# print "\ne = ",e
	e.reverse()
	return e

def main():
	s = raw_input("Enter Digits separated by space :\n")
	a = [int(x) for x in s.split()]
	s = raw_input("Enter Digits separated by space :\n")
	b = [int(x) for x in s.split()]
	B = int(raw_input("Enter Base :\n"))
	print "\na = ",a
	print "\nb = ",b
	print "\nBase = ",B
	c = fftmult(a,b,B)
	print "\noutput = \n",c
	return

main()
quit()
