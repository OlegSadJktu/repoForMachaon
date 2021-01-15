fileName = "mat_dv.txt" #input("File Name?")

file = open(fileName)

winnerOfParallelClass = dict()
pointsOfMath = [{
    "name" : "",
    "points" : 0
}, {
    "name" : "",
    "points" : 0
}]

for line in file:
    lineTuple = tuple(line.split())

    className = str(lineTuple[2])
    sumOfPoints = int(lineTuple[3]) + int(lineTuple[4])
    if className in winnerOfParallelClass:
        if(sumOfPoints > winnerOfParallelClass[className][1]):
            winnerOfParallelClass[className][0] = lineTuple[0] + " "+ lineTuple[1]
            winnerOfParallelClass[className][1] = sumOfPoints
    else:
        winnerOfParallelClass[className] = [str(lineTuple[0] + lineTuple[1]), sumOfPoints]

    if(int(lineTuple[3]) > pointsOfMath[0]["points"]):
        pointsOfMath[0]["name"] = lineTuple[0] + " " + lineTuple[1] + " " + lineTuple[2]
        pointsOfMath[0]["points"] = int(lineTuple[3])

    if (int(lineTuple[4]) > pointsOfMath[1]["points"]):
        pointsOfMath[1]["name"] = lineTuple[0] + " " + lineTuple[1] + " " + lineTuple[2]
        pointsOfMath[1]["points"] = int(lineTuple[4])

file.close()


for key in winnerOfParallelClass:
    print("Победитель {} класса {} набрал {} баллов".format(
        winnerOfParallelClass[key][0], key,  winnerOfParallelClass[key][1]))

for key in pointsOfMath:
    print(key)