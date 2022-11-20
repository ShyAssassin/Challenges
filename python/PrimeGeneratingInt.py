def GetFactors(number):
    i = 1
    flist = []
    while i < number:
        if number%i == 0:
            flist.append(i)
        i = i + 1
    flist.append(number)
    return flist

def isPrime(number):
  if number == 0 or number == 1:
    return False
  for i in range(2, number):
    if (number % i) == 0:
      return False
  return True

def primeFunction(number, factor):
    return factor + (number // factor)

print(GetFactors(6))
number = int(input("give a number: "))
factors = GetFactors(number)

primes = []
subPrimes = []
for i in factors:
    print(f"factor: {i}")
    subFactors = GetFactors(i)
    addList = True
    for j in subFactors:
        print(f"subfactor: {j}")
        print(f"Prime Func num: {primeFunction(i, j)}")
        if isPrime(primeFunction(i, j)):
            continue
        else:
            print(f"{primeFunction(i, j)} is not prime")
            addList = False
            break
    if addList: subPrimes.append(i)

print(subPrimes)