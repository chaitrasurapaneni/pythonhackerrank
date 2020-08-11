def parseLine(line):
    pairs = line.split(", ")
    myDictionary = {}
    for pair in pairs:
        (key, value) = pair.split("=")
        myDictionary[key] = value

    return myDictionary


myList = []
myFile = open("testData.txt", "r")
lines = myFile.readlines()


for line in lines:
    myLine = line.replace("\n", "")
    myList.append(parseLine(myLine))

for x in myList:
    print(x)

#print(myList)

