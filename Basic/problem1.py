def max_split(S):
    leftCount = 0,rightCount = 0
    previous = []
    current = []

    for char in S:
        current.append(char)
        if char == 'L':
            leftCount += 1
        else:
            rightCount += 1
        if leftCount == rightCount:
            previous.append("".join(current))
            current = []
            leftCount = 0
            rightCount = 0
    print(len(previous))
    for substring in previous:
        print(substring)

result = input().strip()
max_split(result)
