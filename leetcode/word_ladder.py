from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordDict):
        """
        Bidirectional BFS
        """

        # BFS attempt
        # queue = deque([(beginWord, 1)])
        # seen = set()

        # while queue:
        #     word, length = queue.popleft()
        #     if word == endWord:
        #         return length

        #     for i in range(len(word)):
        #         for letter in "abcdefghijklmnopqrstuvwxyz":
        #             new_word = word[:i] + letter + word[i+1:]
        #             if new_word in wordList and new_word not in seen:
        #                 queue.append((new_word, length+1))
        #                 seen.add(new_word)

        # return 0

        if endWord not in wordDict:
            return 0

        length = 2
        front, back = set([beginWord]), set([endWord])
        wordDict = set(wordDict)

        while front:
            jumps = set()
            for word in front:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        jumps.add(word[:i] + c + word[i+1:])

            front = wordDict & jumps

            if front & back:
                return length

            length += 1

            if len(front) > len(back):
                front, back = back, front

            wordDict -= front

        return 0
