def main():
    sayHello()
    name = input("What's your name? ").strip().title()
    returned_value = sayHello(name)
    print(returned_value)


def sayHello(to="Stranger"):
    print(f"Hello there! {to}")


main()