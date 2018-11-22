import random

list = ["head","tail"]



def throw():
    rand = random.choice(list)
    if rand == "tail":
        return "Tail"
    elif rand == "head":
        return "Head"
ans = "y"
counter_tail = 0
counter_head = 0
while ans == "y":

    answer = input("Throw Coin? y/n")
    ans = answer.lower()
    coin = throw()
    if coin == "Tail":
        counter_tail += 1
        print("Tail Counter:",counter_tail)
    elif coin == "Head":
        counter_head += 1
        print("Head Counter:",counter_head)
