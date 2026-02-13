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

**Key assumptions**:

- Transition mutations occur more frequently than transversions.
- Mutation probability can be adjusted to reflect organism-specific mutation rates. 
- Mutation events are modelled per nucleotide position using stochastic simulation.

**Supporting Literature**:

- Wang J, Raskin L, Samuels DC, Shyr Y, Guo Y. Genome measures used for quality control are dependent on gene function and ancestry. Bioinformatics. 2015 Feb 1;31 (3):318-23. doi: 10.1093/bioinformatics/btu668. Epub 2014 Oct 8. P
- Wu K, Qin D, Qian Y, Liu H. A new era of mutation rate analyses: Concepts and methods. Zool Res. 2024 Jul 18;45(4):767-780. doi: 10.24272/j.issn.2095-8137.2024.058. PMID: 38894520; PMCID: PMC11298668.
- Drake JW, Charlesworth B, Charlesworth D, Crow JF. Rates of spontaneous mutation. Genetics. 1998 Apr;148(4):1667-86. doi: 10.1093/genetics/148.4.1667. PMID: 9560386; PMCID: PMC1460098.
- Nishant KT, Singh ND, Alani E. Genomic mutation rates: what high-throughput methods can tell us. Bioessays. 2009 Sep;31(9):912-20. doi: 10.1002/bies.200900017. PMID: 19644920; PMCID: PMC2952423.
- Xiong X, Boyett JM, Webster RG, Stech J. A stochastic model for estimation of mutation rates in multiple-replication proliferation processes. J Math Biol. 2009 Aug;59(2):175-91. doi: 10.1007/s00285-008-0225-8. Epub 2008 Oct 10. PMID: 18846374; PMCID: PMC2692649.

## Biological Mutation Weighting 
**Background**

Adenine (A) and guanine (G) are two-ring purine-based nucleotides and cytosine (C) and thymine (T) are one-ring pyrimidine-derived nucleotides. [1]

In substitution mutations, transitions are defined as the interchange of the purine-based **A↔G** or pryimidine-based **C↔T**. Transversions are defined as the interchange between two-ring purine nucleobases and one-ring pyrimidine bases. The possible transversions are **A↔C**, **A↔T**, **C↔G**, **G↔T**. [1]

In theory, if substitution mutations occur randomly, then the Ti/Tv ratio averaged over a large enough number of substations should be 0.5, because there are two possible transitions and four possible transversions. [1] However, transitions are more common because they involve substituting a single-ring structure for another, or double-ring for double-ring, which is less physically disruptive to the DNA helix than the pyrimidine-purine swap of transversions.

Thus, in real sequencing data, the transition and transversion ratio is often greater than 0.5. [1]

**Default Ratio**

Based on molecular genetic literature, this model's default ratio approximates 2:1 transition/transversion bias. 

**References**

1. Wang J, Raskin L, Samuels DC, Shyr Y, Guo Y. Genome measures used for quality control are dependent on gene function and ancestry. Bioinformatics. 2015 Feb 1;31(3):318-23. doi: 10.1093/bioinformatics/btu668. Epub 2014 Oct 8. PMID: 25297068; PMCID: PMC4308666.

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

```
## Example Outputs 

**CLI Version**

<img width="275" height="454" alt="image" src="https://github.com/user-attachments/assets/ecd2a999-31b6-4214-b7f6-30a654c32654" />
<img width="498" height="359" alt="image" src="https://github.com/user-attachments/assets/16d49e23-f101-4b73-90a2-503d58fbf8bc" />
<img width="385" height="288" alt="image" src="https://github.com/user-attachments/assets/93589843-f8aa-42bb-ab3f-018d64bf253b" />

**GUI Version**

<img width="928" height="469" alt="image" src="https://github.com/user-attachments/assets/0cc26e52-551c-4555-b2b3-77738079b329" />
<img width="920" height="218" alt="image" src="https://github.com/user-attachments/assets/51056f6c-3e33-4696-8bec-da6e5b4b7190" />

## Future Improvements 
- Real genome dataset integration
- Advanced mutation heatmaps
- Add all of the CLI version features to GUI version
