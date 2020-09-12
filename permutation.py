def perm(a, low, high):
        if low == high:
                print(a)

        else:
                for i in range(low, high+1):
                        a[i],a[low] = a[low],a[i]
                        perm(a, low + 1, high)
                        a[i],a[low] = a[low], a[i]


perm([1,2,3], 0, 2)
