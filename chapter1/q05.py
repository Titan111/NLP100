def char_n_gram(string,N=2):
	result = {}
	for i in range(len(string)-N+1):
		gram = string[i:i+N]

		if gram in result:
			result[gram]+=1
		else:
			result[gram]=1

	return result

def word_n_gram(string,N=2):
	result = {}
	words = string.replace(".","").replace(",","").split(" ")
	for i in range(len(words)-N+1):
		gram = ""
		for j in range(N):
			gram += words[i+j]

		if gram in result:
			result[gram]+=1
		else:
			result[gram]=1

	return result

