def check_input(dna: str) -> bool:
    """
    Controleert of de input een correcte DNA-string is.
    Accepteert zowel hoofd- als kleine letters.
    >>> check_input("atgc")
    True
    >>> check_input("atgcAgtAttGCA")
    True
    >>> check_input("hello")
    False
    """
    lowercase_dna = dna.lower()
    for letter in lowercase_dna:
        if letter not in "agct":
            return False
    return True

def transcribe_dna_to_rna(dna: str) -> str:
    """
    Schrijft een string met DNA-elementen in hoofd- en/of kleine
    letters om naar een string met RNA-elementen (als hoofdletters).
    Ga ervan uit dat een valide string wordt gegeven (dus geen
    check aanroepen).
    >>> transcribe_dna_to_rna("atgc")
    'UACG'
    >>> transcribe_dna_to_rna("atgcagtattgca")
    'UACGUCAUAACGU'
    >>> transcribe_dna_to_rna("aaaa")
    'UUUU'
    """
    lowercase_dna = dna.lower()
    rna = ""
    for letter in lowercase_dna:
        if letter == "a":
            rna += "U"
        elif letter == "g":
            rna += "C"
        elif letter == "c":
            rna += "G"
        elif letter == "t":
            rna += "A"
    return rna

if __name__ == '__main__':
    dna = input("DNA: ")
    
    if not check_input(dna):
        print("That is not a valid DNA string")
    else:
        print(f"RNA: {transcribe_dna_to_rna(dna)}")