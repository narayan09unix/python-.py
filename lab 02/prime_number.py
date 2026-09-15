# checking for Prime number

n = int(input("Enter the number: "))

if n <= 1:
   print(n, "is NOT a prime number")
   
else:
   is_prime = True
   for i in range(2,n):

      if n % i == 0:
         is_prime = False
         break

   if(is_prime):
      print(n,"is a prime number.")
   else:
      print(n,"is NOT a prime number.")
print("")

# display prime numbers in the given range

a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))

print("PRIME NUMBERS in given range are: ")

count = 0

if( a == 1 ):
   a = a + 1
   
for j in range(a,b+1):
   is_prime = True

   for i in range(2,j):
     if j % i == 0:
         is_prime = False
         break

   if(is_prime):
      print(j)
      count = count + 1 

print("Total prime number in range: ", count)

  