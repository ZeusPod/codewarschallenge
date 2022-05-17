""" GCAT => DNA , GCAU => RNA, Create a function which translates a given DNA string into RNA.
Cree una función que traduzca una cadena de ADN dada en ARN.
 """

def dna_to_rna(dna):
     list_dna = dna.split()
     final_list = []
     for i in list_dna:
            final_list.append(i.replace('T', 'U'))
            return ' '.join(final_list)


print(dna_to_rna("TTTT"))