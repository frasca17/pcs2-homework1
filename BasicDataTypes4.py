if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    A = max(arr)
    while max(arr) == A:
        arr.remove(A)
    print max(arr)