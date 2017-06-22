def answer(chunk, word):
    candidates = []
    seen = set()

    def findCombs(chunk, word):
        if chunk in seen:
            return
        if chunk.find(word) < 0:
            candidates.append(chunk)
            seen.add(chunk)
            return
        for i in range(len(chunk) - len(word) + 1):
            if chunk[i] == word[0]:
                if chunk[i:i+len(word)] == word:
                    findCombs(chunk[:i] + chunk[i+len(word):], word)
                    seen.add(chunk[:i] + chunk[i+len(word):])

    findCombs(chunk, word)

    a = min(candidates, key=len)
    rem = [i for i in candidates if len(i) == len(a)]
    return min(rem)


chunk = "googoodgoogogoooogoogfogoood"
word = "goo"

print(answer(chunk, word))
