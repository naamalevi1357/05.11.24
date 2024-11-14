# start


# 2:

# a:
def my_avg(x: int, y: int) -> float:
    """average"""
    return (x + y) / 2

avg1 = my_avg(90, 99)
print(avg1)


# b:

def my_headline(word: str) -> str:
    return word.upper()+"!"
head1=my_headline("world the concurred has python")
print(head1)

def list_concat(a:list[int], b:list[int], c: list[int])-> list[int]:
    return a + b +c
res_con=list_concat([1,2],[3,4,5,6],[7,8,9])
print(res_con)
print(len(res_con))