#Khushmeet Chandi
#Artificial Intelligence Period 4
#Objective: Create a graph from inputted words where the words are neighbors if
# they have a single letter character difference in exactly the same position. 
# The graph is then used to produce statistics, such as find the number of connected components, 
# and perform tasks, such as find the shortest path between two words. 

import sys
import time
import math
def buildGraph(fileName):
    startTime=time.time()
    d = {}
    wordList = open(fileName, "r").read().splitlines() 
    graph = {k: [] for k in wordList} #Graph 
    degreeList = [0 for k in range(len(wordList)//200)]
    for word in wordList:
        for i in range(len(word)):     
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    maxLength=0
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2: graph[word1].append(word2) 
        if len(graph[word1])>maxLength: maxLength=len(graph[word1])
    degreeList = [str(sum(1 for k in graph if len(graph[k])==n)) for n in range(maxLength+1)]
    print("Word count: {}".format(len(wordList))) #1
    print("Edge count: {}".format(sum([len(graph[key]) for key in graph])//2)) #2 
    print("Degree List: " +  " ".join(degreeList))
    print("Construction time: {}s".format(round(time.time()-startTime, -int(math.log10(time.time()-startTime)//1)+(2))))
def createGraph(fileName):
    startTime=time.time()
    wordList = open(fileName, "r").read().splitlines() #Reads the file and puts it into a list
    maxLength = 0 #Stores the highest degree
    degreeList = [0]*(len(wordList)//250) #The degree distribution list
    graph = {wordList[0]:[]}
    singleDegree = [] #All the words of degree 1
    doubleDegree = [] #All the words of degree 3
    thirdDegree = [] #All the words of degree 3
    setWordList = set(wordList) #A set of all the words
    setCompoCount = set()
    #Creates the graph
    for n in range(len(wordList)):
        word1 = wordList[n]
        for word2 in wordList[n+1:]:
            if n==0: graph[word2] = []
            if neighbor(word1, word2):
                graph[word1].append(word2)
                graph[word2].append(word1)
        length = len(graph[word1])
        if length > maxLength: maxLength = length
        if length==1: singleDegree.append(word1)
        elif length==2: doubleDegree.append(word1)
        elif length==3: thirdDegree.append(word1) 
        degreeList[length]+=1
    degreeList = degreeList[0:maxLength+1]
    for k in graph:
        if len(graph[k])==maxLength-1:
            print("Second degree word: {}".format(k))
            break
    #Finding K2 count
    k2count = sum(1 for n in singleDegree if len(graph[graph[n][0]])==1 and graph[(graph[n])[0]][0] == n)
    #Finding K3 count
    k3count = 0
    for n in doubleDegree:
        if len(graph[graph[n][0]])==2 and len(graph[graph[n][1]])==2: 
            one1 = graph[n][0]
            two1 = graph[n][1]
            one = graph[graph[n][0]]
            two = graph[graph[n][1]]
            if (one[0]==n or one[1]==n) and (one[0]==two1 or one[1]==two1) and (two[0]==n or two[1]==n) and (two[0] == one1 or two[1] == one1) and ((graph[n][0]==one1 and graph[n][1]==two1) or (graph[n][0]==two1 and graph[n][1]==one1)): k3count+=1
    #Finding K4 count
    k4count = 0
    for n in thirdDegree:
        if len(graph[graph[n][0]])==3 and len(graph[graph[n][1]])==3: 
            one1 = (graph[n])[0]
            two1 = (graph[n])[1]
            three1 = (graph[n])[2]
            one = graph[(graph[n])[0]]
            two = graph[(graph[n])[1]]
            three = graph[(graph[n])[2]]
            if (one[0]==two1 or one[1]==two1 or one[2]==two1) and (one[0]==three1 or one[1]==three1 or one[2]==three1) and (one[0]==n or one[1]==n or one[2]==n) and (two[0] == n or two[1] == n or two[2]==n) and (two[0] == three1 or two[1] == three1 or two[2]==three1) and (two[0] == one1 or two[1] == one1 or two[2]==one1) and (graph[n][0]==one1 or graph[n][1]==one1 or graph[n][2]==one1) and (graph[n][0]==two1 or graph[n][1]==two1 or graph[n][2]==two1) and (graph[n][0]==three1 or graph[n][1]==three1 or graph[n][2]==three1) and (three[0]==one1 or three[1]==one1 or three[2]==one1) and (three[0]==n or three[1]==n or three[2]==n) and (three[0]==two1 or three[1]==two1 or three[2]==two1): k4count+=1
    #Finding the connected component sizes
    maxC = 0
    for word in wordList:
        if word in setWordList:
            count=0
            parseMe = [word]
            while parseMe:
                start = parseMe.pop()
                for n in graph[start]:
                    if n in setWordList:
                        count+=1
                        parseMe.append(n)
                        setWordList.remove(n)
            if count>maxC: maxC=count
            setCompoCount.add(count)
    #Printing Statistics
    print("Connected component size count: " + str(len(setCompoCount)))
    print("Largest component size: " + str(maxC))
    print("K2 count: "+str(k2count//2))
    print("K3 count: "+str(k3count//3))
    print("K4 count: "+str(k4count//4))
    print("Neighbors: "+(", ".join(graph[sys.argv[2]]))) 
    print("Farthest: "+findPath(graph, sys.argv[2], " ", 2))
    print("Path: "+findPath(graph, sys.argv[2], sys.argv[3], 0))
    print("Construction time: {0:.1f}s".format(time.time()-startTime))
def neighbor(word1, word2):
    if word1[1:] == word2[1:]: return True
    elif word1[:1] + word1[2:] == word2[:1] + word2[2:]: return True
    elif word1[:2] + word1[3:] == word2[:2] + word2[3:]: return True
    elif word1[:3] + word1[4:] == word2[:3] + word2[4:]: return True
    elif word1[:4] + word1[5:]== word2[:4]+ word2[5:]: return True
    elif word1[:5] == word2[:5]: return True
    return False
def findPath(graph, start, goal, check):
    parseMe = [start]
    dictSeen = {start: " "}
    while parseMe:
        start = parseMe.pop(0)
        for n in graph[start]:
            if n==goal:
                dictSeen[n] = start
                return ", ".join(printPath(dictSeen, goal))
            else:
                if n not in dictSeen:
                    dictSeen[n] = start
                    parseMe.append(n)
                if not parseMe and check==2: return start
    return start
def printPath(dictSeen, goal):
    myList = [goal]
    while dictSeen[goal]!=" ":
        goal = dictSeen[goal]
        myList.append(goal)
    return myList[::-1]
if len(sys.argv)<3:
    buildGraph(sys.argv[1])
else:
    createGraph(sys.argv[1])