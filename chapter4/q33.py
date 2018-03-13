import q30

if __name__ == "__main__":
    morphemes = q30.make_morphemes("neko.txt.mecab")
    verbs = set()
    for morphe in morphemes:
        if morphe["pos"] == "名詞" and morphe["pos1"] == "サ変接続":
            verbs.add(morphe["base"])
    print(verbs)

