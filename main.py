# this is Chris Glanzer's RSA keygen script for Math-201 w/ Spanier
from functools import reduce


# code reference
# https://rosettacode.org/wiki/Modular_inverse#Python


# concept behind the (x, lastx, y , lasty) method for the Extended euclidian algorithm,
# in contrast to how we do it by hand
# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
def extended_gcd(aa, bb):
   lastremainder, remainder = abs(aa), abs(bb)
   #x, lastx, y, lasty = 0, 1, 1, 0
   x, lastx= 0, 1
   while remainder:
      lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
      x, lastx = lastx - quotient*x, x
      #y, lasty = lasty - quotient*y, y
   #return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
   return lastremainder, lastx * (-1 if aa < 0 else 1)

def modinv(a, m): # a=a^1(modm), returns x=a^(-1)(modm)
	#g, x, y = extended_gcd(a, m)
   g, x = extended_gcd(a, m)
   if g != 1:
	   raise ValueError
   #return x % m, y % m
   return x % m

if __name__ == '__main__':
   print("provide me two large primes, p first:")
   p=int(input())
   print("and then q second:")
   q=int(input())
   n=p*q
   m=(p-1)*(q-1)
   print("\nn= p*q,\nn= " +str(n) +"\n\nm= (p-1)*(q-1), \nm= "+ str(m)+"\n")
   print("Next we'll need a number, e, which is coprime to m:")
      #build a serialized list of primes less than ~10^100
      #add in a function that builds a list of coprimes,
      #make sure to filter out known traditional primes, so we build a shorter, denser list of unique coprimes
   e=int(input())
   d=modinv(e,m)
   print("Inverse of e (e^-1(modm)) is d= "+str(d)+"\n\nPublic key pair to encrypt (message x):\t"+str(e)+" & "+str(n)+"\n\tx^e(modn)=y ----> encrypted\n\tx^"+str(e)+"(mod"+str(n)+")\n\nPrivate key to decrypt y(encrypted message x):\t"+str(d)+"\n\ty^d(modn)=y ----> decrypted\n\ty^"+str(d)+"(mod"+str(n)+")\n")
   print("\n this window will self destruct... hit any key to continue")
   input() 

    
       
    
  






