# def week():
    # n = 0
    # w = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # while n <= 6:
    #     yield w[n]
    #     n += 1

def week():
    days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
    ]
    for day in days:
        yield day


days = week()
print(next(days))
print(next(days))