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



#Function to create the combinations of the topics according to the quantity specified
def combinations(topics, topicsPerTalk, prohWords):
    allCombs = []
    tmp = [None]*topicsPerTalk
    length = len(topics)
    def next_num(li=0, pos=0):
        if pos == topicsPerTalk:
            allCombs.append(copy.copy(tmp))
            return

        for pos2 in range(li,length):
            #Calls the function checkCombinations to check if the combination with such words can be done
            #If the combination can't be done we enter to this if and we continue the combinations without
            #considering the prohibited.
            if(not checkCombinations(prohWords, pos, pos2)):
                tmp[pos] = topics[pos2]
                next_num(pos2+1, pos+1)
            #If the combination can be done we just continue with the function
            else:
                next_num(pos2+1, pos)
    next_num()

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
    for i in range(0, numberOfSets): 
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
