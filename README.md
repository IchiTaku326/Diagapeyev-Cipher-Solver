## 📝 Explanatory Article

For a high-level conceptual overview, methodology breakdown, and visualization of the heuristic search process, check out the official explanatory article on Medium:

👉 **[Decrypting the Diagapeyev Cipher: A Heuristic Approach to Under-Specified Transposition](https://medium.com/@takumiichikawa3126/the-diagapeyev-cipher-has-remained-an-unresolved-cryptographic-puzzle-for-over-eight-decades-7dd805764b8e)**

# Diagapeyev-Cipher-Solver

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

This project applies a heuristic optimization framework to the Diagapeyev Cipher, investigating structural extraction methods. The repository provides the source code, datasets, and experimental logs required to reproduce the computational experiments described in the accompanying paper.

The primary objective is not to claim a definitive historical decryption, but to demonstrate that meaningful linguistic structures can emerge from an optimization-driven search over under-specified transposition parameters.

---

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

Run the main decoder:

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

Using the highest-scoring matrix configuration, the decoding framework produced the following candidate plaintext:

```text
ВОВ: БОЕВАЯ ЗАДАЧА УСТАНОВЛЕНА,
ПОДРАЗДЕЛЕНИЯМ НАЧАТЬ ДВИЖЕНИЕ В
СЕКТОР А.
```

This represents the best-scoring reconstruction obtained during the optimization process. The output is presented as a **heuristically generated candidate plaintext** and should not be interpreted as a confirmed historical decryption.

---

## Sample Output: Observed Linguistic Fragments

The reconstructed text contains several highly coherent Russian linguistic fragments:

> **ВОВ: БОЕВАЯ ЗАДАЧА УСТАНОВЛЕНА.**
> **ПОДРАЗДЕЛЕНИЯМ НАЧАТЬ ДВИЖЕНИЕ В**
> **СЕКТОР А.**

These fragments exhibit strong linguistic consistency according to the trigram language model employed during optimization. Researchers are encouraged to reproduce the experiments by executing the provided `src/solver.py` and `src/optimizer.py` scripts.

---

## License

This repository is provided for research purposes to ensure reproducibility and independent verification of the reported computational results.

---

## How to Cite

If you use this research or code in your work, please cite it as follows:

> Ichikawa, T. (2026). *On Heuristic Structure Extraction in Under-Specified Transposition Ciphers: A Case Study on the Diagapeyev Cipher* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.21132297
