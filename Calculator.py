a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Select operation to perform: ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Choose an operation from above (1/2/3/4)"))

if choice == 1:
    result = a + b
    print("sum is: ", result)

elif choice == 2:
    result = a - b
    print("difference is: ", result)

elif choice == 3:
    result = a*b
    print("product is : ", result)

elif choice == 4:
    if b == 0:
        print("invalid input, can not divide by zero.")

    else:
        result = a/b
        print("division is: ", result)