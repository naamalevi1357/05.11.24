# start
from urllib.parse import ParseResult


# 1:

# a:

def my_ascending(a: int, b: int):
    # for i in range (a,b,1):
    #     print(i,end= " ")
    if a > b:
        print(a, b)
    else:
        print(b, a)


my_ascending(-12, 7)


# b:
def my_details(word: str):
    print(word[0])
    print(word[-1])
    print(word[(len(word) // 2)])


my_details("AI is the best")


# c:

def say_bool(bool1: bool):
    if bool1 == True:
        print("yes")
    else:
        print("no")


say_bool(True)
say_bool(False)


# d:
def print_zugi(list: list[int]):
    for i in list:
        if i % 2 == 0:
            print("even")
        else:
            print("odd")


print_zugi([5, 3, 2, 10, 15, 14, 14])


# e:
def my_statistics(list1: list[int]):
    print(max(list1))
    print(min(list1))
    a = sum(list1)
    b = len(list1)
    print(a)
    print(a / b)


# my_statistics([5, 3, 2, 10, 15, 16, 14])
scores: list[int] = []
score: int = 0
while True:
    score: int = int(input(" what is score?"))

    if score == -99:
        break
    if score > 100 or score < 0:
        continue
#
    scores.append(score)
print(scores)
my_statistics(scores)


help(my_avg)





# stop
