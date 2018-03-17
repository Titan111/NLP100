if __name__ == "__main__":
	f = open("../enwiki-20150112-400-r100-10576.txt","r")
	for line in f:
		tokens = []
		for word in line.strip().split(" "):
			word = word.strip(".,!?;:()[]'\"\t\n"+chr(160) )
			if word == "":
				continue
			tokens.append(word)
		print(*tokens)
