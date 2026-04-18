## print function - string object methods 
#print("hello there! What is your name?")
# Greet and ask user for their name
name = input("hello there! What is your name? ").strip().capitalize()
# name.title() 
# Say hello
# print("hello " + name)
# print("hello ", name)    # , also concatenates with extra space
# print("hello, ", name, end= '. ')  with end
print(f"hello, {name}")

# Split the string into two parts
first, last = name.split(" ")
print(f"hello, {first}")