import q30

if __name__ == "__main__":
    morphemes = q30.make_morphemes("neko.txt.mecab")
    result = set()
    for i in range(len(morphemes)):
        if morphemes[i]["surface"] == "の":
            if morphemes[i-1]["pos"] == "名詞" \
            and morphemes[i+1]["pos"] == "名詞":
                A_no_B = ""
                for j in [-1,0,1]:
                    A_no_B += morphemes[i+j]["surface"]
                result.add(A_no_B)

    print(result)




