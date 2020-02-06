import string
def DNA_strand(dna):
    return dna.translate(dna.maketrans("ATCG", "TAGC"))

DNA_strand ("ATTGC")