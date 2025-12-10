def prefixSum(arr):
    ans = []
    ans.append(arr[0])
    for i in range(1, len(arr)):
        x = ans[i-1]+ arr[i]
        ans.append(x)
    return ans

arr= [5,6,3,8,2]

print(prefixSum(arr))