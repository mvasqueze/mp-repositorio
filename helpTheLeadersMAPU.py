import copy

#The program in this moment returns all the combinations without any of the prohibited combinations
#so if in the prohibited combinations we have 'WAR PEACE', none of the combinations will have
#peace or war in them...


#Function to declare the arrays of topics and the array of the prohibited combinations
#In here I also sort the array of topics so it is in lexicographical(a-z) and length(larger-smaller) order
#Plus, I created an array that has arrays, the same amount of topics as there are, and in each
#array will be stored the position of the words it can't be combined with, meaning, if we have 4 topics
#and topic 0 can't be with topic 3, the array will look like this: [[3],[],[0],[]]
def organizeInput(amountTopics, prohibitedCombinations, topics, prohibited, listaTuplas):
        #All posible topics saved in topics[]
        for i in range(0, amountTopics):
            topics[i] = input().upper()
            
        #All prohibited combinations saved in prohibitedCombinations[]
        for i in range(0, prohibitedCombinations):
            prohibited[i] = input().upper()

        prohibited.sort()
        prohibited.sort(key = len, reverse = True)
        #Organize topics array in lexicographical and length order
        topics.sort()
        topics.sort(key = len, reverse =True)

        #Prohibited words saved in prohWords[]
        for i in range (0, len(prohibited)):
            topic1, topic2 = prohibited[i].split()
            index1 = topics.index(topic1)
            index2 = topics.index(topic2)
            tuplaProh=(index1, index2)
            listaTuplas.append(tuplaProh)
            #prohWords[index1].append(index2) 
            #prohWords[index2].append(index1)
            '''Qué tal si se guardan ambas palabras juntas ordenadas en orden lexicográfico, p.ej.
            una lista de tuplas'''
        #print("lista de tuplas: ", listaTuplas)

#Function to create the combinations of the topics according to the quantity specified
def combinations(topics, topicsPerTalk, listaTuplas, topicsForCombs, index):
    allCombs = []
    topicsForCombs = topics.copy()
    #tmp = [None]*topicsPerTalk
    #length = len(topics)
    if topicsPerTalk==1:
        #If there is just one topic per speech, then we shall print all the topics provided but the prohibited ones
        allCombs=topics
        return allCombs
    if topicsPerTalk==2:
        '''This is the base of the recursion: When you need to do just 2-tuples the key is to take the
        longest word (in lexicographical order) and concatenate it with the rest other words, then you take
        the second longest word and concatenate it with the rest of the words and so on. '''
        for i in range (index, len(topics)):
            for j in topicsForCombs[i+1:]:
                pos = []
                pos.append(topics.index(j))
                auxVar=[i, topics.index(j)]
                if(checkCombinations(listaTuplas, i,auxVar)):
                    allCombs.append(topics[i]+' '+j)
                else:
                    continue

    if topicsPerTalk>2:
        '''This is when the recursion happens: This part of the method takes the longest word in lexicographical
        order and concatenates it with the n-1 tuples previously generated.'''
        output=allCombs.copy()
        allCombs.clear()
        for i in range (index, len(topics)):
            index = i+1
            previousTuples=combinations(topics, topicsPerTalk-1, listaTuplas, topicsForCombs[i+1:], index)
            
            for j in previousTuples:
                listaAux=[]
                listWords = j.split(" ")
                pos = []
                listaAux.append(i)
                for h in listWords:
                    listaAux.append(topics.index(h))
                
                if(checkCombinations(listaTuplas, i,listaAux)):
                    output.append(topics[i]+' '+j)
                else:
                    continue
        allCombs=output.copy()
    
    return allCombs
 
#Function to check if the words with which I'm making the combinatios are prohibited among them, if so
#return False, and if not returns True

## [[1],[0],[],[7],[],[],[],[3]]

def printer(setInfo):
    for i in setInfo:
        print(i)
    setInfo.clear()
    print()


def checkCombinations(listaTuplas, firstWord, listAux):
    flag = True
    for t in listaTuplas: # [(7,0), (4,3), (1,2)]
        if (t[0] in listAux and t[1] in listAux):
            flag = False
            return flag
        else:
            flag = True
    
    return flag
    

def main():
    setInfo = []
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
        topics = [ [] for _ in range(amountTopics)]
        prohibited = [ [] for _ in range(prohibitedCombinations)]
        listaTuplas = []
        topicsForCombs = []

        #Call the function to organize the information provided
        organizeInput(amountTopics, prohibitedCombinations, topics, prohibited, listaTuplas)

        #Call combinations function
        index = 0
        allCombs = combinations(topics, topicsPerTalk, listaTuplas, topicsForCombs, index)
        setInfo.append("Set %d:" %(i+1))
        for j in allCombs:
            setInfo.append(j)
        setInfo.append('')
    printer(setInfo)
    print()


main()
