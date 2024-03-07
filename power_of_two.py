# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.


try:
    # Integer input from user
    number = int(input("Please enter an integer: "))

    # Check if the number is a power of two
    if number!=0 and (number & (number - 1)) == 0:
        print("True")

    else:
        print("False")


#Incase user does not enter an integer
except ValueError:
    print("Invalid input")
