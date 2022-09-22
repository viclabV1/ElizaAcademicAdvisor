from random import randint, random
import re

print("> Hello, I am your acadmic advisor. What can I do for you?")
inputString = ""
#rank system used in Eliza implemented by order of elifs
#system will assume input is in complete and grammatically correct sentences
while True:
    outputString = "> "
    inputString = input("< ")
    #match function means it looks at beginning of sentence, so no need for start of sentence operator
    if re.match(r"exit$", inputString):
        break
    #if input contains question
    elif re.search(r"(?:Can|May) I ask(?: you)? (?:something(?: else)?|a(?:nother)? question)\?", inputString):
        responseArray = ["What do you need help with?", "Ask away.", "Go ahead."]
        outputString += responseArray[randint(0,len(responseArray)-1)]
    elif re.search(r"My [A-Za-z]*.$", inputString):
        outputString += re.sub(r"My .*\.$", r"What about your", inputString)
        outputString += "e"
    else:
        outputString += "I don't understand."
    print(outputString)
