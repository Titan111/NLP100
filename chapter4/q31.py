import q30

if __name__ == "__main__":
    morphemes = q30.make_morphemes("neko.txt.mecab")
    verbs = set()
    for morphe in morphemes:
        if morphe["pos"] == "動詞":
            verbs.add(morphe["surface"])
    print(verbs)

