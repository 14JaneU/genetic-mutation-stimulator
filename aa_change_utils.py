from Bio.Seq import Seq

def detect_amino_acid_changes(original_data, mutated_dna):
    """
    Detects codon and amino acid changes between original and mutated DNA sequences.
    Returns a list of changes.
   
    """

    changes = []
    #compare only up to the shortest sequence 
    min_length = min(len(original_data), len(mutated_dna))

    #iterate through codons in both sequences
    for i in range(0, min_length - 2, 3):

        original_codon = original_data[i:i+3]
        mutated_codon = mutated_dna[i:i+3]

        if original_codon != mutated_codon:

            #translate codons to amino acids
            original_aa = str(Seq(original_codon).translate())
            mutated_aa = str(Seq(mutated_codon).translate())
                              
            changes.append({
                "codon_position": i // 3 + 1,
                "original_codon": original_codon,
                "mutated_codon": mutated_codon,
                "original_amino_acid": original_aa,
                "mutated_amino_acid": mutated_aa
            })

    return changes