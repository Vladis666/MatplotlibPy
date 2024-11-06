lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, -10]


def get_filter(a, filter=None):
    if filter is None:
        return a

    res = []
    for x in a:
        if filter(x):
            res.append(x)

    return res


z = get_filter(lst, lambda x: x%2==0)
print(z)
