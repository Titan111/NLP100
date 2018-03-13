import q30

if __name__ == "__main__":
    start_i = 0
    end_i = 0
    befor_noun = False
    noun_list = [] 

    morphemes = q30.make_morphemes("neko.txt.mecab")
    for i in range(len(morphemes)):
        if morphemes[i]["pos"] == "名詞":
            if not befor_noun:
                start_i = i
                befor_noun = True
        else:
            if befor_noun:
                befor_noun = False
                end_i = i
                if start_i == end_i:
                    continue
                noun = ""
                for j in range(start_i,end_i):
                    noun += morphemes[j]["surface"]
                noun_list.append(noun)

    print(max(noun_list,key=lambda x:len(x)))

