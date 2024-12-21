dividend = int(input('what is your number?'))
divisors = []
for x in range(dividend):
    rem = dividend%(x+1)
    if rem == 0:
        divisors.append(x+1)
print(divisors)
