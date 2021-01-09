file = open("travels.txt")

days = {1 : 0,
        2 : 0,
        3 : 0}

massOfLipki = 0
sumOfDistance = 0
pointsOfDeparture = dict()
destinations = dict()
dictOfMaxBenzineAverage = dict()

for line in file:
    lineTuple = tuple(line.split())
    days[int(lineTuple[0])] += int(lineTuple[6])
    if "Липки" == lineTuple[2]:
        massOfLipki += int(lineTuple[6])

    if "1" == lineTuple[0]:
        sumOfDistance += int(lineTuple[5])

    destinationOnLine = lineTuple[3]

    if lineTuple[2] in pointsOfDeparture:
        pointsOfDeparture[lineTuple[2]] += int(lineTuple[6])
    else:
        pointsOfDeparture[lineTuple[2]] = int(lineTuple[6])

    if destinationOnLine in destinations:
        destinations[destinationOnLine] += int(lineTuple[6])
    else:
        destinations[destinationOnLine] = int(lineTuple[6])

    if destinationOnLine in dictOfMaxBenzineAverage:
        dictOfMaxBenzineAverage[destinationOnLine][0] += int(lineTuple[5])
        dictOfMaxBenzineAverage[destinationOnLine][1] += 1
    else:
        dictOfMaxBenzineAverage[destinationOnLine] = [0, 0]
        dictOfMaxBenzineAverage[destinationOnLine][0] = int(lineTuple[5])
        dictOfMaxBenzineAverage[destinationOnLine][1] = 1
        



maxMassOfDay = days[1]
maxBenzineAverage = 0

for i in days:
    if days[i] > massOfLipki:
        maxMassOfDay = days[i]

for key in dictOfMaxBenzineAverage:
    localMax = dictOfMaxBenzineAverage[key][0] / dictOfMaxBenzineAverage[key][1]
    if (localMax) > maxBenzineAverage:
        maxBenzineAverage = localMax





print('Суммарный объем', str(maxMassOfDay))
print('Из поселка Липки', str(massOfLipki))
print('Расстояние за 1 окт', str(sumOfDistance))

for key in pointsOfDeparture:
    print(key, str(pointsOfDeparture[key]))
print('\n')

for key in destinations:
    print(key, str(destinations[key]))
print('\n')

print(maxBenzineAverage)


