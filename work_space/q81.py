
if __name__ == "__main__":
	f = open("country_name.txt","r")
	country_names = list( map(lambda x:x.strip(),f))

	f = open("result.q80.txt","r")
	for line in f:
		for name in country_names:
			new_name = name.replace(" ","_")
			line = line.strip().replace(name,new_name)
		print(line)
