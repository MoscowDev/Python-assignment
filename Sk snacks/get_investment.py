def get_investment(investment_amount,monthly_interest_rate, years):
	
	numberOfMonths = years / 12
	future_investment_value = investment_amount*(1+ monthly_interest_rate)**numberOfMonths


	return(future_investment_value)

print(get_investment(5,10,2))