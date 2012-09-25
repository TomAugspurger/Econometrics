def myBootstrap(myData, estimFunc, M=128):
    N = len(myData)
    h = [0.0] * M
    bootSamp = [0.0]*N
    for sample in range(M):
        for val in range(N):
            bootSampe[val] = myData[randint(0, N-1)]
        h[sample] = estimFunc(bootSamp)
        originEstim = estimFunc(myData)
        return origEstim