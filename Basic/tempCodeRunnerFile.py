s = input()
balance = 0
res = []
temp = ""

for ch in s:
    temp += ch
    if ch == 'L':
        balance += 1
    else:
        balance -= 1
    if balance == 0:
        res.append(temp)
        temp = ""

print(len(res))
for part in res:
    print(part)
