
import sys

def richieRich(s, n, k):
    # Complete this function
    if n <= 1:
        return s if k < 1 else '9'
    
    h = n / 2
    min_op = 0
    for _ in range(h):
        if s[(n-1)-_] != s[_]:
            min_op += 1
    if min_op > k:
        return '-1'
    
    possible = []
    odd = n % 2 == 1
    for i in range(h+1):
        left = '9'*i + s[i:h]
        right = ''
        i = 0
        while i < len(left):
            right += left[-(i+1)]
            i += 1
        if odd:
            possible.append(left + s[h] + right)
            possible.append(left + '9' + right)
        else:
            pal = left + right
            possible.append(pal)
            
    i = 0
    while i < len(possible):
        palindrome = possible[-(i+1)]
        delta = 0
        for _i in range(len(palindrome)):
            if palindrome[_i] != s[_i]:
                delta += 1
        if delta <= k:
            return palindrome
        i += 1
    
    return '-1'

with open('input10.txt') as f:
    n, k = f.readline().strip().split(' ')
    n, k = int(n), int(k)
    s = f.readline().strip()
    result = richieRich(s, n, k)
    print(result)
