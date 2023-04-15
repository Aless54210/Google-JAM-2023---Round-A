def count_chars(i):
    totChars = 0
    for letter in string.ascii_uppercase:
        if letter <= chr(ord('Z') + 1):
            totChars += i
    return totChars

def get_char(n):
    i = 1
    totChars = count_chars(i)
    while totChars < n:
        i += 1
        totChars = count_chars(i)
    offset = n - (totChars - count_chars(i-1))
    index = (offset - 1) // i
    letter = chr(ord('A') + index)
    return letter


T = int(input())
for t in range(1, T+1):
    n = int(input())
    char = get_char(n)
    print("Case #{}: {}".format(t, char))
