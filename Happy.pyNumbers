

def check_happy_num(num):
    numm = str(num)


    sum = 0
    while sum !=1 and sum < 101:

        sum = 0
        for i in numm:

            k = int(i)
            sum += k**2
            c = sum
            numm = str(c)

    if sum == 1:
        return True

    else:
        return False


for i in range(1,100,1):
    if check_happy_num(i):
        print(i)


