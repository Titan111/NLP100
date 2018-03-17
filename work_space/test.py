test =  "t \"\" (  \"New Egypt\").  aa aa  aa   aa"

for line in test.split(" "):
	new_str = line.strip(".,!?;:()[]'\"\t\n"+chr(160))
	if new_str != "":
		print(ord(new_str[0]),end="")
	else:
		print(0,end="")
	print(new_str)
		#print("\'"+  ord(new_str[0])  +"\'")
