def isPrime(a):
    if a == 1:
        return False
    for i in range(2, a):
        if (a % i == 0):
            return False
    return True


s = input("Insert 1 number")

print(isPrime(int(s.split(" ")[0])))
