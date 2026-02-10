from Bio.Seq import Seq


def translate_dna(sequence):
    """
    Translates a DNA sequence into a protein sequence.
    """
    dna_seq = Seq(sequence)
    protein = dna_seq.translate(to_stop=True)
    return str(protein)


def compare_proteins(original_protein, mutated_protein):
    """
    Compares two protein sequences.
    Returns True if different, False if identical.
    """
    return original_protein != mutated_protein
