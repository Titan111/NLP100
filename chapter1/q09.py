import random
def typoglycemia(string):
	words = string.split(" ")
	result = []
	for i in words:
		len_i = len(i)
		if len_i > 4:
			one_word = i[0]
			one_word += "".join(random.sample(i[1:len_i-1],k=len_i-2))
			one_word += i[-1]
			result.append(one_word)
		else:
			result.append(i)
	
	return " ".join(result)

if __name__ == "__main__":
	print( typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .") )


