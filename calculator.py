#x = int(input("Enter first integer number for calculation: ").strip())
#y = int(input("Enter second integer number for calculation: ").strip())
#print(x + y)

x = float(input("Enter first real number for calculation: ").strip())
y = float(input("Enter second real number for calculation: ").strip())
z = round((x + y), 4)
print(f"The resulting rounding number is {z:,}")

## Division problem with rounding within f string
x = float(input("Enter first real number for division: ").strip())
y = float(input("Enter second non-zero real number for division: ").strip())
z = x / y
print(f"The resulting rounding number is {z:.2f}")
