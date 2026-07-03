## 📝 Explanatory Article

For a high-level conceptual overview, methodology breakdown, and visualization of the heuristic search process, check out the official explanatory article on Medium:

👉 **[Decrypting the Diagapeyev Cipher: A Heuristic Approach to Under-Specified Transposition](https://medium.com/@takumiichikawa3126/the-diagapeyev-cipher-has-remained-an-unresolved-cryptographic-puzzle-for-over-eight-decades-7dd805764b8e)**

# Diagapeyev-Cipher-Solver

> A reproducible computational framework for heuristic analysis of the unsolved Diagapeyev Cipher (1939).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21022129.svg)](https://doi.org/10.5281/zenodo.21022129)

This repository contains the computational framework, source code, and experimental logs used in the following research paper.

---

## Paper Information

**Title**
*On Heuristic Structure Extraction in Under-Specified Transposition Ciphers: A Case Study on the Diagapeyev Cipher*

**Author**
Takumi Ichikawa

**Version**
1.1.0 (July 2026)

**DOI (Current Version)**
https://doi.org/10.5281/zenodo.21022129

**DOI (Concept/Latest)**
https://doi.org/10.5281/zenodo.21022128 *(Always resolves to the latest version)*

---

## Project Overview

The Diagapeyev Cipher is an unsolved transposition cipher first published in 1939. More than 80 years later, no publicly verified key, encryption procedure, or authoritative plaintext has been established.

This project applies a heuristic optimization framework to investigate the structural properties of the cipher through computational search. Rather than claiming a definitive historical decryption, the objective is to demonstrate that statistically meaningful linguistic structures can emerge from optimization over under-specified transposition parameters.

The repository provides the source code, datasets, optimization logs, and documentation required to reproduce every computational experiment described in the accompanying paper.

---

## Original Ciphertext

The original Diagapeyev Cipher consists solely of the following numerical ciphertext. This ciphertext serves as the sole input to all experiments presented in this repository.

```text
75628 28591 62916 48164 91748 58464 74748 28483 81638 18174
74826 26475 83828 49175 74658 37575 75936 36565 81638 17585
75756 46282 92857 46382 75748 38165 81848 56485 64858 56382
72628 36281 81728 16463 75828 16483 63828 58163 63630 47481
91918 46385 84656 48565 62946 26285 91859 17491 72756 46575
71658 36264 74818 28462 82649 18193 65626 48484 91838 57491
81657 27483 83858 28364 62726 26562 83759 27263 82827 27283
82858 47582 81837 28462 82837 58164 75748 58162 92000
```

## Contents

```text
.
├── src/      # Python source code used for decryption experiments
├── logs/     # Decryption logs for each phase and matrix configurations corresponding to peak scores
└── data/     # Cryptograms and datasets used in the experiments
```

---

## Usage

### 1. Basic Decryption

Run the main decoding program:

```bash
python src/solver.py
```

This script implements the decryption framework using a 6×6 Straddling Checkerboard together with alternating key cycles (30, 40) to reconstruct candidate plaintext.

### 2. Heuristic Search

Run the optimization procedure:

```bash
python src/optimizer.py
```

The optimizer searches candidate checkerboard configurations by anchoring high-frequency symbols and maximizing a Russian trigram-based scoring function.

---

## Experimental Results (Highest Score)

The following 6×6 matrix achieved the highest log-score (**15.84**) during the heuristic search.

| Row |  1  |  2  |  3  |  4  |  5  |  6  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|  1  |  Г  |  Я  |  Ж  |  Ю  |  Ц  |  -  |
|  2  |  Э  |  С  |  Ч  |  К  |  З  |  -  |
|  3  |  Ф  |  Н  |  П  |  Ы  |  Л  |  -  |
|  4  |  Ш  |  Е  |  И  |  В  |  Б  |  -  |
|  5  |  А  |  О  |  М  |  Р  |  Т  |  -  |
|  6  |  Д  |  У  |  Щ  |  -  |  Х  |  -  |

---

## Generated Candidate Plaintext

Using the original ciphertext together with the highest-scoring 6×6 matrix configuration, the decoding framework produced the following candidate plaintext:

```text
ВОВ: БОЕВАЯ ЗАДАЧА УСТАНОВЛЕНА,
ПОДРАЗДЕЛЕНИЯМ НАЧАТЬ ДВИЖЕНИЕ В
СЕКТОР А.
```

This represents the highest-scoring reconstruction obtained during the optimization process. The output is presented as a **heuristically generated candidate plaintext** and should not be interpreted as a confirmed historical decryption.

---

## Sample Output: Observed Linguistic Fragments

The reconstructed text contains several highly coherent Russian linguistic fragments:

> **ВОВ: БОЕВАЯ ЗАДАЧА УСТАНОВЛЕНА.**
> **ПОДРАЗДЕЛЕНИЯМ НАЧАТЬ ДВИЖЕНИЕ В**
> **СЕКТОР А.**

These fragments exhibit strong linguistic consistency according to the trigram language model employed during optimization. Researchers are encouraged to reproduce the experiments by executing the provided `src/solver.py` and `src/optimizer.py` scripts.

---

## Reproducibility

All source code, datasets, optimization logs, and the accompanying paper are publicly available so that every experiment reported in this repository can be independently reproduced and verified.

Researchers can reproduce the reported candidate plaintext by executing `src/solver.py` together with the optimization framework included in this repository.

## License

This repository is provided for research and educational purposes.

---

## How to Cite

If you use this research or code in your work, please cite it as follows:

> Ichikawa, T. (2026). *On Heuristic Structure Extraction in Under-Specified Transposition Ciphers: A Case Study on the Diagapeyev Cipher* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.21132297

---

## Acknowledgements

The Diagapeyev Cipher remains an open problem in classical cryptanalysis.

This repository is intended as an open and reproducible research project. Contributions, discussion, independent verification, and alternative approaches are welcome.
