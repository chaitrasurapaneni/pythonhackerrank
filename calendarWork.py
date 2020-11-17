import calendar
day = input().split(" ")

cd = (calendar.weekday(int(day[2]), int(day[0]), int(day[1])))
print(list(calendar.day_name)[cd].upper())

