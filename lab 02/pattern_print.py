# PATTERN PRINTING USING NESTED LOOPS

# Printing square
print("SQUARE: ")
n = int(input("Enter lenght of square: "))
for i in range(1,n+1):
    for j in range(1,n+1):
       print("* ", end="")
    print(" ")
print(" ")


# Print right angled triangle
print("RIGHT ANGLED TRIANGLE: ")
n = int(input("Enter the height of right triangle: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    print(" ")
print(" ")

# Print triangle
print("")
print("TRIANGLE: ")
n = int(input("Enter the height of triangle: "))
for i in range(1,n+1):
   for j in range(1,n+1-i):
       print(" ", end = "")
   for k in range(1,2*i):
       print("*", end = "")
   print("")
print(" ")  


# Print number pattern
print("NUMBER PATTERN: ")
n = int(input("Enter number of rows to print: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print(" ")
print(" ")


# Print number pattern square




            