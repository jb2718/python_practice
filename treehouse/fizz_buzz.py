name = input("Please enter your name: ")
number = int(input("Please enter a number: "))

print("Hello,", name)
print("You entered", number)


is_fizz = number % 3 == 0
is_buzz = number % 5 == 0

if is_fizz and not is_buzz:
    print(number, "is a Fizz number")
elif not is_fizz and is_buzz:
    print(number, "is a Buzz number")
elif is_fizz and is_buzz:
    print(number, "is a FizzBuzz number")
else:
    print(number, "is neither a fizzy nor a buzzy number")

