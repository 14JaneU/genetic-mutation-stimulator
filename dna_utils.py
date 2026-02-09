
def validate_dna(sequence):
    """
    Validates whether a DNA sequence contains only A, T, C, G.
    Returns True if valid, False otherwise.
    """
    valid_bases = {"A", "T", "C", "G"}
    sequence = sequence.upper()

    if len(sequence) == 0:
        return False

    for base in sequence:
        if base not in valid_bases:
            return False

    return True


def clean_sequence(sequence):
    """
    Removes whitespace and converts sequence to uppercase.
    """
    return sequence.replace(" ", "").replace("\n", "").upper()
