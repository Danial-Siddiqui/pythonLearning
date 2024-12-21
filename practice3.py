numel = int(input("How many items are on your list?"))
numlist = []
for x in range(numel):
    num = int(input('what is your number?'))
    numlist.append(num)
for x in range(numel):
    if numlist[x] < 5:
        print(numlist[x])



