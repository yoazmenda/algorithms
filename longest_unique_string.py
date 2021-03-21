def find(string):
    return naive(string)


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
