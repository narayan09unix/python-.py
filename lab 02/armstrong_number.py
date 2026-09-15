# checking whether entered number is armstrong or not 

n = int(input("Enter the number: "))
original = n

#number of digits
digits = 0
while n != 0:
   n = n // 10
   digits = digits + 1

n = original

#checking for armstrong number
total = rem = 0
while n != 0:
   rem = n % 10
   total = total + pow(rem,digits)
   n = n // 10

if total == original:
   print(original, "is an armstrong number.")
else:
   print(original, "is NOT an armstrong number.")


# armstrong numbers in given range
a = int(input("Enter lower limit of range: "))
b = int(input("Enter upper limit of range: "))

print("ARMSTRONG NUMBERS IN GIVEN RANGE ARE : ")

# checking each number in range
for j in range(a,b+1):
   real = j
   digits = 0

# total digits 
   while j != 0:
     j = j // 10
     digits = digits + 1

   j = real
   total = rem = 0

# checking for armstrong number
   while j != 0:
     rem = j % 10
     total = total + pow(rem,digits)
     j = j // 10

# display armstrong number
   if total == real:
     print(real)
  