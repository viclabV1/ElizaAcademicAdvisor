#Program Name: AcaDemic Adisor (ADA)
#(Yeah, I know I know)
#Author: Victor LaBrie
#Date: September 22, 2022
#THE PROBLEM/GOAL:
#The goal of this program is to try to imitate an academic advisor in the same
#way that ELIZA imitated a Georgian psychologist. That is to say, we dont' want 
#necessarily to say anything helpful, but we want to be able to take what is said and
#use it in a way to keep the user engaged in a way that it might feel like talking to someone. 
#EXAMPLE USAGE:
#THE ALGORITHM:
#1) The program starts by introducing itself and asking for the user's first name.
#   From there it will not proceed until it has a name.
#2) The program enters the main loop of the program that continues until the user
#   types "exit".
#3) The program will look for certain sentence structures and keywords. Depending
#   on what get's matched, the program will respond accordingly.
from random import randint
import re

studentName = None
studentGrade = None
studentMajor = None
studnetMinor = None
#first the adivsor will ask basic questions that can be used later
print("> Hello, I am Ada, your acadmic advisor. What's your first name?")
#loop to get name
while studentName == None:
    inputString = input("< ")
    #Use capture groups to get things that will be remembered
    if re.search(r"My name(?:'| i)s [A-Z][a-z|'-]+\.", inputString):
        thisMatch = re.search(r"My name(?:'| i)s ([A-Z][a-z|'-]+)\.", inputString)
        studentName = thisMatch.group(1)
        print("What can I do for you", studentName + "?")
    else:
        print("> I didn't catch that. Tell me again, using proper grammar.")
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
        #responses shouldn't always be the same, which can be handled by having a list of responses and randomly choosing
        responseArray = ["What do you need help with?", "Ask away.", "Go ahead."]
        outputString += responseArray[randint(0,len(responseArray)-1)]
    elif re.search(r"[Mm]ajor", inputString):
        if studentMajor == None:
            print("> Before we talk about your major, tell me what you're majoring in.")
            inputString = input("< ")
            thisMatch = re.search(r"(?:(?:My major(?:'| i)s)|(?:I'm majoring in)) ([A-Z][a-z|'-]+)\.", inputString)
            studentMajor = thisMatch.group(1)
        print("> What would you like to know about ", studentMajor, "?")
    elif re.search(r"My [A-Za-z]* ?\.$", inputString):
        outputString += re.sub(r"My .*\.$", r"What about your", inputString)
        outputString += "e"
    else:
        outputString += "I don't understand."
    print(outputString)
