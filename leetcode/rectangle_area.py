class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        Beats 95.28%
        """
        result = abs(A-C) * abs(B-D) + abs(E-G) * abs(F-H)

        if not (C < E or A > G or D < F or H < B):
            width = min(C, G) - max(A, E)
            height = min(D, H) - max(B, F)
            result -= width * height

        return result
