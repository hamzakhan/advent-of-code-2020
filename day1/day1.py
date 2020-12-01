f = open("input.txt", "r")

#Part 1
Dict = {}
def PartOne():
    for line in f:
        val = int(line)
        if val in Dict:
            return Dict[val] * val        
        else:
            Dict[2020-val] = val
print(PartOne())

#Part 2
DictPart2 = {}
def PartTwo(): 
    for key in Dict:
        for line in f:
            val = int(line)
            if val in DictPart2:
                return DictPart2[val] * val * Dict[key]
            elif val < key:
                DictPart2[key-val] = val
        f.seek(0)
print(PartTwo())