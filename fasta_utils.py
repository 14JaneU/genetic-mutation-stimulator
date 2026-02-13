def read_fasta(file_path):
    """
    Reads DNA sequence from FASTA file
    Returns sequence as a single string
    """

    sequence = ""

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            # Skip header
            if line.startswith(">"):
                continue

            sequence += line

    return sequence.upper()
