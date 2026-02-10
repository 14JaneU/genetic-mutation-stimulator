from colorama import Fore, Style, init

# Enables colour on Windows
init(autoreset=True)


def highlight_dna_changes(original_dna, mutated_dna):
    """
    Highlights nucleotide differences between sequences.
    """

    highlighted_original = ""
    highlighted_mutated = ""

    max_len = max(len(original_dna), len(mutated_dna))

    for i in range(max_len):

        o = original_dna[i] if i < len(original_dna) else "-"
        m = mutated_dna[i] if i < len(mutated_dna) else "-"

        if o == m:
            highlighted_original += Fore.GREEN + o
            highlighted_mutated += Fore.GREEN + m
        else:
            highlighted_original += Fore.RED + o
            highlighted_mutated += Fore.RED + m

    return highlighted_original, highlighted_mutated

def mutation_pointer(original, mutated):
    pointer = ""

    max_len = max(len(original), len(mutated))

    for i in range(max_len):
        o = original[i] if i < len(original) else "-"
        m = mutated[i] if i < len(mutated) else "-"

        if o != m:
            pointer += "^"
        else:
            pointer += " "

    return pointer
