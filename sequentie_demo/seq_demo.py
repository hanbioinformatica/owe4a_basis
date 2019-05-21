from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

mijn_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG",IUPAC.unambiguous_dna)
prot = mijn_seq.translate(table=1)
print(prot)
mijn_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG",IUPAC.unambiguous_dna)
prot = mijn_seq.translate(table=2)
print(prot)


# from Bio.Data import CodonTable
# print (CodonTable.unambiguous_dna_by_id.get(2))