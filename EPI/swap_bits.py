"""
Given binary input integer x and 2 integers i and j, swap bits at index i and j. 
"""
def swap_bits(x,i,j):
    """
    Returns int with bits at i and j swapped in-place.
    1. Identify bit at index i and j.
    2. If they both are same, ignore.
    3. If they are different, swap those. 
    4. Generate mask and xor.
    """
    if (x>>i & 1) != (x>>j & 1):
        x ^= (1<<i | 1<<j)
    return str(bin(x))

x = int("1001001",2)
i = 1
j = 6
print(swap_bits(x,i,j))
