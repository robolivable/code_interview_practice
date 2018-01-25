def sum_integer_strings(ar):
    return str(sum([int(i) for i in ar]))

def _aVeryBigSum(n, ar):
    # Complete this function
    if n == 1:
        return sum_integer_strings(ar)
    left, right = [], []
    for snum in ar:
        left.append(snum[:-1])
        right.append(snum[-1])
    r = str(_aVeryBigSum(1, right))
    carry, base = 0, r[0]
    if len(r) > 1:
        carry, base = r[:-1], r[-1]
    return '%s%s' % (int(_aVeryBigSum(n-1, left)) + int(carry), base)
    
def aVeryBigSum(n, ar):
    ar = sorted(ar, reverse=True)
    z = len(str(ar[0]))
    ar = [str(n).zfill(z) for n in ar]
    return _aVeryBigSum(z, ar)

a1 = [1, 123, 43, 2345, 1, 3234, 2]
a2 = ['99764700', '94679148', '90889282', '70431391', '67277123', '64529748',
      '60841180', '46626298', '12848728']
a3 = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

import random

a4 = [int(1 * 10**5)+1 for _ in range(10000000)]

print aVeryBigSum(0, a1)
print aVeryBigSum(0, a2)
print aVeryBigSum(0, a3)
print aVeryBigSum(0, a4)


