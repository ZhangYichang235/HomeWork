for i in range(2):
    P = i
    for j in range(2):
        Q = j
        print(P or not Q or (P and not Q) or (not P and not Q))
