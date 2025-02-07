words = ["a", "aba", "ababa", "aa"]

def isPrefixAndSuffix(str1, str2):
    return str2.startswith(str1) and str2.endswith(str1)

def find_count(words):
    count = 0  # Make count a local variable
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if isPrefixAndSuffix(words[i], words[j]):
                count += 1
    return count

print(find_count(words))
