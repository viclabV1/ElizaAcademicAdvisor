#Program Name: AcaDemic Advisor (ADA)
#Author: Victor LaBrie
#Date: September 22, 2022
#THE PROBLEM/GOAL:
#The goal of this program is to try to imitate an academic advisor in the same
#way that ELIZA imitated a Georgian psychologist. That is to say, we don't want 
#necessarily to say anything helpful, but we want to be able to take what is said and
#use it in a way to keep the user engaged in a way that it might feel like talking to someone. 
#EXAMPLE USAGE:
#THE ALGORITHM:
#1) The program starts by introducing itself and asking for the user's first name.
#   From there it will not proceed until it has a name.
#2) The program enters the main loop of the program that continues until the user
#   types "exit".
#3) The program will look for certain sentence structures and keywords. Depending
#   on what get's matched, the program will respond accordingly. Some responses will use
#   "memorized" information, so certain keywords and patterns will cause the program to 
#   ask for that information and won't allow the user to continue until it's entered.
#   
#EXAMPLE:
# < I want to learn more about graduation requirements.
# > What year are you?
# < 4th.
# > So you're a senior. How many credits do you have?
# < Koalas.
# > I didn't quite catch that. How many credits do you have?
# < About 110.
# > More than halfway there. How about your GPA?
# < It's about 3.338.
# > That's above average. What else would you like to know about graduation.
#Sidenote: This could have been a lot shorter if I used functions. Several things are repeated.
#If I wrote anotherEliza-like chatbot might have certain functions assosciated with different keywords.
#2nd Sidenote: Some responses aren't meant to be taken seriously.
from random import randint
import re


#Rank system used in Eliza implemented by order of elifs. The highest ranked ones are those that will involve
#values that will be saved.
#System will assume input is in complete and grammatically correct sentences.
#Placed inside a function to allow for returning whenever an exit is encountered.
def advisorFunc():
    #These are things that the program should "remember" if they're brought up.
    studentName = None
    studentGrade = None
    studentMajor = None
    studentCredits = None
    studentGPA = None

    #To avoid loops, this program will just use some booleans to track if a topic
    #has already been visited. Some topics won't need this, such as GPA and Major,
    #as those will already be recorded in the above variables.
    graduationVisited = False


    #First the adivsor will ask basic questions that can be used later
    print("> Hello, I am Ada, your acadmic advisor. What's your first name?")
    #loop to get name
    while studentName == None:
        inputString = input("< ")
        if re.match(r"exit$", inputString):
            return
        #Use capture groups to get name.
        #Regex explanation: User will probably say something like "I am" or "My name is" before their name, but they also might not,
        #so the only thing that needs to be in a capture group is the Name at the end.
        if re.search(r"(?:(?:My name(?:'| i)s )|(?:I(?:'| a)m ))?([A-Z][a-z|'-]+)\.", inputString):
            thisMatch = re.search(r"(?:(?:My name(?:'| i)s )|(?:I(?:'| a)m ))?([A-Z][a-z|'-]+)\.", inputString)
            studentName = thisMatch.group(1)
            print("> What can I do for you", studentName + "?")
        else:
            print("> I didn't catch that. Tell me again, using proper grammar.")
    while True:
        #Responses will always start with ">".
        outputString = "> "
        #User input will always be prompted by "<"."
        inputString = input("< ")
        #Match function means it looks at beginning of sentence, so no need for start of sentence operator. Will match
        #only if "exit" is typed by itself.
        if re.match(r"exit$", inputString):
            return
        #One of the higher priority patterns to look for are those regarding abusive language. I will only demonstrate this with one of the
        #more mild ones, simply becuase there are just too many abusive words for the scope of this project.
        elif re.search(r"(?: |^)[Hh][Ee3][Ll1\|]{2}(?: |$|\.|\!)",inputString):
            outputString += "I won't tolerate that manner of unprofessional language in my office. Get the hell out of here."
            print(outputString)
            #If any variation of "hell" is returned (but not "hello" or "shell", or other words containing "hell"), the user will be kicked out for abusive language.
            return
        #Regex explanation: If credits are mentioned, the program will prompt the use to tell it how many credits they have.
        elif re.search(r"[Cc]redits", inputString):    
            while studentCredits == None:
                    outputString += "How many credits do you have?"
                    print(outputString)
                    outputString = "> "
                    inputString = input("< ")
                    if re.match(r"exit$", inputString):
                        return
                    #Regex explanation: Get number of credits from response. Will be between 0 and 999.
                    thisMatch = re.search(r"(?:.* |^)([0-9]{1,3}).*",inputString)
                    if thisMatch:
                        studentCredits = int(thisMatch.group(1))
                        if studentCredits < 60:
                            outputString += "You're not quite halfway there. "
                        else:
                            outputString += "You're more than halfway there. "
                    else:
                        outputString += "Didn't catch that. "
            outputString += "What else would you like to know about credits."
        #If input contains gpa, GPA, or Gpa:
        elif re.search(r"[Gg](?:PA|pa)", inputString):
            while studentGPA == None:
                outputString += "Ok, what's your GPA?"
                print(outputString)
                outputString = "> "
                inputString = input("< ")
                if re.match(r"exit$", inputString):
                    return
                #Regex explanation: GPA should be a number between 0 and 5 followed by up to 3 decimals. The .* at the end allows for other words but doesn't capture them.
                thisMatch = re.search(r"([0-5]{1}\.[0-9]{1,3}).*", inputString)
                if thisMatch:
                    studentGPA = float(thisMatch.group(1))
                    if studentGPA < 2.0:
                        outputString += "Your GPA is currently below average. "
                    else:
                        outputString += "Your GPA is currently above average. "
                else:
                    outputString += "Sorry, I'm hard of hearing."
            outputString += "Is there anything else about your GPA you want to talk about?"
        if re.search(r"(?:[Yy]ear|[Gg]rade)", inputString):    
            while studentGrade == None:
                    thisMatch = None
                    outputString += "What year are you?"
                    print(outputString)
                    outputString = "> "
                    inputString = input("< ")
                    if re.match(r"exit$", inputString):
                        return
                    #Regex explanation: Will capture any variation of grade/year that I could think of when I wrote this.
                    thisMatch = re.search(r"([Ff]irst|[Ss]econd|[Tt]hird|[Ff]ourth|[Ff]ifth|[Ss]ixth|1st|2nd|3rd|[456]th|[Ff]reshman|[Ss]ophomore|[Jj]unior|[Ss]enior)", inputString)
                    if thisMatch:
                        matchedGrade = thisMatch.group(1).lower()
                        if matchedGrade in ["first", "1st", "freshman"]:
                            studentGrade = "freshman"
                        elif matchedGrade in ["second", "2nd", "sophomore"]:
                            studentGrade = "sophomore"
                        elif matchedGrade in ["third", "3rd", "junior"]:
                            studentGrade = "junior"
                        elif matchedGrade in ["fourth", "fifth", "sixth", "4th", "5th", "6th", "senior"]:
                            studentGrade = "senior"
                        outputString += ("So you're a " + studentGrade + ". ")
                    else:
                        outputString += "I didn't quite get that. "
                    outputString += "What else would you like to know about your year?"
        #Regex explanation: If input contains keyword "major" or "Major".
        elif re.search(r"[Mm]ajor", inputString):
            #If major hasn't been discussed before, ADA will ask about the major in a loop until a valid input is received.
            while studentMajor == None:
                print("> Before we talk about your major, tell me what you're majoring in.")
                inputString = input("< ")
                if re.match(r"exit$", inputString):
                    return
                #Regex explanation: Captures major. Major itself is the only thing being captured here. Usually will 
                thisMatch = re.search(r"(?:(?:My major is )|(?:I'm majoring in )|(?:It's ))?([A-Za-z][a-z]* ?[A-Za-z][a-z]+(?:'s)? ?[A-Za-z]*)\.", inputString)
                if thisMatch:
                    studentMajor = thisMatch.group(1).lower()
            #After major is recorded, program will ask general question about major.
            outputString += "What would you like to know about "+ studentMajor +", " + studentName + "?"
        #Regex explanation: If the user mentions graduation, graduate, or graduating.
        elif re.search(r"[Gg]raduat(?:e|ion|ing)", inputString):
            #If relevant info not already known, Ada will ask
            #If student year not known:
            while studentGrade == None:
                thisMatch = None
                outputString += "What year are you?"
                print(outputString)
                outputString = "> "
                inputString = input("< ")
                if re.match(r"exit$", inputString):
                    return
                #Regex explanation: Will capture any variation of grade/year that I could think of when I wrote this.
                thisMatch = re.search(r"([Ff]irst|[Ss]econd|[Tt]hird|[Ff]ourth|[Ff]ifth|[Ss]ixth|1st|2nd|3rd|[456]th|[Ff]reshman|[Ss]ophomore|[Jj]unior|[Ss]enior)", inputString)
                if thisMatch:
                    matchedGrade = thisMatch.group(1).lower()
                    if matchedGrade in ["first", "1st", "freshman"]:
                        studentGrade = "freshman"
                    elif matchedGrade in ["second", "2nd", "sophomore"]:
                        studentGrade = "sophomore"
                    elif matchedGrade in ["third", "3rd", "junior"]:
                        studentGrade = "junior"
                    elif matchedGrade in ["fourth", "fifth", "sixth", "4th", "5th", "6th", "senior"]:
                        studentGrade = "senior"
                    outputString += ("So you're a " + studentGrade + ". ")
                else:
                    outputString += "I didn't quite get that. "
            #If student number of credits not known:
            while studentCredits == None:
                outputString += "How many credits do you have?"
                print(outputString)
                outputString = "> "
                inputString = input("< ")
                if re.match(r"exit$", inputString):
                    return
                #Regex explanation: Get number of credits from response. Will be between 0 and 999.
                thisMatch = re.search(r"(?:.* |^)([0-9]{1,3}).*",inputString)
                if thisMatch:
                    studentCredits = int(thisMatch.group(1))
                    if studentCredits < 60:
                        outputString += "You're not quite halfway there. "
                    else:
                        outputString += "You're more than halfway there. "
                else:
                    outputString += "Didn't catch that. "
            #If GPA not known
            while studentGPA == None:
                outputString += "Ok, what's your GPA?"
                print(outputString)
                outputString = "> "
                inputString = input("< ")
                if re.match(r"exit$", inputString):
                    return
                #Regex explanation: GPA again, same as above. This is why I should have used functions.
                thisMatch = re.search(r"([0-9]{1}\.[0-9]{1,3}).*", inputString)
                if thisMatch:
                    studentGPA = float(thisMatch.group(1))
                    if studentGPA < 2.0:
                        outputString += "Your GPA is currently below average. "
                    else:
                        outputString += "Your GPA is currently above average. "
                else:
                    outputString += "Say that again. "
            if graduationVisited:
                outputString += "What else would you like to know about graduating?"
            else:
                outputString += "What would you like to know about graduation?"
                graduationVisited = True
        #The rest of these responses are more basic and only seek to continue the conversation.
        #Regex explanation: If the user says something about their x, the program will substitute out everything 
        #before the object of the sentence with "what about your".
        elif re.search(r".* ?[Mm]y [A-Za-z]* ?\.$", inputString):
            outputString += re.sub(r".* ?[Mm]y", r"What about your", inputString)[:-1] + "?"
        #Response to user asking for Ada to do something.
        #Regex explanation: Variations on question regarding the ability of the program to do something.
        elif re.search(r"(?:Can|Would|May|Will|Might|Could) you .*\?", inputString):
            outputString += ("I'm sorry " + studentName + ", I'm afraid I can't do that.")
        #To some questions, a user might respond simply "yes" or "no", or some variation of those.
        #Regex explanation: Probably overly complicated way of saying many forms of yes or no that aren't part of another word.
        elif re.search(r"(?:(?:(?:N|(?: |^)n)(?:egative|o|ah))|(?:(?:Y|(?: |^)y)(?:es|uh|ah|eh?|essir)))", inputString):
            responseList = ["Uh-huh. ", "Ah. ", "I see. ", "Gotcha. "]
            secondResponseList = ["Is there anything else?", "What else did you want to ask?", "How are the wife and kids?"]
            outputString += (responseList[randint(0,len(responseList)-1)] + secondResponseList[randint(0,len(secondResponseList)-1)])
        #If user wants to aks something. Generic question and response.
        elif re.search(r"(?:Can|May) I ask(?: you)? (?:something(?: else)?|a(?:nother)? question)\?", inputString):
            #responses shouldn't always be the same, which can be handled by having a list of responses and randomly choosing
            responseList = ["What do you need help with?", "Ask away.", "Go ahead."]
            outputString += responseList[randint(0,len(responseList)-1)]
        #If no pattern or keyword is found, program will respond randomly from list of responses. Depending
        #on what was already discussed, Ada will bring up other topics.
        else:
            responseList = ["I didn't catch that.", "Say that again.", "Slow down there.", "Uh, what?", "I don't understand."]
            if studentGrade != None:
                responseList.append("Let's change the topic. Do you have any questions about being a " + studentGrade + "?")
            if studentMajor != None:
                responseList.append("I'm not sure what you're getting at, so let's change the topic. Do you have any questions about " + studentMajor + "?")
            if studentGPA != None:
               responseList.append("What? Whatever. Changing the subject here, but are you satisfied with a " + str(studentGPA) + " GPA?")
            outputString += responseList[randint(0,len(responseList)-1)]
        print(outputString)
advisorFunc()