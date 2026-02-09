from dna_utils import validate_dna, clean_sequence
from mutation_functions import (
    substitution_mutation, 
    insertion_mutation, 
    deletion_mutation
)

def main():
    print("Genetic Mutation Simulator")
    print("--------------------------")

    dna_sequence = input("Enter a DNA sequence: ")
    dna_sequence = clean_sequence(dna_sequence)

    if not validate_dna(dna_sequence):
        print("Invalid DNA sequence. Please use only A, T, C, G.")
        return
    
    print("\nChoose mutation type:")
    print("1. Substitution")
    print("2. Insertion")
    print("3. Deletion")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        mutated_sequence, pos, original_base, new_base = substitution_mutation(dna_sequence)
        print(f"\nSubstitution Mutation:")
        print(f"Original Sequence: {dna_sequence}")
        print(f"Mutated Sequence:  {mutated_sequence}")
        print(f"Position: {pos}, Original Base: {original_base}, New Base: {new_base}")

    elif choice == "2":
        mutated_sequence, pos, inserted_base = insertion_mutation(dna_sequence)
        print(f"\nInsertion Mutation:")
        print(f"Original Sequence: {dna_sequence}")
        print(f"Mutated Sequence:  {mutated_sequence}")
        print(f"Position: {pos}, Inserted Base: {inserted_base}")

    elif choice == "3":
        mutated_sequence, pos, deleted_base = deletion_mutation(dna_sequence)
        print(f"\nDeletion Mutation:")
        print(f"Original Sequence: {dna_sequence}")
        print(f"Mutated Sequence:  {mutated_sequence}")
        print(f"Position: {pos}, Deleted Base: {deleted_base}")

    else: 
        print("Invalid choice. Please only use A, T, C, G.")
        return

if __name__ == "__main__":
    main()
