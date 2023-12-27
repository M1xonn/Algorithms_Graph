from arraylist import ArrayList


def getMinRun(arr: ArrayList):
    n = len(arr)
    r = 0
    while n >= 64:
        r = r | (n & 1)
        n //= 2
    return n + r


def binarySearch(arr: ArrayList, left, right, val, key):
    if left == right:
        if arr[left][key] > val:
            return left
        else:
            return left + 1
    elif left > right:
        return left
    else:
        mid = (left + right) // 2
        if arr[mid][key] > val:
            return binarySearch(arr, left, mid - 1, val, key)
        elif arr[mid][key] < val:
            return binarySearch(arr, mid + 1, right, val, key)
        else:
            return mid


def binaryInsertionSort(arr: ArrayList, key):
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        index = binarySearch(arr, 0, i - 1, arr[i][key], key)
        if index != i:
            arr.insert(index, arr[i])
            arr.remove(i + 1)
    return arr


def reverse(arr: ArrayList):
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]


def merge(left: ArrayList, right: ArrayList, key):
    l = 0
    r = 0
    res = ArrayList()
    while l < len(left) and r < len(right):
        if l < len(left) and left[l][key] < right[r][key]:
            res.push(left[l])
            l += 1
        else:
            res.push(right[r])
            r += 1

    if r == len(right):
        while l < len(left):
            res.push(left[l])
            l += 1
    else:
        while r < len(right):
            res.push(right[r])
            r += 1

    return res


def TimSort(arr: ArrayList, key):
    min_run = getMinRun(arr)
    res = ArrayList()
    runs = ArrayList()
    run = ArrayList()
    i = 0
    while i <= len(arr):
        if len(run) < 2:
            run.push(arr[i])
            i += 1
            continue
        order = run[-1][key] - run[-2][key]

        if i >= len(arr) or (arr[i][key] >= run[-1][key] and order < 0) or (arr[i][key] < run[-1][key] and order >= 0):
            if len(run) < min_run:
                if i + min_run < len(arr):
                    for j in range(i, i + min_run):
                        run.push(arr[j])
                else:
                    for j in range(i, len(arr)):
                        run.push(arr[j])
                run = binaryInsertionSort(run, key)
                i += min_run
            elif len(run) >= min_run and order < 0:
                reverse(run)
            runs.push(ArrayList(run)[0])
            run = ArrayList()
            if i != len(arr):
                i -= 1
        else:
            run.push(arr[i])
        i += 1
        while len(runs) > 0:
            if len(runs) == 1:
                res = runs.pop()
            elif len(runs) == 2:
                res = merge(runs.pop(), runs.pop(), key)
            else:
                x = runs.pop()
                y = runs.pop()
                z = runs.pop()

                if not (len(x) > len(y) + len(z)) or not (len(y) > len(z)):
                    if len(x) >= len(z):
                        z = merge(z, y, key)
                    else:
                        x = merge(x, y, key)
                    runs.push(z)
                    runs.push(x)
                else:
                    runs.push(z)
                    runs.push(y)
                    runs.push(x)

    return res
