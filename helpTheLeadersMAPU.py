import copy

#The program in this moment returns all the combinations without any of the prohibited combinations
#so if in the prohibited combinations we have 'WAR PEACE', none of the combinations will have
#peace or war in them...


#Function to declare the arrays of topics and the array of the prohibited combinations
#In here I also sort the array of topics so it is in lexicographical(a-z) and length(larger-smaller) order
#Plus, I created an array that has arrays, the same amount of topics as there are, and in each
#array will be stored the position of the words it can't be combined with, meaning, if we have 4 topics
#and topic 0 can't be with topic 3, the array will look like this: [[3],[],[0],[]]
def organizeInput(amountTopics, prohibitedCombinations, topics, prohibited, prohWords):
        #All posible topics saved in topics[]
        for i in range(0, amountTopics):
            topics[i] = input()
        
        #All prohibited combinations saved in prohibitedCombinations[]
        for i in range(0, prohibitedCombinations):
            prohibited[i] = input()

        #Organize topics array in lexicographical and length order
        topics.sort()
        topics.sort(key = len, reverse =True)

        #Prohibited words saved in prohWords[]
        for i in range (0, len(prohibited)):
            topic1, topic2 = prohibited[i].split()
            
            index1 = topics.index(topic1)
            index2 = topics.index(topic2)
            prohWords[index1].append(index2) 
            prohWords[index2].append(index1)
            '''Qué tal si se guardan ambas palabras juntas ordenadas en orden lexicográfico, p.ej.
            una lista de tuplas'''



#Function to create the combinations of the topics according to the quantity specified
def combinations(topics, topicsPerTalk, prohWords):
    allCombs = []
    #tmp = [None]*topicsPerTalk
    #length = len(topics)
    if topicsPerTalk==1:
        allCombs=topics
        return allCombs
    if topicsPerTalk==2:
        for i in topics:
            firstWord=topics.pop(0)
            for j in topics:
                allCombs.append(firstWord+' '+j)
    if topicsPerTalk>2:
        output=allCombs.copy()
        allCombs.clear()
        for i in topics:
            firstWord=topics.pop(0)
            previousTuples=combinations(topics, topicsPerTalk-1, prohWords)
            for j in previousTuples:
                output.append(firstWord+' '+j)
        allCombs=output.copy()
    return allCombs
 
#Function to check if the words with which I'm making the combinatios are prohibited among them, if so
#return False, and if not returns True
def checkCombinations(prohWords, pos, pos2):
    for i in range(0,len(prohWords[pos2])):
        if(prohWords[pos2][i] == pos):
            return False
        return True

def main():
    numberOfSets = int(input())
    for i in range(0, numberOfSets):
        #Read all the line of the info (amount of topics, amount of prohibited combinations & quantity of topics per combination)
        infoSets = input()
        #Divide all the info into the variables
        x = 0
        amount = ""
        while x < len(infoSets) and infoSets[x] != " ":
            amount += infoSets[x]
            x += 1
        x += 1
        amountTopics = int(amount)
        amount = ""
        while x < len(infoSets) and infoSets[x] != " ":
            amount += infoSets[x]
            x += 1
        x += 1
        prohibitedCombinations = int(amount)

        amount = ""
        while x < len(infoSets) and infoSets[x] != " ":
            amount += infoSets[x]
            x += 1
        x += 1
        topicsPerTalk = int(amount)

        #Initialize the arrays of topics & prohibited combinations
        topics = [None] * amountTopics
        prohibited = [None] * prohibitedCombinations
        prohWords = [ [] for _ in range(amountTopics)]

        #Call the function to organize the information provided
        organizeInput(amountTopics, prohibitedCombinations, topics, prohibited, prohWords)
        
        #Cycle to do the combinations to each set
        #for i in range(0, numberOfSets): 
        #Call combinations function
        allCombs = combinations(topics, topicsPerTalk, prohWords)
        print("Set:", i+1)
        #Print the combinations of each set
        for j in allCombs:
            for h in j:
                print(h, end = " ")
            print()
        print()

main()
