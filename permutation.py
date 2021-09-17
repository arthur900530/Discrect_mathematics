import copy


def perAlg(l):
    fl = []
    for i in range(len(l)+1):
        for j in range(len(l)+1):
            l2 = copy.deepcopy(l)
            if l[i] == l[j]:
                fl.append(l)
            else:
                l2[i] = l[j]
                l2[j] = l[i]
                fl.append(l2)
    print(fl)

perAlg(['A','B','C'])