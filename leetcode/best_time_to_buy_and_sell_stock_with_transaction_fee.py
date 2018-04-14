class Solution:
    def __init__(self):
        self.dp = {}

    def maxProfit(self, prices, fee):
        """
         day i, we have two situations:

        Hold stock:
        (1) We do nothing on day i: hold[i - 1];
        (2) We buy stock on day i: notHold[i - 1] - prices[i];

        Not hold stock:
        (1) We do nothing on day i: notHold[i - 1];
        (2) We sell stock on day i: hold[i - 1] + prices[i] - fee;
        """
        hold, not_hold = -prices[0], 0

        for price in prices:
            p_hold = hold
            hold = max(hold, not_hold - price)  # buy more stack
            not_hold = max(not_hold, p_hold + price - fee)  # sell more stock

        return not_hold
