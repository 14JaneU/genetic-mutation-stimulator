import random
def substitution_mutation(sequence):
    bases = ["A", "T", "C", "G"]
    pos = random.randint(0, len(sequence) - 1)
    original_base = sequence[pos]
    new_base = random.choice([b for b in bases if b != original_base])
    mutated_sequence = sequence[:pos] + new_base + sequence[pos + 1:]
    return mutated_sequence, pos, original_base, new_base

def insertion_mutation(sequence):
    bases = ["A", "T", "C", "G"]
    pos = random.randint(0, len(sequence))
    inserted_base = random.choice(bases)
    mutated_sequence = sequence[:pos] + inserted_base + sequence[pos:]
    return mutated_sequence, pos, inserted_base


def deletion_mutation(sequence):
    pos = random.randint(0, len(sequence) - 1)
    deleted_base = sequence[pos]
    mutated_sequence = sequence[:pos] + sequence[pos + 1:]
    return mutated_sequence, pos, deleted_base

