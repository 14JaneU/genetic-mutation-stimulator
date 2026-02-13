import streamlit as st

from dna_utils import clean_sequence, validate_dna
from protein_utils import translate_dna
from mutation_functions import (
    substitution_mutation,
    insertion_mutation,
    deletion_mutation
)
from probability_utils import apply_mutation_probability


def read_uploaded_fasta(uploaded_file):
    sequence = ""

    for line in uploaded_file:
        line = line.decode("utf-8").strip()

        if line.startswith(">"):
            continue

        sequence += line

    return sequence.upper()

st.set_page_config(page_title="Genetic Mutation Simulator", layout="wide")

st.title("🧬 Genetic Mutation Simulator")
st.write("Simulate DNA mutations and analyse protein effects")

# Sidebar Controls
st.sidebar.header("Mutation Settings")

mutation_type = st.sidebar.selectbox(
    "Select Mutation Type",
    ["Substitution", "Insertion", "Deletion", "Probability-based"]
)

mutation_rate = st.sidebar.slider(
    "Mutation Rate",
    0.0, 1.0, 0.05
)


# Main Input

input_method = st.radio(
    "Choose input method:",
    ("Manual Input", "Upload FASTA File")
)

dna_sequence = ""

if input_method == "Manual Input":
    dna_sequence = st.text_area("Enter DNA Sequence:")

elif input_method == "Upload FASTA File":
    uploaded_file = st.file_uploader(
        "Upload FASTA file",
        type=["fasta", "fa", "txt"]
    )

    if uploaded_file:
            dna_sequence = read_uploaded_fasta(uploaded_file)

            st.success("FASTA file uploaded successfully!")
            st.text_area("Extracted DNA Sequence:", dna_sequence)


if dna_sequence:

    dna_sequence = clean_sequence(dna_sequence)

    if validate_dna(dna_sequence):
        st.success("Valid DNA sequence loaded!")
    else:
        st.error("Invalid DNA sequence.")

run_simulation = st.button("Run Simulation")

if run_simulation and dna_sequence:
        original_protein = translate_dna(dna_sequence)

        # --- Mutation Selection ---
        if mutation_type == "Substitution":
            mutated, pos, original, new = substitution_mutation(dna_sequence)

        elif mutation_type == "Insertion":
            mutated, pos, inserted = insertion_mutation(dna_sequence)

        elif mutation_type == "Deletion":
            mutated, pos, deleted = deletion_mutation(dna_sequence)

        elif mutation_type == "Probability-based":
            mutated, events = apply_mutation_probability(
                dna_sequence,
                mutation_rate,
            )

        mutated_protein = translate_dna(mutated)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original DNA")
            st.code(dna_sequence)

            st.subheader("Original Protein")
            st.code(original_protein)

        with col2:
            st.subheader("Mutated DNA")
            st.code(mutated)

            st.subheader("Mutated Protein")
            st.code(mutated_protein)

        if mutation_type == "Substitution":
            st.info(f"Substitution at position {pos+1}: {original} → {new}")

        elif mutation_type == "Insertion":
            st.info(f"Insertion at position {pos+1}: {inserted}")

        elif mutation_type == "Deletion":
            st.info(f"Deletion at position {pos+1}: {deleted}")

        elif mutation_type == "Probability-based":
            st.info(f"Total mutations: {len(events)}")
