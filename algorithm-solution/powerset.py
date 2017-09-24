def powerset(Set):
		set_list= list(Set)
		power_size= 2 ** len(Set)
		for i in range(power_size):
			for j in range(len(Set)):
				if i & 1 << j:
					print(set_list[j],end=" ")
			print("\n")
		


powerset(set(["a","b","c"]))