def calculate_missing(prices):
    missing_prices = []

    for i, price in enumerate(prices):
        if not price:
            prev_price = 0
            weight_previous = 1
            next_price = 0
            weight_next = 1

            j = i
            while j > 0 and prev_price == 0:
                j -= 1
                if prices[j]:
                    prev_price = prices[j]
                else:
                    weight_next += 1

            j = i
            while j < len(prices) and next_price == 0:
                j += 1
                if prices[j]:
                    next_price = prices[j]
                else:
                    weight_previous += 1

            if prev_price and next_price:
                avg_adjacent = (
                    prev_price * weight_previous
                    + weight_next * next_price
                ) / (weight_previous + weight_next)
            else:
                avg_adjacent = prev_price or next_price
            missing_prices.append(avg_adjacent)

    return missing_prices


n = int(input())
prices = []

for i in range(n):
    date, time, price = input().split()

    try:
        price = float(price)
    except ValueError:
        price = None

    prices.append(price)

missing_prices = calculate_missing(prices)
for price in missing_prices:
    print(price)
