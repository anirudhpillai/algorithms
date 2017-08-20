class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        Beats 97.25%
        """
        one = {v: i for i, v in enumerate(list1)}
        index_values = [(i + one[v], v) for i, v in enumerate(list2) if v in one]
        min_index = min(index_values, key=lambda x: x[0])[0]
        return [i[1] for i in index_values if i[0] == min_index]
