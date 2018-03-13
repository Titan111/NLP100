import matplotlib.pyplot as plt
import q36

word_list = q36.make_word_list("../neko.txt")
word_ranking = q36.make_word_ranking(word_list)

freq_list = list(map(lambda x:x[1],word_ranking))
print(freq_list)

plt.hist(freq_list,range=(0,1000),normed=False)
plt.show()
