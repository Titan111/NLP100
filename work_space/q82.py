import random
if __name__ == "__main__":
	for line in open("result.q81.txt","r"):
		words = line.strip().split(" ")
		N = len(words)
		for i in range(N):
			d = random.randrange(5)+1
			for j in range(d):
				pos = (i-1)-j
				if pos > 0:
					print(words[i],words[pos],sep="\t")
			for j in range(d):
				pos = (i+1)+j
				if pos < N:
					print(words[i],words[pos],sep="\t")
