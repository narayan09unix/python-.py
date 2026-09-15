# Menu Driven Application
while True:
    print("")
    print("---- SELECT OPTION FROM THE MENU ----")
    print("1. ARMSTRONG NUMBER ")
    print("2. PRIME NUMBER.")
    print("3. PERFECT NUMBER.")
    print("4. PALINDROME.")
    print("5. FIBONACCI SERIES.")
    print("6. PATTERN PRINTING.")
    print("7. EXIT THE PROGRAM.")
    print("--------------------------------------")

    choice = int(input("Enter your choice: "))
    print("--------------------------------------")


    match choice:
        case 1:
            # checking for armstrong number
            n = int(input("Enter the number: "))
            original = n

            digits = 0
            while n != 0:
                n = n // 10
                digits = digits +1

            n = original
            total = rem = 0
            while n != 0:
                rem = n % 10
                total = total + pow(rem,digits)
                n = n // 10

            if total == original:
                print(original, "is an armstrong number.")
            else:
                print(original, "is NOT an armstrong number.")

            # display armstrong numbers in given range
            a = int(input("Enter lower limit of range: "))
            b = int(input("Enter upper limit of range: "))
            print("Armstrong numbers in given range are: ")

            for j in range(a,b+1):
                real = j
                digits = 0

                while j != 0:
                    j = j // 10
                    digits = digits + 1

                j = real
                total = rem = 0

                while j != 0:
                    rem = j % 10
                    total = total + pow(rem, digits)
                    j = j // 10

                if total == real:
                    print(real)


        case 2:
            # checking for prime numbers
            n = int(input("Enter the number: "))

            if n <= 1:
                print(n, "is NOT a prime number.")
            else:
                is_prime = True
                for i in range(2,n):

                    if n % i == 0:
                        is_prime = False
                        break

                if(is_prime):
                    print(n,"is a prime number.")
                else:
                    print(n, "is NOT a prime number.")
            print("")

            # display prime numbers in given range
            a = int(input("Enter the lower limit: "))
            b = int(input("Enter the upper limit: "))

            print("Prime numbers in given range are: ")
            count = 0

            if(a == 1):
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
            print("Total prime numbers in range: ", count)


        case 3:
            # checking for perfect number
            n = int(input("Enter the number: "))

            if n <= 0:
                print("NOT a perfect number.")
            else:
                total = 0
                for i in range(1,n):
                    if(n % i == 0):
                        total = total + i

                if ( total == n):
                    print(n, "is a perfect number.")
                else:
                    print(n, "is NOT a perfect number.")

            # display perfect number in given range
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

        case 4:
            # checking number for palindrome
            n = int(input("Enter the number: "))
            original = n
            digit = 0
            reverse = 0

            while n != 0:
                digit = n % 10
                reverse = reverse*10 + digit
                n = n // 10

            if(reverse == original):
                print(original, "is Palindrome.")
            else:
                print(original, "is NOT a Palindrome.")
            print("")

            # checking palindrome for string
            s = input("Enter the string: ")

            reverse = "" 
            i = len(s) - 1

            while i >= 0:
                reverse = reverse + s[i]
                i = i - 1

            print("Reversed string: ", reverse)

            if( reverse == s):
                print(s, "is Palindrome.")
            else:
                print(s, "is NOT a Palindrome.")


        case 5:
            # display fibonacci sequence upto n terms
            print("Fibbonacci sequence by reassignment of variable.")
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
            print("Fibonacci sequence by recursion.")

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


        case 6:
            # pattern printing
            # squre
            print("Square: ")
            n = int(input("Enter length of square: "))
            for i in range(1,n+1):
                for j in range(1,n+1):
                    print("* ", end = "")
                print(" ")
            print(" ")

            # right angled triangle
            print("Right angled triangle.")
            n = int(input("Enter the height of right triangle: "))
            for i in range(1,n+1):
                for j in range(1,i+1):
                    print("*", end="")
                print("")
            print("")

            # triangle
            print("")
            print("Trianle")
            n = int(input("Enter the height of triangle: "))
            for i in range(1,n+1):
                for j in range(1,n+1-i):
                    print(" ", end = "")
                for k in range(1,2*i):
                    print("*", end = "")
                print("")
            print("")

            # number pattern
            print("Number pattern")
            n = int(input("Enter the number of rows: "))
            for i in range(1,n+1):
                for j in range(1,i+1):
                    print(j, end="")
                print(" ")
            print(" ")


        case 7:
            print("Program succesfully executed.")
            print("THANK YOU! :) ")
            break

        case _:
            print("Invalid choice!")
            print("Please! select from the given choices( 1-7 ).")

  s