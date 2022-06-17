def runLengthEncoding(string):
    counter = 1
    result = ""

    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            counter += 1
        else:
            if counter > 0:
                result += str(counter) + string[i-1]
            counter = 1

        if counter == 9:
            result += "9" + string[i]
            counter = 0
    result += str(counter) + string[len(string)-1]
    return result


string = "........______=========AAAA   AAABBBB   BBB"

print(runLengthEncoding(string))


# "8.6_9=4A3 3A4B3 3B"