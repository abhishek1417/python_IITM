

# Write a python program using dictionary to get the transverse of dna sequence ?
a='ATGCTTAG'
b=""

codon = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

for i in a:
    b=b+codon[i]
print(b)

# OR # wonderful apprach in reference of data science
input='ATGCTTAG'
condon={'A':'T','T':'A','C':'G','G':'C'}
output=""

for i in input:
    temp=""
    for key,value in condon.items():
        if(i==key):
           temp=temp+ i.replace(i,value)

    output=output+temp
print(output)
