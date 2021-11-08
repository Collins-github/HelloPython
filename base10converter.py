# converts any number from base 10 to another base

number_in_base_10 = int(input("Number in base 10: "))
new_base = int(input("Input the base you want to covert it to: "))
remainder = []

while number_in_base_10 != 0:
	remainder.append(number_in_base_10 % new_base)
	number_in_base_10 //= new_base
remainder.reverse()
print(remainder)
