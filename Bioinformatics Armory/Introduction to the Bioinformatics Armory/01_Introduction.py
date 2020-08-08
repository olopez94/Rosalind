from Bio.Seq import Seq

with open("dataset/rosalind_ini.txt", "r") as f:
    contents = f.read()

my_seq = Seq(contents)
print(my_seq.count("A"), my_seq.count("C"), my_seq.count("G"), my_seq.count("T"))
#my_seq = str(my_seq)

"""
with open("dataset/rosalind_ini_ans.txt", "w") as f:
    f.write("{}".format(my_seq))
"""
