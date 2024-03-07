"""
Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit
ordering.
"""

#Take integer input
num=int(input("Enter an integer with more than one digit:"))

def reverse_integer(num):
    # Check if the number is negative
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)

    # Convert the number to a string
    reversed_string=(num)[::-1]
    reversed_num = int(reversed_string)

    # Return the reversed number with the original sign if it was negative
    return -reversed_num if is_negative else reversed_num

reversed_num = reverse_integer(num)
print("Reversed number:", reversed_num)