

day, month, year = eval(input("Enter the day,month,year"))

currentDay = [day, month, year]
compareingDate = [2, 1, 2022]
count = 0
if year < compareingDate[2]:
    while True:

        if currentDay == compareingDate:
            break
        if currentDay[1] > 7:
            if currentDay[1] % 2 == 0:
                if currentDay[0] != 31:
                    currentDay[0] += 1
                else:
                    if currentDay[1] == 12:
                        currentDay[1] = 1
                        currentDay[2] += 1
                    else:
                        currentDay[1] += 1

                    currentDay[0] = 1

            else:

                if currentDay[0] != 30:
                    currentDay[0] += 1
                else:
                    if currentDay[1] == 12:
                        currentDay[1] = 1
                        currentDay[2] += 1
                    else:
                        currentDay[1] += 1

                    currentDay[0] = 1
        elif currentDay[1] == 2:
            if currentDay[2] % 4 == 0:
                if currentDay[2] % 100 == 0:
                    if currentDay[2] % 400 == 0:
                        if currentDay[0] != 29:
                            currentDay[0] += 1
                        else:
                            if currentDay[1] == 12:
                                currentDay[1] = 1
                                currentDay[2] += 1
                            else:
                                currentDay[1] += 1

                            currentDay[0] = 1
                    else:
                        if currentDay[0] != 28:
                            currentDay[0] += 1
                        else:
                            if currentDay[1] == 12:
                                currentDay[1] = 1
                                currentDay[2] += 1
                            else:
                                currentDay[1] += 1

                            currentDay[0] = 1
                else:
                    if currentDay[0] != 29:
                        currentDay[0] += 1
                    else:
                        if currentDay[1] == 12:
                            currentDay[1] = 1
                            currentDay[2] += 1
                        else:
                            currentDay[1] += 1

                        currentDay[0] = 1

            else:
                if currentDay[0] != 28:
                    currentDay[0] += 1
                else:
                    if currentDay[1] == 12:
                        currentDay[1] = 1
                        currentDay[2] += 1
                    else:
                        currentDay[1] += 1

                    currentDay[0] = 1
        else:
            if currentDay[1] % 2 == 0:
                if currentDay[0] != 30:
                    currentDay[0] += 1
                else:
                    if currentDay[1] == 12:
                        currentDay[1] = 1
                        currentDay[2] += 1
                    else:
                        currentDay[1] += 1
                    currentDay[0] = 1

            else:

                if currentDay[0] != 31:
                    currentDay[0] += 1
                else:

                    if currentDay[1] == 12:
                        currentDay[1] = 1
                        currentDay[2] += 1
                    else:
                        currentDay[1] += 1
                    currentDay[0] = 1
        count += 1
days = ["Sundae","Moonday","Chewsday","Weddingday","ThirstDay","Fryday","Saturday"]
print(f"The day is {days[(count)%7]} on {day}/{month}/{year}")
print(count)