if __name__ == '__main__':
    n = int(input())
    dataList = []
    # insert 0 6
    for x in range(n):
        commandList = input().split(" ")
        command = commandList[0]
        if (command == 'insert'):
            index = int(commandList[1])
            value = int(commandList[2])
            dataList.insert(index, value)

        if (command == 'print'):
            print(dataList)

        if (command == 'remove'):
            value = int(commandList[1])
            dataList.remove(value)

        if (command == 'append'):
            index = int(commandList[1])
            dataList.append(index)

        if (command == 'sort'):
            value = (commandList[-1])
            dataList.sort()

        if (command == 'pop'):
            value = (commandList[-1])
            dataList.pop()

        if (command == 'reverse'):
            value = (commandList[0])
            dataList.reverse()
