a = int(input(':'))
b = []

for i in range(a):
        c = int(input())
        b.append(c)

x = 0
for j in range(a - 1, 0, -1):
        for t in range(j):
                if b[t] > b[t + 1]:
                        b[t],b[t + 1] = b[t + 1],b[t]
                        x += 1

print(x)


