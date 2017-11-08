def money(dollar):

	#dollar*=100
	quarters=dollar//25
	amount_left=dollar-(quarters*25)
	dimes=amount_left//10
	amount_left=amount_left - (dimes*10)
	nickles=amount_left//5
	amount_left=amount_left - (nickles*5)
	cents=amount_left
	print("Number of quarters = "+str(quarters))
	print("Number of dimes = "+str(dimes))
	print("Number of nickles = "+str(nickles))
	print("Number of cents = "+str(cents))


money(99)
print()
money(13)