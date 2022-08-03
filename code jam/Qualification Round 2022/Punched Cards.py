T = int(input())

for k in range(1, T+1):
    R, C = map(int, input().split()) # row, col
    print("Case #%d:" % k)

    for i in range (R * 2 + 1):
        for j in range (C * 2 + 1):
            if (i <= 1 and j <= 1):
                print(".", end = "")
            elif (i % 2 == 1 and j % 2 == 1):
                print(".", end = "")
            elif (i % 2 == 1):
                print("|", end = "")
            elif (j % 2 == 1):
                print("-", end = "")
            else:
                print("+",end = "")
        print(' ')
