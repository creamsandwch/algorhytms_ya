def merge(arr: list, lf, mid, rg):
    res = []

    lft = lf
    md = mid

    while lft < mid and md < rg:
        if arr[lft] <= arr[md]:
            res.append(arr[lft])
            lft += 1
        else:
            res.append(arr[md])
            md += 1

    while lft < mid:
        res.append(arr[lft])
        lft += 1
    while md < rg:
        res.append(arr[md])
        md += 1

    return res


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        print(f'base_rec: arr = {arr[lf:rg]}')
        return arr[lf:rg]
    else:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        print(f'lf, rg = ({lf, rg}), arr[{lf}:{rg}]={arr[lf:rg]}', end=' ')
        arr[lf:rg] = merge(arr, lf, mid, rg)
        print(f'after merge: {arr[lf:rg]}')


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
