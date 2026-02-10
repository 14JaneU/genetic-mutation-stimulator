def mutation_metadata(original_dna, mutated_dna):
    length_change = len(mutated_dna) - len(original_dna)

    if length_change > 0:
        size_text = f"+{length_change} nucleotide(s)"
    elif length_change < 0:
        size_text = f"{length_change} nucleotide(s)"
    else:
        size_text = "0 nucleotides"

    if length_change != 0 and length_change % 3 != 0:
        frame_text = "Yes"
    else:
        frame_text = "No"

    return size_text, frame_text
