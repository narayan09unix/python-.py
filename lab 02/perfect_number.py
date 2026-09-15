# checking for perfect number

n = int(input("Enter the number: "))

if n <= 0:
    print("NOT a perfect number.")
else:
    total = 0
    for i in range(1,n):
         if( n % i == 0):
            total = total + i

    if ( total == n ):
        print(n, "is a perfect number.")
    else:
        print(n, "is NOT a perfect number.")

# perfect numbers in given range

a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))

print("Perfect numbers in range are: ")

for j in range(a,b):
    total = 0
    for i in range(1,j):
        if j % i == 0:
            total = total + i

    if total == j:
        print(j)
