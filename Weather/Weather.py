countOfTenLess = 0

# startDate, finalDate = input(), input()
# idStart = startDate.split('.')
# idStart = int(idStart[0]) + int(idStart[1] * 31)
# idFinal = finalDate.split('.')
# idFinal = int(idFinal[0]) + int(idFinal[1] * 31)

maxTemperature = [str(), int()]
minTemperature = [str(), int()]

averageTemp = dict()

print('asd')
with open("weather.txt") as file:
    lineTuple = file.readline().split()
    minTemperature[0], maxTemperature[0] = lineTuple[0] + " ", lineTuple[0] + " "
    maxTemperature[1] = int(lineTuple[1])
    minTemperature[1] = int(lineTuple[1])

    for line in file:
        lineTuple = tuple(line.split())
        dayTemp = int(lineTuple[1])
        date = lineTuple[0]
        
        if dayTemp < -10:
            countOfTenLess += 1

        if dayTemp < minTemperature[1]:
            minTemperature[1] = dayTemp
            minTemperature[0] = date + " "
        elif dayTemp == minTemperature[1]:
            minTemperature[0] += date + " "

        if dayTemp > maxTemperature[1]:
            maxTemperature[1] = dayTemp
            maxTemperature[0] = date + " "
        elif dayTemp == minTemperature[1]:
            maxTemperature[0] += date + " "

        month = date[-2:]
        if month in averageTemp:
            averageTemp[month][0] += dayTemp
            averageTemp[month][1] += 1
        else:
            averageTemp[month] = [dayTemp, 1]

        
        

print(countOfTenLess)

print(maxTemperature)
print(minTemperature)

for key in averageTemp:
    print("Month:", key, "average:", averageTemp[key][0] / averageTemp[key][1])
