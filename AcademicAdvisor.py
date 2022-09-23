#Program Name: AcaDemic Adisor (ADA)
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

#These are things that the program should "remember" if they're brought up.
studentName = None
studentGrade = None
studentMajor = None
studentCredits = None
studentGPA = None
#first the adivsor will ask basic questions that can be used later
print("> Hello, I am Ada, your acadmic advisor. What's your first name?")
#loop to get name
while studentName == None:
    inputString = input("< ")
    #Use capture groups to get things that will be remembered
    if re.search(r"(?:(?:My name(?:'| i)s )|(?:I(?:'| a)m ))?([A-Z][a-z|'-]+)\.", inputString):
        thisMatch = re.search(r"(?:(?:My name(?:'| i)s )|(?:I(?:'| a)m ))?([A-Z][a-z|'-]+)\.", inputString)
        studentName = thisMatch.group(1)
        print("> What can I do for you", studentName + "?")
    else:
        print("> I didn't catch that. Tell me again, using proper grammar.")
#Rank system used in Eliza implemented by order of elifs. The highest ranked ones are those that will involve
#values that will be saved.
#System will assume input is in complete and grammatically correct sentences.
while True:
    #Responses will always start with ">".
    outputString = "> "
    #User input will always be prompted by "<"."
    inputString = input("< ")
    #Match function means it looks at beginning of sentence, so no need for start of sentence operator. Will match
    #only if "exit" is typed by itself.
    if re.match(r"exit$", inputString):
        break
    #If user wants to aks something.
    elif re.search(r"(?:Can|May) I ask(?: you)? (?:something(?: else)?|a(?:nother)? question)\?", inputString):
        #responses shouldn't always be the same, which can be handled by having a list of responses and randomly choosing
        responseList = ["What do you need help with?", "Ask away.", "Go ahead."]
        outputString += responseList[randint(0,len(responseList)-1)]
    #If input contains keyword "major".
    elif re.search(r"[Mm]ajor", inputString):
        #If major hasn't been discussed before, ADA will ask about the major in a loop until a valid input is received.
        while studentMajor == None:
            print("> Before we talk about your major, tell me what you're majoring in.")
            inputString = input("< ")
            thisMatch = re.search(r"(?:(?:My major is )|(?:I'm majoring in )|(?:It's ))?([A-Za-z][a-z]+(?:'s)? ?[A-Za-z]*)\.", inputString)
            if thisMatch:
                studentMajor = thisMatch.group(1).lower()
        #After major is recorded, program will ask general question about major.
        print("> What would you like to know about "+ studentMajor +", " + studentName + "?")
    #If the user mentions graduation
    elif re.search(r"[Gg]raduat(?:e|ion)", inputString):
        while studentCredits == None:
            print("> How many credits do you have?")
            inputString = input("< ")
            #Get number of credits from response
            thisMatch = re.search(r"([0-9]{1,3}).*",inputString)
            if thisMatch:
                studentCredits = int(thisMatch.group(1))
                if studentCredits < 60:
                    print("> You're not quite halfway there.")
                else:
                    print("> You're more than halfway there.")
        while studentGPA == None:
            print("> Ok, what's your GPA?")
            inputString = input("> ")
            thisMatch = re.search(r"([0-9]{1}\.[0-9]{1,3}).*", inputString)
            if thisMatch:
                studentGPA = float(thisMatch.group(1))
                if studentGPA < 2.0:
                    print("> Your GPA is currently below average.")
                else:
                    print("> Your GPA is currently above average.")
        outputString += "What would you like to know about graduation?"
    elif re.search(r"My [A-Za-z]* ?\.$", inputString):
        
        outputString += re.sub(r"My (.*\.$)", r"What about your", inputString)
    #Response to user asking for Ada to do something.
    elif re.search(r"Can you .*\?", inputString):
        outputString += ("I'm sorry " + studentName+ ", I'm afraid I can't do that.")
    #If no pattern or keyword is found, program will respond randomly from list of responses.
    else:
        responseList = ["I didn't catch that.", "Say that again.", "Slow down there.", "Uh, what?", "I don't understand."]
        outputString += responseList[randint(0,len(responseList)-1)]
    print(outputString)
