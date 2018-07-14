for _ in range(int(input())):
    S = input()
    even = ''
    odd = ''
    for i in range(len(S)):
        if i % 2 == 0:
            even += S[i]
        else:
            odd += S[i]
    print(even, odd)