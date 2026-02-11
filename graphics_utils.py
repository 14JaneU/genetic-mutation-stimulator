import matplotlib.pyplot as plt
from collections import Counter


def plot_mutation_types(events):
    """
    Creates bar chart of mutation substitutions.
    """

    if not events:
        print("No mutation events to plot.")
        return

    substitutions = [f"{orig}->{new}" for _, orig, new in events]

    counts = Counter(substitutions)

    labels = list(counts.keys())
    values = list(counts.values())

    plt.figure()
    plt.bar(labels, values)
    plt.title("Mutation Type Distribution")
    plt.xlabel("Substitution")
    plt.ylabel("Frequency")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()
