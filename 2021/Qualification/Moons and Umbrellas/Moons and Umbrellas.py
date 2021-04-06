import sys

def moons_umbrellas(CJ_price, JC_price, word):
    CJ = 0
    JC = 0
    C = 0
    J = 0
    for i in range(len(word)):
        if word[i] == 'C':
            if C == 0:
                C += 1
                if J == 1:
                    JC += 1
                    J = 0
        if word[i] == 'J':
            if J == 0:
                J += 1
                if C == 1:
                    CJ += 1
                    C = 0
    result = CJ*CJ_price+JC*JC_price
    return result
    
nums = sys.stdin.readlines()
content = [x.split() for x in nums]
content = content[1:]

cases = 0
i = 0 
while i < len(content):
    cases += 1
    CJ_price = int(content[i][0])
    JC_price = int(content[i][1])
    word = content[i][2]
    print("Case #"+str(cases)+": "+str(moons_umbrellas(CJ_price, JC_price, word)))
    i += 1
