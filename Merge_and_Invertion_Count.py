import sys

sys.setrecursionlimit(10 ** 6)


def merge(left, right, inversions):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):

        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
            inversions += (len(left) - left_idx)

    if left_idx == len(left):
        result.extend(right[right_idx:])
    else:
        result.extend(left[left_idx:])

    return result, inversions


def merge_sort(array, inv_count=0):
    if len(array) <= 1: return array, inv_count
    left = merge_sort(array[:len(array) // 2], inv_count)
    right = merge_sort(array[len(array) // 2:], inv_count)
    inv_count = left[1] + right[1]
    return merge(left[0], right[0], inv_count)


if __name__ == '__main__':
    def createarray(size=10, max=100):
        from random import randint
        return [randint(0, max) for _ in range(size)]



    sorted_array, inversion = merge_sort(createarray())

    print(sorted_array)
    print(inversion)
