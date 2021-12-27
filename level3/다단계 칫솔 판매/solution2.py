def solution(enroll, referral, seller, amount):
    money, parent = {}, {}
    for e, r in zip(enroll, referral):
        money[e] = 0
        parent[e] = r

    for s, a in zip(seller, amount):
        price = a * 100
        while True:
            total_price = price
            price = total_price//10
            money[s] += total_price-price
            s = parent[s]
            if (s == '-') or (not price):
                break

    return list(money.values())