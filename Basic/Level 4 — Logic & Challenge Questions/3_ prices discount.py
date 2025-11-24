# Given a list of prices, apply 10% discount to each.

price=[99, 15, 239, 149, 399, 999]
discount=0.10
for i in range(len(price)):
    price[i]=price[i]-(price[i]*discount)
print(price)