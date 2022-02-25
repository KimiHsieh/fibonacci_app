def fibonacci(val):
    if val == 0:
        return 0
    if val == 1:
        return 1

    arr = [0] * (val + 1)
    arr[0] = 0
    arr[1] = 1
    for i in range(2, val + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[val]
