q = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

string = q.replace(",","")
words =  string.split(" ")
nums = list(map(lambda x:len(x),words))

print(nums)
