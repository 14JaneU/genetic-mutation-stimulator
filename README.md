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
## Biological Realism of Model
This simulator implements probabilistic mutation modelling informed by empirical molecular genetics literature.

Key assumptions:

- Transition mutations occur more frequently than transversions with a ratio often greater than 0.5 (~2:1).
- Mutation probability can be adjusted to reflect organism-specific mutation rates.
- Mutation events are modelled per nucleotide position using stochastic simulation.

Supporting Literature:

- Wang J, Raskin L, Samuels DC, Shyr Y, Guo Y. Genome measures used for quality control are dependent on gene function and ancestry. Bioinformatics. 2015 Feb 1;31 (3):318-23. doi: 10.1093/bioinformatics/btu668. Epub 2014 Oct 8. P
- Wu K, Qin D, Qian Y, Liu H. A new era of mutation rate analyses: Concepts and methods. Zool Res. 2024 Jul 18;45(4):767-780. doi: 10.24272/j.issn.2095-8137.2024.058. PMID: 38894520; PMCID: PMC11298668.
- Drake JW, Charlesworth B, Charlesworth D, Crow JF. Rates of spontaneous mutation. Genetics. 1998 Apr;148(4):1667-86. doi: 10.1093/genetics/148.4.1667. PMID: 9560386; PMCID: PMC1460098.
- Nishant KT, Singh ND, Alani E. Genomic mutation rates: what high-throughput methods can tell us. Bioessays. 2009 Sep;31(9):912-20. doi: 10.1002/bies.200900017. PMID: 19644920; PMCID: PMC2952423.
- Xiong X, Boyett JM, Webster RG, Stech J. A stochastic model for estimation of mutation rates in multiple-replication proliferation processes. J Math Biol. 2009 Aug;59(2):175-91. doi: 10.1007/s00285-008-0225-8. Epub 2008 Oct 10. PMID: 18846374; PMCID: PMC2692649.

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


