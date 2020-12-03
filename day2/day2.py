f = open("day2/input.txt", "r")

#Part 1
def PartOne():
    validPasswords = 0
    for line in f:
        strList = line.split(" ")
        passRange= strList[0].split("-")
        passChar = strList[1][0]
        password = strList[2]
        count = password.count(passChar)
        if count >= int(passRange[0]) and count <= int(passRange[1]):
            validPasswords = validPasswords + 1
    f.seek(0)
    return validPasswords

print(PartOne())

#Part 2
def PartTwo():
    validPasswords = 0
    for line in f:
        strList = line.split(" ")
        passPositions= strList[0].split("-")
        passChar = strList[1][0]
        password = strList[2]
        if (password[int(passPositions[0]) - 1] == passChar) != (password[int(passPositions[1]) - 1] == passChar):
            validPasswords = validPasswords + 1
    f.seek(0)
    return validPasswords

print(PartTwo())