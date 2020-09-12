def c(a, b, n, m):
        if m > 0:
                for i in range(n, m - 1,-1):
                        b[m-1] = a[i - 1]
                        c(a, b, i-1, m-1)

        else:
                print(b)

def main():
        n = int(input(':'))
        m = int(input(':'))
        arr = [i + 1 for i in range(n)]
        b=[0 for i in range(m)]
        c(arr, b, n, m)

main()
