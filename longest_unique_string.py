def find(string):
    return optimized(string)


# O(n)
def optimized(string):
    longest_start = 0
    longest_end = 0
    current_start = 0
    current_end = 0
    dic = {}
    for i in range(len(string)):
        c = string[i]
        if c in dic:
            prev = dic[c]
            if prev >= current_start:
                if current_end - current_start > longest_end - longest_start:
                    longest_start = current_start
                    longest_end = current_end
                current_start = prev + 1
        dic[c] = i
        current_end += 1
    if current_end - current_start > longest_end - longest_start:
        longest_start = current_start
        longest_end = current_end
    winner = string[longest_start:longest_end]
    print("Longest unique substring: {}".format(winner))
    return len(winner)


# O(n^3)
def naive(string):
    max = 0
    for i in range(len(string)):
        for j in range(len(string) - i):
            candidate = string[i:i + j + 1]
            if len(candidate) > max:
                unique_chars = {}
                for char in candidate:
                    if not char in unique_chars:
                        unique_chars[char] = True
                if len(candidate) == len(unique_chars):
                    max = len(candidate)
    return max
