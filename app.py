from classification_utils import classify_mutation
from metadata_utils import mutation_metadata
from aa_change_utils import detect_amino_acid_changes
from visualisation_utils import highlight_dna_changes
from visualisation_utils import mutation_pointer

from dna_utils import validate_dna, clean_sequence
from mutation_functions import (
    substitution_mutation,
    insertion_mutation,
    deletion_mutation
)
from protein_utils import translate_dna, compare_proteins

def main():
    print("Genetic Mutation Simulator")
    print("--------------------------")

    dna_sequence = input("Enter a DNA sequence: ")
    dna_sequence = clean_sequence(dna_sequence)

    if not validate_dna(dna_sequence):
        print("Invalid DNA sequence. Please use only A, T, C, G.")
        return

    original_protein = translate_dna(dna_sequence)

    print("\nChoose mutation type:")
    print("1 - Substitution")
    print("2 - Insertion")
    print("3 - Deletion")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        mutated, pos, original, new = substitution_mutation(dna_sequence)
        mutation_description = f"Substitution at position {pos}: {original} → {new}"

    elif choice == "2":
        mutated, pos, inserted = insertion_mutation(dna_sequence)
        mutation_description = f"Insertion at position {pos}: inserted {inserted}"

    elif choice == "3":
        mutated, pos, deleted = deletion_mutation(dna_sequence)
        mutation_description = f"Deletion at position {pos}: removed {deleted}"

    else:
        print("Invalid choice.")
        return

    mutated_protein = translate_dna(mutated)
    mutation_type = classify_mutation(
        dna_sequence,
        mutated,
        original_protein,
        mutated_protein
    )

    print("\nMutation summary:")
    print(mutation_description)

    vis_original, vis_mutated = highlight_dna_changes(dna_sequence, mutated)

    print("\nDNA Visualisation:")
    
    print("Original:", vis_original)
    print("Mutated :", vis_mutated)
    print("          ", mutation_pointer(dna_sequence, mutated))


    print("\nOriginal protein:")
    print(original_protein)

    print("\nMutated protein:")
    print(mutated_protein)

    print("\nMutation classification:")
    print(mutation_type)

    size, frame = mutation_metadata(dna_sequence, mutated)

    print("\nMutation metadata:")
    print(f"Mutation size: {size}")
    print(f"Reading frame disrupted: {frame}")


    amino_acid_changes = detect_amino_acid_changes(dna_sequence, mutated)
    if amino_acid_changes:
        print("\nAmino acid changes:")

        for change in amino_acid_changes:
            print(
                f"Codon {change['codon_position']}: "
                f"{change['original_codon']} → ({change['mutated_codon']}) | "
                f"{change['original_amino_acid']} → {change['mutated_amino_acid']}")
    else:
        print("\nNo amino acid changes detected.")
   
    if compare_proteins(original_protein, mutated_protein):
        print("\n⚠️ Protein sequence changed due to mutation.")
    else:
        print("\n✅ Protein sequence unchanged (silent mutation).")


if __name__ == "__main__":
    main()
