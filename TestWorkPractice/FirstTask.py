def alsoCalculateDistance(func):
    def wrapper(starting, final, time):
        try:
            accel = func(starting, final, time)
        except ZeroDivisionError:
            print("Время равно нулю")
            return 0
        except TypeError:
            print("Неверный тип данных")
            return 0

        distance = starting * time + (accel * time * time) / 2
        return "Ускорение = {} \n" \
               "Расстояние = {}".format(accel, distance)
    return wrapper

@alsoCalculateDistance
def calculateAcceleration(starting, final, time):
    return ((final - starting) / time)

print(calculateAcceleration(5, 10, 0))