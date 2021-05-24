def aladdin(magic, dist):
    if sum(magic) < sum(dist): return -1
    len = len(magic)
    total = 0
    result = 0
    for i in range(len):
        if total < 0:
            result = i
            total = 0
        total += (magic[i] - dist[i])
    return result