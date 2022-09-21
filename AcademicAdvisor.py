import re   

print("> Hello, I am your acadmic advisor. What can I do for you?")

inputString = ""
while True:
    outputString = "> "
    inputString = input("< ")
    if re.match(r"exit$", inputString):
        break
    elif re.search(r"help", inputString):
        outputString += "What do you need help with?"
    else:
        outputString += "I don't understand."
    print(outputString)
