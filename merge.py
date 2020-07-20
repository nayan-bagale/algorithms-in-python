import sys

sys.setrecursionlimit(10 ** 6)


def merge(a, b):
    c = []
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    return c


def merge_sort(a):
    if len(a) <= 1: return a
    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:])
    # print(left,right)
    return merge(left, right)


if __name__ == '__main__':
    def createarray(size=10, max=100):
        from random import randint
        return [randint(0, max) for _ in range(size)]


    temp = createarray()
    print(merge_sort(temp))
