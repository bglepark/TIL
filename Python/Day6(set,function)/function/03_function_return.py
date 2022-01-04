# 상품 가격, 주문 수량을 입력받아서 주문액을 계산하여 반환하는 함수 작성
# 함수명 : order()


# 상품 가격 입력 :
# 주문 수량 입력 :
# ------------------
# 상품 가격 : 1000원
# 주문 수량 : 10개
# 주문액 : 10000원

def order():
    price = int(input('상품 가격 입력 : '))
    amount = int(input('주문 수량 입력 : '))
    total = price * amount
    print('-' * 20)
    print('상품 가격 : %d 원' % price)
    print('주문 수량 : %d 개 ' % amount)
    print('주문액 : %d 원' % total)
    return total


order()


# 강사 코드

def order():
    price = int(input('상품 가격 입력 : '))
    amount = int(input('주문 수량 입력 : '))
    total = price * amount
    return price , amount , total

price , qty , amount = order()

price('--------------')
print('상품 가격 : %d원' %price)
print('주문수량 : %d개' %qty)
print('주문액 : %d원' %amount)


