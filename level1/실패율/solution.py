def solution(N, stages):
    a_lst, n_dict = [i for i in range(1, N+1)], {}
    tot = len(stages)
    for i in stages:
        n_dict[i] = n_dict[i] + 1 if i in n_dict else 1

    if N+1 in n_dict:
        del n_dict[N+1]

    for i, val in sorted(n_dict.items(), key=lambda x: x):
        n_dict[i] = val / tot
        tot -= val

    b_lst = []
    for n in sorted(n_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True):
        a_lst.remove(n[0])
        b_lst.append(n[0])

    return b_lst + a_lst