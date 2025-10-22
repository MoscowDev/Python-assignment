
def get_drivers_payment_per_day(collection ):
	base_pay = 5000
	if collection <= 50:
		amount_per_parcel = 160
		payment = (amount_per_parcel * collection ) + base_pay
		return payment

	elif collection > 50 and collection <= 59:
		amount_per_parcel = 200
		payment = (amount_per_parcel * collection) + base_pay
		return payment

	elif collection > 60 and collection <= 69:
		amount_per_parcel = 250
		payment = (amount_per_parcel * collection) + base_pay
		return payment

	elif collection >= 70 and collection <=100:
		amount_per_parcel = 500
		payment = (amount_per_parcel * collection) + base_pay
		return payment

		
		