# sherlock_strings.py
'''
Sherlock considers a string, , to be valid if either of the following
conditions are satisfied:

All characters in  have the same exact frequency (i.e., occur the same
number of times). For example,  is valid, but  is not valid.

Deleting exactly  character from  will result in all its characters
having the same frequency. For example,  and  are valid because all
their letters will have the same frequency if we remove  occurrence of
c, but  is not valid because we'd need to remove  characters.

Given , can you determine if it's valid or not? If it's valid, print
YES on a new line; otherwise, print NO instead.
'''

TRUE = 'YES'
FALSE = 'NO'

def isValid(s):
    # Complete this function
    char_map = {}
    for c in s:
        if c not in char_map:
            char_map[c] = 0
        char_map[c] += 1
    counts_map = {}
    for n in char_map.values():
        if n not in counts_map:
            counts_map[n] = 0
        counts_map[n] += 1
    if len(counts_map) == 1:
        return TRUE
    if len(counts_map) > 2:
        return FALSE
    minority_value = min(*counts_map.values())
    if minority_value > 1:
        return FALSE
    for k in counts_map:
        if counts_map[k] == minority_value:
            minority_key = k
        else:
            majority_key = k
    if minority_key > majority_key:
        delta = minority_key - majority_key
    else:
        delta = minority_key
    return TRUE if delta <= 1 else FALSE

print isValid('aaabbbccceeeefffggg')

