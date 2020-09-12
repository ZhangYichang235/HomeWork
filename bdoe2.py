a = int(input(':'))
b = []

for i in range(a):
        c = int(input())
        b.append(c)

for j in range(a - 1):
        for t in range(a - 1):
                if b[t] > b[t + 1]:
                        b[t],b[t + 1] = b[t + 1],b[t]

print(b)


