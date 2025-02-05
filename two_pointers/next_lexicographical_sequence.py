def next_lexicographical_sequence(s: str) -> str:
    # Write your code here
    # 'abcdefghijklmnopqrstuvwxyz'
    #      01234567890123456789012
    # s = 'syrkcbptalfgkjihgfedcba'  ; left=11, right=15
    # s = 'syrkcbptalfgkkkkkkkkkkk'  ; left=11, right=22
    # s = 'syrkcbptalfgk'            ; left=11, right=12
    # s = 'syrkcbptalfgkfedcba'      ; left=11, right=12
    # Let's try Narayan Pandit's algorithm here.
    N = len(s)
    # "left" is the highest index at which a character is less than its right neighbor
    left = None
    for i in range(N-1):
        if s[i] < s[i+1]:
            left = i
    if left is None:
        # The string is the last in lexicographical order, just return the reversed string
        return s[::-1]
    # "right" is the highest index at which a character is greater than the one in "left"
    right = N - 1
    for i in range(N-1, -1, -1):
        if s[i] > s[left]:
            right = i
            break
    # Swap left and right characters
    arr = list(s)
    arr[left], arr[right] = arr[right], arr[left]
    # Now reverse everything from left+1 onwards till the end
    arr = arr[:left+1] + arr[left+1:][::-1]
    return ''.join(arr)


