import pdb

if __name__ == "__main__":
    file_name = "../enwiki-20150112-400-r100-10576.txt"
    f = open(file_name,"r")
    for line in f:
        for word in line.strip().split(" "):
            print(word.strip("\.,!?;:()[]'\"\n\t"),end=" ")
