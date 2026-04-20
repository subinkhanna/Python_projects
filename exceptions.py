def main():
    print(f"Your number is {get_int()}")

def get_int():
    while True:
        try:
            x = int(input("Enter the number of your choice: "))
            return x
        except ValueError:
            print("You did not enter the integer number. Try again")        ##or pass if no message is to be thrown to user. 

main()