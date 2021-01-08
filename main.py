fileOfCensus = open("Perepis.txt", "r")

minYear, maxYear = int(input()), int(input())

countOf1978 = 0

for line in fileOfCensus:
    tupleOfLine = tuple(line.split())
    dateTuple = tuple(tupleOfLine[3].split('.'))
    if int(dateTuple[2]) < 1978:
        print(tupleOfLine[0])
        countOf1978 += 1

print(countOf1978)

fileOfCensus2 = open("Perepis.txt", "r")

for line in fileOfCensus2:
    year = line.split()[3].split('.')[2]
    if (minYear < int(year) < maxYear ):
        print(line, end="")
