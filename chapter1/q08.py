def my_encode(string):
	result = ""

	for i in string:
		if ord("a") <= ord(i) and ord(i) <= ord("z"):
			result += chr(219-ord(i))
		else:
			result += i

	return result

if __name__ == "__main__":
	print( my_encode("I am an NLPer") )
