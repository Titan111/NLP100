import q36

word_list = q36.make_word_list("../neko.txt")
word_ranking = q36.make_word_ranking(word_list)
for i in range(10):
    print(word_ranking[i][0] , "," ,word_ranking[i][1] ) 
