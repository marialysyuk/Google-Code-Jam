import sys

def reversort(amount, target):
    arr = [1]*(amount-1)
    remaining = target -(amount-1)
    i = 0
    while remaining >0:
        if amount-1-i < remaining:
            arr[i] += amount-1-i
            remaining -= amount-1-i
        else:
            arr[i]+= remaining
            remaining -= remaining
        i +=1
    for i in range(amount-1):
        arr[i] -= 1
    ind = []
    for i in range(amount):
        ind.append(i)
    nums = [0]*amount
    curr_i = 0
    while curr_i < len(nums)-1:
        targ = arr[curr_i]
        nums[curr_i+targ] = curr_i+1
        nums[curr_i:curr_i+targ+1] = reversed(nums[curr_i:curr_i+targ+1])
        ind[curr_i:curr_i+targ+1] = reversed(ind[curr_i:curr_i+targ+1])
        curr_i += 1
    nums[curr_i] = amount
    ans = []
    for i in range(len(nums)):
        ans.append([ind[i], nums[i]])
    ans = sorted(ans)
    fin = []
    for i in range(len(nums)):
        fin.append(ans[i][1])
    return str(' '.join(str(i) for i in fin))
    
def reversort_engineering(amount, minimum, maximum, target):
    if target < minimum or target > maximum:
        return 'IMPOSSIBLE'
    else:
        return reversort(amount, target)
        
nums = sys.stdin.readlines()

content = [[int(num) for num in line.split()] for line in nums]
content = content[1:]
cases = 0
i = 0 
while i < len(content):
    cases += 1
    amount = content[i][0]
    target = content[i][1]
    arr = []
    for k in range(1, amount+1):
        arr.append(k)
    minimum = amount -1
    maximum = amount*(amount+1)/2-1
    ans = reversort_engineering(amount, minimum, maximum, target)
    print("Case #"+str(cases)+": "+str(ans))
    i += 1
