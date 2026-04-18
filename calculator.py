#x = int(input("Enter first integer number for calculation: ").strip())
#y = int(input("Enter second integer number for calculation: ").strip())
#print(x + y)

x = float(input("Enter first real number for calculation: ").strip())
y = float(input("Enter second real number for calculation: ").strip())
z = round((x + y), 4)
print(f"The resulting rounding number is {z:,}")
