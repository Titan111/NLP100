def make_morphemes(file_name):
    f= open(file_name,"r")
    morphemes = [] 
    for line in f:
        node = line.split("\t")
        if node[0] == "EOS\n":
            continue
        surface = node[0]
        node = node[1].split(",")
        morphemes.append({
                    "surface":surface,
                    "base":node[6],
                    "pos":node[0],
                    "pos1":node[1]
                })
    return morphemes

if __name__ == "__main__":
    print(make_morphemes("neko.txt.mecab"))



