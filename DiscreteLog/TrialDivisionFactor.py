import math

def main():
	num = raw_input(); #Get the number to factor 
	primeFactors = []; #Array to hold the prime factors
	i = 0;
	num = int(num); #gotta convert the raw_input to a num 
	factor(num, primeFactors, 0); #call factor function. Results will be stored in primeFactors[] when function returns. 
	#print the factors
	print("\n");
	print("Factors are:");
	for i in range(0, len(primeFactors)):
		print(primeFactors[i]);

#Find factors
def factor(x, primeFactors, i):
	j = 2; #Start searching for factors from 2.
	if x == 1:
		return;
	else:
		while j < math.ceil(x/2): 
			if(x % j) == 0: #found a factor 
				if isPrime(j): #test if prime
					primeFactors.append(j);
					if isPrime(x/j): #check if other branch factor is prime as well. 
						primeFactors.append(x/j);
						return;
					else:
						i += 1;
						factor((x/primeFactors[(i-1)]), primeFactors, i);  
						return;
			j += 1;
	return

#Sieve primality test. 
def isPrime(y):
	h = 2;
	while h <= math.ceil(y/2):
		if y % h == 0:
			return 0; #not prime
		h += 1;
	return 1 #cool. 