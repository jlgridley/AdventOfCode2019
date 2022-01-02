
total = 0
with open("input") as f:
    for line in f:
        num = int(line.strip())
        while num > 0:
            num = max(0, num//3 - 2)
            total += num

print(total)
