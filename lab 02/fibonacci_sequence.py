# Printing fibonacci sequence upto n terms

print("FIBONACCI SEQUECNE BY REASSINMENT OF VARIABLES.")
n = int(input("Enter the number of terms: "))

a = 0
b = 1

if n == 1:
   print(a, end = " ")

if n == 2:
   print(a, end = " ")
   print(b, end = " ")

if n > 2:
    print(a, end = " ")
    print(b, end = " ")
    for i in range(1, n-1):
        c = a + b
        a = b
        b = c
        print(c, end = " ")

print("")

# fibonacci sequence by recursion
print("")
print("FIBONACCI SEQUENCE BY RECURSION. ")

count = 0
def fibonacci(n):
    global count
    count = count + 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(1,n+1):
    print(fibonacci(i), end = " ")

print("")
print("Total number of function calls by recursion: ", count)