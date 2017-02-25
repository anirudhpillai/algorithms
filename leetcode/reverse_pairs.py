def reverse_pairs(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global counter
        counter = 0

        def mergesort(arr):
            l = len(arr)
            if l <= 1:
                return arr
            else:
                return merge(mergesort(arr[:l//2]), mergesort(arr[l//2:]))

        def merge(one, two):
            result = []
            o, t = 0, 0

            while o < len(one) and t < len(two):
                if one[o] > 2*two[t]:
                    global counter
                    counter += len(one) - o
                    t += 1
                else:
                    o += 1

            o, t = 0, 0

            while o < len(one) and t < len(two):
                if one[o] <= two[t]:
                    result.append(one[o])
                    o += 1
                else:
                    result.append(two[t])
                    t += 1

            result += one[o:]
            result += two[t:]

            return result

        mergesort(nums)
        return counter


print(reverse_pairs([2,4,3,5,1]))
