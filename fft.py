import math
import cmath

def fft(a):
	n = len(a)
	if(n <= 0):
		print "\nERROR going to use FFT on list of size <=0"
		quit()
	A = [complex] * n 
	if (n==1):
		A[0] = a[0]
		return A
	wn = complex(cmath.rect(1, 2*cmath.pi/n))
	w = complex(1,0)
	n_2 = n/2
	a_even = [complex] * n_2 
	a_odd = [complex] * n_2
	for i in range(0,n_2):
		a_even[i] = a[i*2]
		a_odd[i] = a[i*2+1]
	A_even = fft(a_even)
	A_odd = fft(a_odd)
	for k in range(0,n_2):
		A[k] = A_even[k] + (A_odd[k] * w)
		A[k+n_2] = A_even[k] - (A_odd[k] * w)
		w = w * wn
	return A

def ifft(A):
	a = fft(A)
	n = len(A)
	n_2 = n/2
	for i in range(0,n):
		a[i] = a[i]/n
	for i in range(1,n_2):
		a[i],a[n-i] = a[n-i],a[i]
	return a

def driver():
	s = raw_input("Enter Digits separated by space :\n")
	a = [complex(x) for x in s.split()]
	# print len(a)
	print "\nGiven Data :\n",a
	# d = complex(2,0)
	# c = a[0] * d
	# print c
	A = fft(a)
	print "\nAfter FFT :\n",A
	b = ifft(A)
	print "\nAfter IFFT :\n",b
	return

driver()
quit()
