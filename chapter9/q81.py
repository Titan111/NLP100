if __name__ == "__main__":
    
    file_name = "data/country_list.txt"
    country_list = list(map(lambda x:x.strip(),open(file_name,"r")))

    file_name = "data/words.txt"
    f = open(file_name,"r")
    for line in f:
        for name in country_list:
            new_name = name.replace(" ","_")
            line = line.replace(name,new_name)
        print(line)

