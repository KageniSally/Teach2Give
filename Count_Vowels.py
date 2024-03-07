#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence

#take input from user
text=input("Enter a string:")

def count_vowels(text):
    vowels='aeiouAEIOU'
    return sum(c in vowels for c in text)

num_of_vowels=count_vowels(text)
print(f"The text has {num_of_vowels} vowels.")