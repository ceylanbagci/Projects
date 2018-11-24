#######################################
#        Fizz Buzz                    #
#                                     #
#                                     #
#######################################
def fizz():
    return "fizz, "

def buzz():
    return "buzz, "

def fizzbuzz():
    return "fizzbuzz, "

if __name__ == '__main__':
    for i in range(101):
        if i%10 == 0:
            print("\n")
        if i%3 == 0:
            print(fizz(),end="")
        elif i%5 == 0:
            print(buzz(),end="")
        elif i%3 == 0 and i%5 == 0 :
            print(fizzbuzz(),end="")
        else:
            print(i,end=", ")
