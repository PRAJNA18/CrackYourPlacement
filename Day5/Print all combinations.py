def combinations(ind, curr, arr, k, ans):
    if len(curr) == k:
        ans.append(curr.copy())
    else:
        for i in range(ind, len(arr)):
            curr.append(arr[i])
            combinations(i+1, curr, arr, k, ans)
            curr.pop()
    return ans

arr = list(map(int, input().split()))
k = int(input())
if k > len(arr) or k == 0:
    print("Not possible")
else:
    print(combinations(0, [], arr, k, []))
    