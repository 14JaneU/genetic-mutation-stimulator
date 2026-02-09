from dna_utils import validate_dna, clean_sequence

def main():
    print("Genetic Mutation Simulator")
    print("--------------------------")

    dna_sequence = input("Enter a DNA sequence: ")
    dna_sequence = clean_sequence(dna_sequence)

    if not validate_dna(dna_sequence):
        print("Invalid DNA sequence. Please use only A, T, C, G.")
        return

    print("Valid DNA sequence entered:")
    print(dna_sequence)
    print(f"Sequence length: {len(dna_sequence)}")


if __name__ == "__main__":
    main()
