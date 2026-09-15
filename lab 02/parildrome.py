# Checking number for Palindrome
# user input
n = int(input("Enter the number: "))
original = n

# variable initialization
digit = 0
reverse = 0

# reversing the number
while n != 0:
   digit = n % 10
   reverse = reverse * 10 + digit
   n = n // 10

# equating with original number
if( reverse == original):
   print(original, "is Palindrome.")
else:
   print(original,"is NOT a palindrome.")
print("")


# checking palindrome for string
# user input
s = input("Enter the string: ")

# variable initialisation
reverse = ""
i = len(s) - 1

# reversing the string
while i >= 0:
   reverse = reverse + s[i]
   i = i-1

print("REVERSED STRING: ", reverse)

# comparing reverse string with original string 
if( reverse == s):
   print(s,"is Palindrome.")
else:
   print(s,"is NOT a Palindrome.")