def main(a,b):
	t1,t2 = a,b
	m1 = n2 = 1
	m2 = n1 = 0
	while True:
		q = a//b
		r = a - q*b
		m = m1 - q*m2
		n = n1 - q*n2
		a = b
		b = r
		m1 = m2
		m2 = m
		n1 = n2
		n2 = n
		if (a == 0) or (b == 0):
			m = m1
			n = n1
			break

	if a == 0:
		gcd = b
		print(f"GCD: {b}")
	else:
		gcd = a
		print(f"GCD: {a}")

	print(f"m: {m} \n n: {n}")
	cn = (gcd == (m*t1 + n*t2))
	print(f"Condition: {cn}")
	return gcd

if __name__ == '__main__':
	a = int(input("Enter 1st number: "))
	b = int(input("Enter 2nd number: "))
	main(a,b)