"""
Given binary input array x and 2 integers i and j, swap bits at index i and j. 
"""
def swap_bits(x,i,j):
    """
    Updates input array with bits at i and j swapped in-place.
    1. Identify bit at index i and j.
    2. If they both are same, ignore.
    3. If they are different, swap those. 
    4. Generate mask and xor.
    """
    if (x>>i & 1) != (x>>j & j):
        x = x ^ (x>>i | x>>j)

x = [0,1,0,0,1,0,0,1]
i = 1
j = 6
swap_bits(x,i,j)
print(x)
