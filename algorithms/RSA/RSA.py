DEBUG = False


def isPrime(num):
    """
    Tell whether the given number is a prime number
    """
    if num < 1:
        return False
    if num == 1:
        return True
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True


def findHighestCommonFactor(a, b):
    if b == 0:
        return a
    else:
        return findHighestCommonFactor(b, a % b)


print(findHighestCommonFactor(48, 60))
print(findHighestCommonFactor(60, 48))


def countNumOfPrimeFromOne(num):
    count = 0
    breakNumbers = []
    for i in range(1, num):
        hcf = findHighestCommonFactor(i, num)
        if hcf == 1:
            count += 1
            breakNumbers.append(i)
            if DEBUG:
                print(
                    f"Number {i} is a break number to number {num}, count + 1 = {count}"
                )
    return count, breakNumbers


print(8, countNumOfPrimeFromOne(8))
print(20, countNumOfPrimeFromOne(20))
print(30, countNumOfPrimeFromOne(30))
print(31, countNumOfPrimeFromOne(31))
print(35, countNumOfPrimeFromOne(35))
print(37, countNumOfPrimeFromOne(37))
