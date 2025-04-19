if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    maxValue = max(arr)
    list1=[x for x in arr if x != maxValue]
    print(max(list1))
