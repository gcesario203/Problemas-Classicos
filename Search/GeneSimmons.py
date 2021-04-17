from typing import List,Tuple
from enum import IntEnum

Nucleotide: IntEnum =  IntEnum('Nucleotide',('A','C','G','T'))

Codon = Tuple[Nucleotide,Nucleotide,Nucleotide]
Gene = List[Codon]

codon_exists: Codon = (Nucleotide.A,Nucleotide.C,Nucleotide.G)
codon_not_exists: Codon = (Nucleotide.C,Nucleotide.C,Nucleotide.A)

gene_str = 'ACGTGGCTCTCTAACGTACGTATCGACTGATCGATGATCGCCGCCGTATAGCCT'

print(len(gene_str))

def string_to_gene(str_value:str) -> Gene:
    gene:Gene = []

    for i in range(0,len(str_value),3):
        if i + 2 >= len(str_value):
            return gene

        codon: Codon = (Nucleotide[str_value[i]],Nucleotide[str_value[i+1]],Nucleotide[str_value[i+2]])
        gene.append(codon)

    return gene

def binary_search(gene_to_search: Gene, codon_tuple: Codon) -> bool:
    left: int  = 0
    right: int = len(gene_to_search) - 1

    while left <= right:
        mid: int = (left + right)//2
        print(mid)
        if gene_to_search[mid] < codon_tuple:
            left = mid + 1
        elif gene_to_search[mid] > codon_tuple:
            right = mid - 1
        else:
            return True
    return False

teste = string_to_gene(gene_str)
my_gene_ordered: Gene = sorted(teste)
print(binary_search(my_gene_ordered,codon_exists))
print(binary_search(my_gene_ordered,codon_not_exists))
