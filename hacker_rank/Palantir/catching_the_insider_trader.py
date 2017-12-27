def findPotentialInsiderTraders(datafeed):
    result = []
    prices = {}  # {day: price}
    trades = {}  # {day: [trades]}

    for item in datafeed:
        items = item.split("|")

        if len(items) == 2:
            day, price = items
            prices[int(day)] = int(price)
        else:
            day, trader, ttype, quantity = items

            if int(day) in trades:
                trades[int(day)].append((trader, ttype, int(quantity)))
            else:
                trades[int(day)] = [(trader, ttype, int(quantity))]

    for day in sorted(prices.keys())[1:]:
        current_price = prices[day]
        for prev_day in range(max(0, day-3), day):
            if prev_day not in trades:
                continue

            for d in range(prev_day, -1, -1):
                if d in prices:
                    prev_price = prices[d]
                    break

            for trade in trades[prev_day]:
                change = (current_price - prev_price) * trade[2]
                if (
                    (trade[1] == "BUY" and change >= 500000)
                    or (trade[1] == "SELL" and change <= -500000)
                ):
                    result.append((prev_day, trade[0]))

    result = sorted(set(result))
    return ["{}|{}".format(day, trader) for day, trader in result]
