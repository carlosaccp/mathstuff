def Euclid():
    userinput = input("Enter 2 numbers separated by a space: ")
    n1,n2 = userinput.split(' ')
    n1 = int(n1)
    n2 = int(n2)
    maxn = max(n1,n2)
    minn = min(n1,n2)
    while minn != 0:
        remainder = maxn - int(maxn/minn)*minn
        maxn = minn
        minn = remainder
    print('Their GCD is: ' + str(maxn))

Euclid()
