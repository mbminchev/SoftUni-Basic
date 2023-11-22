square_meters_for_landscaping = float(input())
prise_for_the_whole_yard = square_meters_for_landscaping * 7.61
discount = prise_for_the_whole_yard * 0.18
total_sum = prise_for_the_whole_yard - discount

print(f"The final prise is: {total_sum} lv.")
print(f"The discount is: {discount} lv.")
