def contains_premature_stop (dna_sequence):
    stop_codons = {"TAA", "TAG", "TGA"}

    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]
        if codon in stop_codons:
            return True
    return False

def classify_mutation(original_dna, mutated_dna, original_protein, mutated_protein):
    """
    Classifies mutation type using DNA and protein comparison.
    """
#Classification priority:
#Frameshift > In-Frame indel > Silent > Nonsense > Missense
    
    length_change = len(mutated_dna) - len(original_dna)

    # ---- Frameshift ----
    if length_change != 0 and length_change % 3 != 0:
        return "Frameshift mutation"

    # ---- In-frame insertion / deletion ----
    if length_change > 0 and length_change % 3 == 0:
        return "In-frame insertion"

    if length_change < 0 and length_change % 3 == 0:
        return "In-frame deletion"

    # ---- Silent mutation ----
    if original_protein == mutated_protein:
        return "Silent mutation"

    # ---- Nonsense mutation ----
    if contains_premature_stop(mutated_dna) and original_protein != mutated_protein:
        return "Nonsense mutation"

    if len(mutated_protein) < len(original_protein):
        return "Nonsense mutation"

    # ---- Missense mutation ----
    return "Missense mutation"

