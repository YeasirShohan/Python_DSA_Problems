def countDigits(n):
    count = 0
    for i in str(n):
        j=int(i)
        if j==0:
            continue
        if n%j==0:
            count+=1
    return count

print(countDigits(10112))