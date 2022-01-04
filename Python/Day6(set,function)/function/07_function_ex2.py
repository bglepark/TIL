# 문제
# 할인액(discount) 계산
# 주문액이 10만원 이상이면 10% 할인
# 주문액이 5만원 이상 10만원 미만이면 5% 할인
# 주문액이 5만원 미만이면 할인 없음

def order(price, qt):
    amount = price * qt
    if amount >= 100000:
        discount = amount * 0.1
    elif 50000<=amount<100000 :
        discount = amount *0.05
    else :
        discount = 0
    result = amount - discount
    return amount , discount , result

price = int(input('상품가격 : '))
qt = int(input('주문수량 : '))
amount , discount , result = order(price, qt)

print(f'주문액 : {amount}')
print(f'할인액 : {discount}')
print(f'지불액 : {result}')

# qt를 기본으로 고정하는 방법
# def order(price, qt = 100):
#     # 내용은 같다
# amount , discount , result = order(price)
# qt = 100으로 고정되어 있으니 매개변수로 price 1개만 사용하면 된다

