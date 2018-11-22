for i in range(2,100,1):
    print("\n")
    while i != 1:
        if i % 2 == 0:
            i = round(i / 2)
            print(i, end="--")

        elif i % 2 == 1:
            i = round(i * 3 + 1)
            print(i, end="--")

