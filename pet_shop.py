square_meters = float(input())
price = float(input())
price = square_meters * 7.61
discount = 0.18 * price
discount_price = price - discount
print(f'The final price is {discount_price} lv.')
print(f'The discount is {discount} lv.')