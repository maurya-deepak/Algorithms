# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    a.sort()
    countDict = {}
    for i in a:
        if i in countDict:
            countDict[i] += 1
        else:
            countDict[i] = 1
    for key in countDict.keys():
        if countDict[key] > right // 2:
            return key
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
