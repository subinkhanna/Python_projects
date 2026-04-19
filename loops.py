# for loop
for i in range(3):
    print("Meow!")

# While loop
i = 3
while i > 0:
    print("Meow!!")
    i -= 1

# range function (range(3))

print("Meow\n" * 3, end='')

## Use of break and continue in a loop
while True:
    n = int(input("Enter a positive non-zero number: ").strip())
    if n > 0:
        break
#    else:
#        continue

for _ in range(n):
    print("Meow!")