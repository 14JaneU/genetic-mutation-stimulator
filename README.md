# Genetic Mutation Simulator

A Python-based tool for simulating genetic mutations in DNA sequences and analysing their potential biological impact.

## Project Overview
This project is a Python-based bioinformatics tool designed to simulate DNA mutations and analyse their effects on protein translation. The simulator models substitution, insertion, deletion and probabilistic mutation events while providing mutation classification, amino acid impact analysis and sequence visualisation.

## Features
- DNA sequence validation and cleaning
- Simulation of substitution, insertion, and deletion mutations
- Probabilty-based mutation modelling
- Mutation classification (silent, missense, nonsense, frameshift)
- Amino acid change detection 
- Mutation metadata reporting
- DNA sequence visualisation
- Interactive GUI using Streamlit
- Mutation statistics visualisation using matplotlib

## Scientific Relevance

Mutation modelling is essential in genomics research, precision medicine and evolutionary biology. This tool demonstrates how nucleotide-level changes influence protein translation and functional outcomes.

## Technologies
- Python
- Biopython
- Matplotlib
- Streamlit

## Installation

```bash
git clone <https://github.com/14JaneU/genetic-mutation-stimulator>
cd genetic-mutation-simulator
pip install -r requirements.txt
```
## Running the Program

Run CLI version:

```bash
python app.py
```

Run GUI version:

```bash
python -m streamlit run streamlit_app.py
```
## Example Output

GUI version:
<img width="940" height="485" alt="image" src="https://github.com/user-attachments/assets/9c0eba08-fef3-4fd9-829d-04019a9fd712" />

## Project Structure 

```
app.py
streamlit_app.py
dna_utils.py
mutation_functions.py
classification_utils.py
metadata_utils.py
aa_change_utils.py
statistics_utils.py
graphics_util.py
visualisation_utils.py
```
## Future Improvements

```
- Real genome dataset integration
- Literature-based mutation rate modelling
- Advanced mutation heatmaps
```
## Code Structure 

```
genetic-mutation-simulator
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dna_utils.py
├── mutation_functions.py
├── classification_utils.py
├── metadata_utils.py
├── aa_change_utils.py
├── statistics_utils.py
├── visualisation_utils.py
├── probability_utils.py


