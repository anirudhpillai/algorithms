from collections import deque

# @param arr : list of integers
# @param w : width of the window
# @return a list of integers
def answer(arr, w):
    # deque gives a double ended queue
    # Q[0] is peeking from back
    # Q[-1] is peeking from front
    # Q will store the index of elements in the array
    Q = deque()
    ret = []
    for i in range(w):
        # for each element, the previous smaller elements are useless so removing them
        while Q and arr[i] >= arr[Q[0]]:
            Q.popleft()
        # adding the index of current element at the back of the queue
        Q.appendleft(i)
    for i in range(w, len(arr)):
        # element at the front is largest element from previous window
        ret.append(arr[Q[-1]])
        # removing element not part of the window
        # storing the index in Q helps us calculate this easily
        while Q and Q[-1] <= i-w:
            Q.pop()
        # remove useless elements
        while Q and arr[i] >= arr[Q[0]]:
            Q.popleft()
        Q.appendleft(i)
    ret.append(arr[Q[-1]])
    return ret

assert answer([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
