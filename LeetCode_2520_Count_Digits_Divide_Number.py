def countDigits(num):
    count = 0
    for i in str(num):
        j=int(i)
        if j==0:
            continue
        if num%j==0:
            count+=1
    return count
