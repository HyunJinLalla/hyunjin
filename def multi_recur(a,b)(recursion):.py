def multi_recur(a,b):
    if b == 1:
        return a
    else:
        return a + multi_recur(a,b-1)
print(multi_recur(4,2))