#!/usr/bin/env python
# coding: utf-8

# Print only the words that start with s in this sentence

st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0]=='s':
     print(word)
    
st = 'Sam Print only the words that start with s in this sentence'
for word in st.split():
    # if word[0]=='s' or word[0]=='S':
   if word[0].lower() == 's': 
    # print Sam, start, s, sentence...so include word with S
    print(word)

# Use range() to print all the even numbers from 0 to 10

list(range(0,10,2))


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3


[x for x in range(1,51) if x%3==0]


# Go through the string below and if the length of a word is even print "even!"


st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2==0:
     print(word,"..has even number of letter")


# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"

#range(a,b+1) cause it will end with 99 in this case and we do not want it..
for num in range(1,101):
    # multiple three and five are also three of five, so let's go with three and five first
    if num%3==0 and num%5==0:
        print(num," FizzBizz")
    elif num%3==0:
        print(num, " Fizz")
    elif num%5==0:
        print(num," Bizz")
    else:
        print(num)


# Use List Comprehension to create a list of the first letters of every word in the string below


st = 'Create a list of the first letters of every word in this string'
[word[0] for word in st.split()]





