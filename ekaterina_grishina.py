n = input()
summ = 0
multiple = 1
for i in n:
    summ += int(i)
    multiple *= int(i)
print(multiple - summ)
