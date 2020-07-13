def modification(tokenA, tokenB):
    va = tokenA
    vb = tokenB
    ret = 0
    if len(va) != len(vb):
        ret = abs(len(va) - len(vb))
    mn_len = min( len(va), len(vb) )
    va, vb = va[:mn_len], vb[:mn_len]
    for wordA, wordB in zip(va, vb):
        if wordA != wordB:
            ret += 1
    return ret / len(va)