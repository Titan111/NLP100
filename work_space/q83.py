from collections import Counter
import pickle


if __name__ == "__main__":
	tc_counter = Counter()
	t_counter = Counter()
	c_counter = Counter()

	tc_list = []
	t_list = []
	c_list = []

	n=0

	for line in open("result.q82.tsv","r"):
		tc = line.strip()
		word_list = tc.split("\t")
		if len(word_list) !=2:
			print(n)

		t,c =word_list
		tc_list.append(tc)
		t_list.append(t)
		c_list.append(c)
		
		n+=1

		if n % 1000000 == 0:
			tc_counter.update(tc_list)
			t_counter.update(t_list)
			c_counter.update(c_list)
			tc_list = []
			t_list = []
			c_list = []
			print(n,"line finish")

	tc_counter.update(tc_list)
	t_counter.update(t_list)
	c_counter.update(c_list)

	print(n)
	pickle.dump(tc_counter,open("result.q83.tc.bin","wb"))
	pickle.dump(t_counter,open("result.q83.t.bin","wb"))
	pickle.dump(c_counter,open("result.q83.c.bin","wb"))




