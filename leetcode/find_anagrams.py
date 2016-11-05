def find_anagrams(s, p):

    result = []

    cnts = [0] * 26
    for c in p:
        cnts[ord(c) - ord('a')] += 1

    left, right = 0, 0
    while right < len(s):
        cnts[ord(s[right]) - ord('a')] -= 1
        while left <= right and cnts[ord(s[right]) - ord('a')] < 0:
            cnts[ord(s[left]) - ord('a')] += 1
            left += 1
        if right - left + 1 == len(p):
            result.append(left)
        right += 1

    return result

print(find_anagrams("cbaebabacd", "abc"))
