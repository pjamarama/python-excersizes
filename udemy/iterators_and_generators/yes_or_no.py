# def yes_or_no():
#     while True:
#         answer = 1
#         if answer == True:
#             yield 'yes'
#             answer = 0
#         yield 'no'
#         answer = 1

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"

gen = yes_or_no()
