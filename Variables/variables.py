"""
 Variable are containers for values inside the computer's memory
 Variables can store Strings, Numbers, Pictures etc
 In This File we will learn to use variables in python
"""

name = input("Hi! What is your name? ");
#strip() method removes white spaces from the string. just as trim does in JavaScript

name = name.strip();

# capitalize() method Capitalizes the first character of the string

name = name.capitalize();

print("My name is", name);

print("My name is ", end="");
print(name);


print("My name is", name ,  sep="!!");

# What if i want to use double quotes in the double qoutes

print("Hello,  \"friend\"");


#if you want to pass a Variable to the string then you must write "f" outside the Double Quotations. f characters specifies that the string is not an ordinary string, it has something specil in it

print(f"Hey, {name}");