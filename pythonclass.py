# n = int(input("enter number :"))
# d = int(input("enter number d:"))
# print(n - d)
# print("Lets {0} {3} {4} {1} {2}".format("go","outside","together","and","play"))
# x = open('myfile.txt', 'w')
# x.write('This is my file that I opened')
# x.close()
#
# def myfunc():
#     print('All of the galaxy.')
#
# This = ("Target, Macy's, Justice")
# print(This)
#
# print("This is how you type and or print")
#
# USA = "The whole country"
# print(USA [9:17])
#
#
# print("practice on hacker rank alsmost every day.")
#
#
# #Undestanding the functions
# def printName(fname, lname="N/A"):
#     print(f'First: {fname}, Last: {lname}')
#
#
#     printName("abc", "123")
#     printName(lname="123", fname="abc")
#     printName("abc")

#def printFruitsList(fruits):
#    fruits.add("new Fruit")
#print(fruits)

#def printFruitsTuple(*fruits):
#     print(fruits)

#def printAllNames(**names):
#     print(f"First: {names['first']}, Middle: {names['middle']}, Last: {names['last']}")

#def printAllNamesDict(names):
#     print(f"First: {names['first']}, Middle: {names['middle']}, Last: {names['last']}")
#printFruitsTuple("apple", "banana")
#printFruitsList({"apple", "banana"})
#printAllNames(first="Chaitra", last="Surapaneni", middle="S")
#printAllNamesDict({"first": "Chaitra", "last": "Surapaneni", "middle": "S"})



#def runnerUp(myArr):
#     newList = []
#
#     while myArr:
#         highest = myArr[0]
#         for x in myArr:
#             if x > highest:
#                 highest = x
#
#         if highest not in newList:
#             newList.append(highest)
#         myArr.remove(highest)
#
#     if len(newList) >= 2:
#         return newList[1]
#     else:
#         return newList[0]
#
#
# if __name__ == '__main__':
#     n = int(input("How many Numbers?: "))
#     arr = list(map(int, input("Enter numbers: ").split()))
#  x = runnerUp(arr)
# print(f"Runner up score is : {runnerUp(arr)}")


#def bubbleSortAlgorthim(bubble):
#    n = len(bubble)

#    for x in range(n - 1):

#        for j in range (0, n - x - 1):

#            if bubble[j] > bubble[j + 1]:
#                bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

#bubble = list(map(int, input("Enter your number: ").split()))

#bubbleSortAlgorthim(bubble)
#print(f"sorted list is {bubble}")

# def parseLine(line):
#     pairs = line.split(", ")
#     myDictionary = {}
#     for pair in pairs:
#         (key,value) = pair.split(" = ")
#         myDictionary[key] = value
#
#     return myDictionary
#
# myList = []
# myFile = open("testData.txt.py","r")
# lines = myFile.readlines()
#
# for line in lines:
#     parseLine(line)
#
#print(myList)

# division hackerank
# a = int(input("Enter Number a:"))
# b = int(input("Enter Number b: "))
# print(a//b)
# print(a/b)

# def squareOf(num):
#     return num * num
#
# n = int(input())
# list1 = list(range(n))
# list2 = list(map(squareOf, list1))
#
# print(list1)
# print(list2)

# myList = []
# if __name__ == '__main__':
#     for _ in range(int(input("How many: "))):
#         name = str(input("Name(s): "))
#         score = float(input("Scores(s): "))
#         studentInfo = [name, score]
#         myList.append(studentInfo)
#
# scoreList = []
#
# for newList in myList:
#     if (scoreList.count(newList[1])) == 0:
#         scoreList.append(newList[1])
#
#
# scoreLength = len(scoreList)
# if scoreLength >= 1:
#     secondScore = scoreList[1]
# else:
#     secondScore = scoreList[0]
#
# nameList = []
# for student in myList:
#     if student[1] == secondScore:
#         nameList.append(student[0])
#
# nameList.sort()
#
# for name in nameList:
#     print(name)


# def count_substring(string, sub_string):
#     lN = len(string)
#     l2 = len(sub_string)
#     counts = 0
#     for idx in range(lN - l2 + 1):
#         if string[idx: idx+l2] == sub_string:
#             counts = counts + 1
#     return counts
print("new line")
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)



