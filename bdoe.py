a = int(input(':')) 
b = []

for i in range(a):
        c = input(':')
        b.append(c)

for j in range(a):
        for t in range(a):
                if b[j] < b[t]:
                        b[j],b[t] = b[t],b[j]


print(b)
print(b[0])


