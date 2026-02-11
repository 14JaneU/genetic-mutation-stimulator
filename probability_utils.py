import random


def apply_mutation_probability(sequence, mutation_rate):
    """
    Applies substitution mutations across sequence using probability.
    """

    mutated = list(sequence)

    bases = ["A", "T", "C", "G"]

    mutation_events = []

    for i in range(len(mutated)):

        if random.random() < mutation_rate:

            original_base = mutated[i]

            possible_bases = bases.copy()
            possible_bases.remove(original_base)

            new_base = random.choice(possible_bases)

            mutated[i] = new_base

            mutation_events.append((i, original_base, new_base))

    return "".join(mutated), mutation_events
