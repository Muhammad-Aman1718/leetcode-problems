# All About That Base

t = int(input())

for _ in range(t):
    dna = input()
    convertDNA = ""
    for i in range(len(dna)):
        if dna[i] == "A":
            convertDNA += "T"
        elif dna[i] == "T":
            convertDNA += "A"
        elif dna[i] == "C":
            convertDNA += "G"
        elif dna[i] == "G":
            convertDNA += "C"

    print(convertDNA)
