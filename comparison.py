def main():
    score = int(input("What is the score(integer) you got? ").strip())
    print(f"Your grade is {grade_generator(score)}")
    if isEven(score):
        print("Score number is even")
    else:
        print("Score number is odd")

def grade_generator(score):
    if score == 100:
        return "S"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"

def isEven(n):
    return n%2==0       ## return True if n%2==0 else False (other way of writing)

## Use of match keyword and case statements
##    match name:
##        case "A" | "B" | "C":
##            print("abc")
##        case "D":
##            print("def")
##        case _:
##            print("what else!")

main()