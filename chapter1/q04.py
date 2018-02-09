q = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = q.split(" ")
print(words)
index = 0
one_char = [1,5,6,7,8,9,15,16,19,1024]
next_one = 0
answer = {}
for i in words:
	index+=1
	if index == one_char[next_one]:
		answer[index] = i[0:1]
		next_one += 1
	else:
		answer[index] = i[0:2]
	
print(answer)

