def yell(text):
    text = text.upper()
    number_of_chars = len(text)

    result = text + "!" * (number_of_chars // 2)
    print(result)

yell("You are doing great")
yell("Don't forget to ask for help")
yell("Don't Repeat Yourself.  Keep things DRY")