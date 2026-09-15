n = int(input("Enter odd number: "))

if n % 2 == 1:
    for i in range(n // 2 + 1):
        print(" " * (n // 2 - i), end="")

        if i == 0:
            print("*")
        else:
            print("*" + " " * (2 * i - 1) + "*")

    for i in range(n // 2 - 1, -1, -1):
        print(" " * (n // 2 - i), end="")

        if i == 0:
            print("*")
        else:
            print("*" + " " * (2 * i - 1) + "*")
else:
    print("invalid input")