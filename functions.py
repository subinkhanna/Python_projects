def main():
    sayHello()
    name = input("What's your name? ").strip().title()
    #returned_value = sayHello(name)
    #print(returned_value)
    sayHello(name)
    x = int(input("What integer number you wish to square? ").strip())
    print(f"Number squared is {raiseToPower(x)}")

def sayHello(to="Stranger"):
    print(f"Hello there! {to}")

def raiseToPower(n):
    return pow(n,2)     ## or x**y  or x * x (for square only)

main()