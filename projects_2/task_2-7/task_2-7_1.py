files = ["seq1", "seq2", "seq3", "seq4"]
for name in files:
   new_name = name + ".fasta"
   data = "24.04.1998"
   new_data_name = new_name + data
   print(f"{new_data_name}")