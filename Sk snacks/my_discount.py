def my_discount(price,discount):
	discount = price * discount/100
	#price = price - discount
	
	return price-discount

print(my_discount(150,15))