num_cases = int(input())
for case in range(num_cases):
    alphabet_nums = list(map(int, input().split()))

    num_to_letter = {}
    for i in range(26):
        num_to_letter[i] = chr(ord('A') + i)

    letter_to_num = {}
    for i in range(26):
        letter_to_num[chr(ord('A') + i)] = alphabet_nums[i]

    num_words = int(input())
    
    encodings = set()
    for i in range(num_words):
        word = input().strip()
        encoding = ''
        for letter in word:
            encoding += str(letter_to_num[letter])
        encodings.add(encoding)

    if len(encodings) < num_words:
        print("Case #{}: YES".format(case+1))
    else:
        print("Case #{}: NO".format(case+1))