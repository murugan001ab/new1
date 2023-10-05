"""
get input to user  a line of words
then pass it in for loop
the reverce a string
"""
revstr=""
str=input("enter a string").split(" ")
for words in str:
    print(words[::-1],end=" ")
