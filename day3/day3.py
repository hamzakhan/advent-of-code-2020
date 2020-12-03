f = open("day3/input.txt", "r")

trimmedLine = "".join(f.readline().split())
lineLength = len(trimmedLine)
f.seek(0)

#Part 1
def PartOne(rightShift = 3, downShift = 1):
    index = 0
    trees = 0
    skipLine = False
    dShift = downShift

    for line in f:
        if skipLine:
            dShift = dShift - 1
            if dShift == 0:
                skipLine = False
                dShift = downShift
            continue

        if line[index] == '#':
            trees = trees + 1
        index = index + rightShift
        if index > lineLength - 1:
            index = index - lineLength

        if downShift > 1:
            dShift = dShift - 1
            skipLine = True

    f.seek(0)
    return trees

print(PartOne())

#Part 2
def PartTwo():
    return PartOne(1,1) * PartOne(3,1) * PartOne(5,1) * PartOne(7,1) * PartOne(1,2)

print(PartTwo())