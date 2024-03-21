roman = input("enter the Roman numeral:")
roman=roman.upper()
Rdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
res = 0
for i in range(len(roman)):
	if i > 0 and Rdict[roman[i]] > Rdict[roman[i-1]]:
		res +=Rdict[roman[i]] - 2 * Rdict[roman[i-1]]
	else:
		res += Rdict[roman[i]]
print("The Decimal equivalent of", roman, "is", res)