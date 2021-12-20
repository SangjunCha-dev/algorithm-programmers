def solution(enroll, referral, seller, amount):
    answer = []

    data = {'center': {'amount': 0,'parent': None}}
    for i in range(len(enroll)):
        data[enroll[i]] = {
            'amount': 0,
            'parent': referral[i] if referral[i] != '-' else 'center'
        }

    for i in range(len(seller)):
        sell = seller[i]
        price = amount[i] * 100
        data[sell]['amount'] += price-price//10
        price = price//10

        while data[sell]['parent'] and price:
            sell = data[sell]['parent']
            if sell == 'center':
                data[sell]['amount'] += price
                break
            data[sell]['amount'] += price-price//10
            price = price//10

    del data['center']
    for value in data.values():
        answer.append(value['amount'])

    return answer