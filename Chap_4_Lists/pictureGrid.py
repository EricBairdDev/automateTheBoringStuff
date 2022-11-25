def pyramidFunc(N):
    k = N - 1
    for i in range(N):
        for j in range(k):
            print(end=" ")
        k = k - 1
        for j in range(i + 1):
            print("* ", end="")
        print('\r')

while True:
    print('Please enter a positive integer:')
    try:
        N = int(input())
    except ValueError:
        continue
    if N < 1:
        continue
    else:
        break
pyramidFunc(N)