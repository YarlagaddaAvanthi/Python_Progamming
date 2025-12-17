num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print(num, "is not prime")
            break
    else:
        print(num, "is prime")
else:
    print(num, "is not prime")
