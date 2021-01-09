first_name = input("What is your first name? ")
print("Hello,", first_name)

if first_name == "JB":
    print(first_name, "is learning Python")
elif first_name == "Roald":
    print(first_name, "is learning with felow students in the Community!")
else:
    # This is for younger readers who may not be able to read
    age =  int(input("How old are you? "))
    if age <= 6:
        print("Wow, you're {}!  If you're confident with your reading already you should start learning to program!".format(age))
    print("You should totally learn Python, {}!".format(first_name))