import MeCab

def make_word_list(file_name):
    mecab = MeCab.Tagger("-Owakati")
    f = open(file_name)
    wakati_str = ""
    for line in f:
        wakati_str += mecab.parse(line)
    return wakati_str.split(" ")

def make_word_ranking(words):
    word_freq = {}
    for one_word in words:
        if one_word in word_freq:
            word_freq[one_word]+=1
        else:
            word_freq[one_word]=1

    return sorted(word_freq.items(),key=lambda x:x[1],reverse=True)


if __name__ == "__main__":
    word_list = make_word_list("../neko.txt")
    word_ranking = make_word_ranking(word_list)
    for line in word_ranking:
        print(line[0],"\t",line[1])

