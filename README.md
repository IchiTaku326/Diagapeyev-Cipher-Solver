# Diagapeyev-Cipher-Solver

> A reproducible computational framework for heuristic analysis of the unsolved Diagapeyev Cipher (1939).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21484792.svg)](https://doi.org/10.5281/zenodo.21484792)

---

## 📝 Explanatory Article

For a high-level conceptual overview, a detailed explanation of the methodology, and a visualization of the heuristic search process, see the accompanying Medium article:

👉 **[Decrypting the Diagapeyev Cipher: A Heuristic Approach to Under-Specified Transposition](https://medium.com/@takumiichikawa3126/the-diagapeyev-cipher-has-remained-an-unresolved-cryptographic-puzzle-for-over-eight-decades-7dd805764b8e)**

---

## Paper Information

**Title**

*On Heuristic Structure Extraction in Under-Specified Transposition Ciphers: A Case Study on the Diagapeyev Cipher*

**Author**

Takumi Ichikawa

**Version**

v3 (July 2026)

**DOI (Current Version)**

https://doi.org/10.5281/zenodo.21484792

**DOI (Concept DOI / Always Resolves to the Latest Version)**

https://doi.org/10.5281/zenodo.21022128

---

# Project Overview

The **Diagapeyev Cipher** is an unsolved transposition cipher first published in **1939**. More than eighty years later, no publicly verified key, encryption procedure, or authoritative plaintext has been established.

This project investigates the structural properties of the cipher using a reproducible heuristic optimization framework.

Rather than claiming a definitive historical decryption, the objective is to demonstrate that statistically meaningful linguistic structures can emerge through optimization over under-specified transposition parameters.

The repository contains everything required to reproduce the computational experiments presented in the accompanying paper, including:

- Python source code
- Experimental datasets
- Optimization logs
- Candidate checkerboard matrices
- Documentation

Every experiment reported in the paper can be independently reproduced from this repository.

---

# Original Ciphertext

The original Diagapeyev Cipher consists solely of the following numerical ciphertext.

This ciphertext serves as the only input used throughout every experiment contained in this repository.

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

---

# 🔍 Decryption Mechanism

The proposed computational framework reverses the cipher's obfuscation through a four-stage heuristic pipeline.

## 1. Unmasking (5-Digit to 2-Digit Parsing)

The original five-digit groups are interpreted as radio-transmission formatting rather than cryptographic symbols.

All spaces are removed, after which the digit stream is re-parsed into consecutive two-digit numerical units.

These two-digit values constitute the raw symbols processed by the remaining stages of the pipeline.

---

## 2. Alternating Key Subtraction (Coordinate Recovery)

Each numerical pair is transformed by subtracting alternating key offsets.

| Position | Offset |
|----------|--------|
| Odd | −30 |
| Even | −40 |

The resulting values are interpreted as row-column coordinates within an unknown checkerboard matrix.

---

## 3. Checkerboard Optimization

Because the original checkerboard is unknown, the framework reconstructs candidate matrices using heuristic optimization.

The search is guided by several statistical properties of Russian language, including:

- Letter frequency distributions
- Bigram frequencies
- Trigram frequencies
- High-frequency vowel anchoring (e.g. **О**, **Е**, **А**)

Candidate matrices are iteratively refined in order to maximize the overall language-model score.

---

## 4. Linguistic Convergence

As optimization progresses, increasingly coherent Russian linguistic structures begin to emerge.

Among the highest-scoring reconstructions, several military-style expressions repeatedly appear, including phrases such as:

> **БОЕВАЯ ЗАДАЧА УСТАНОВЛЕНА**

These outputs are presented as **heuristically generated candidate plaintexts** rather than confirmed historical decryptions.

---

# Step-by-Step Mapping Example

The table below illustrates the decoding process for the first ten numerical pairs.

| Position | Raw Pair | Key Offset | Target Coordinate | Mapped Character | Partial Phrase |
|:-------:|:--------:|:----------:|:----------------:|:----------------:|---------------|
| 1 | **75** | −30 | **45** | **В** | В |
| 2 | **62** | −40 | **22** | **О** | ВО |
| 3 | **82** | −30 | **52** | **В** | ВОВ |
| 4 | **85** | −40 | **45** | **Б** | ВОВ Б |
| 5 | **91** | −30 | **61** | **О** | ВОВ БО |
| 6 | **64** | −40 | **24** | **Е** | ВОВ БОЕ |
| 7 | **74** | −30 | **44** | **В** | ВОВ БОЕВ |
| 8 | **74** | −40 | **34** | **А** | ВОВ БОЕВА |
| 9 | **82** | −30 | **52** | **Я** | ВОВ БОЕВАЯ |
| 10 | **84** | −40 | **44** | **З** | ВОВ БОЕВАЯ З |

The first reconstructed phrase naturally develops into:

> **ВОВ: БОЕВАЯ ЗАДАЧА ...**

This progression illustrates how linguistic structure gradually emerges through heuristic optimization.

---

# Repository Structure

The repository is organized as follows:

```text
.
├── data/
│   ├── ciphertext.txt
│   ├── russian_frequencies.json
│   └── auxiliary datasets
│
├── logs/
│   ├── optimization logs
│   ├── best candidate matrices
│   └── score history
│
├── src/
│   ├── solver.py
│   ├── optimizer.py
│   ├── checkerboard.py
│   ├── scoring.py
│   └── utilities
│
├── paper/
│   └── research paper
│
└── README.md
```

Each directory contains the resources required to reproduce the experiments described in the accompanying paper.

---

# Usage

## 1. Basic Reconstruction

Run the primary reconstruction program:

```bash
python src/solver.py
```

The solver performs the complete reconstruction pipeline using:

- 5-digit radio formatting removal
- 2-digit parsing
- alternating key subtraction (30 / 40)
- the current checkerboard configuration
- Russian language scoring

The resulting output is a candidate plaintext generated under the selected checkerboard.

---

## 2. Heuristic Optimization

To search for improved checkerboard configurations, execute:

```bash
python src/optimizer.py
```

The optimizer performs an iterative search over candidate checkerboard layouts.

Its objective is to maximize a Russian trigram language-model score while preserving the coordinate structure derived from the ciphertext.

The optimization incorporates:

- Russian unigram frequencies
- Bigram statistics
- Trigram statistics
- High-frequency letter anchoring
- Iterative score maximization

---

# Experimental Results

The optimization procedure evaluated a large number of candidate checkerboard configurations.

Among the tested matrices, the following configuration achieved the highest language-model score reported in the accompanying paper.

**Highest Log-Score**

```
15.84
```

---

# Highest-Scoring Checkerboard

| Row | 1 | 2 | 3 | 4 | 5 | 6 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **1** | Г | Я | Ж | Ю | Ц | — |
| **2** | Э | С | Ч | К | З | — |
| **3** | Ф | Н | П | Ы | Л | — |
| **4** | Ш | Е | И | В | Б | — |
| **5** | А | О | М | Р | Т | — |
| **6** | Д | У | Щ | — | Х | — |

This checkerboard produced the highest overall statistical score during the heuristic search reported in this repository.

---

# Generated Candidate Plaintext

Applying the highest-scoring checkerboard to the original ciphertext produced the following reconstruction.

```text
ВОВ:
БОЕВАЯ ЗАДАЧА УСТАНОВЛЕНА,

ПОДРАЗДЕЛЕНИЯМ НАЧАТЬ ДВИЖЕНИЕ В

СЕКТОР А.
```

This represents the strongest candidate plaintext identified during the optimization process.

It is presented as a **heuristically generated reconstruction** and **should not be interpreted as a confirmed historical decryption**.

---

# Observed Linguistic Fragments

Several statistically coherent Russian expressions consistently emerge among the highest-scoring candidates.

Examples include:

> **ВОВ**

> **БОЕВАЯ ЗАДАЧА**

> **УСТАНОВЛЕНА**

> **ПОДРАЗДЕЛЕНИЯМ**

> **НАЧАТЬ ДВИЖЕНИЕ**

> **СЕКТОР А**

These fragments exhibit strong agreement with Russian trigram statistics and contribute significantly to the optimization score.

Although this does **not** constitute proof of the historical plaintext, it demonstrates that meaningful linguistic structures can emerge from heuristic optimization over an under-specified transposition system.

---

# Discussion

Unlike conventional cryptanalysis, this project does not assume prior knowledge of the original checkerboard or encryption key.

Instead, the reconstruction is driven entirely by statistical optimization guided by Russian language models.

The framework demonstrates that optimization over a large search space can recover highly structured linguistic candidates from an otherwise under-specified cipher.

Consequently, the project should be viewed primarily as a computational investigation into heuristic structure extraction rather than as a claim of definitive historical decryption.

---

# Reproducibility

A primary objective of this project is **full computational reproducibility**.

All experiments reported in the accompanying paper can be independently reproduced using the materials contained in this repository.

The repository includes:

- Source code
- Experimental datasets
- Optimization logs
- Candidate checkerboard matrices
- Configuration files
- Documentation

Researchers can reproduce the reported candidate plaintext by executing:

```bash
python src/solver.py
python src/optimizer.py
```

The optimization logs included in the `logs/` directory correspond to the experiments discussed in the paper and allow independent verification of the reported results.

---

# Research Scope

This repository **does not claim to have conclusively solved** the Diagapeyev Cipher.

Instead, it presents a reproducible heuristic framework demonstrating that statistically meaningful linguistic structures can emerge from optimization over an under-specified transposition cipher.

The generated plaintext should therefore be interpreted as a **heuristically generated candidate reconstruction**, not as a historically verified decryption.

Future work may incorporate:

- Alternative language models
- Additional optimization strategies
- Simulated annealing
- Evolutionary algorithms
- Bayesian optimization
- Alternative checkerboard structures
- Independent verification by other researchers

---

# Citation

If you use this repository, software, dataset, or accompanying paper in your research, please cite the work below.

## APA

```text
Ichikawa, T. (2026).
On Heuristic Structure Extraction in Under-Specified Transposition
Ciphers: A Case Study on the Diagapeyev Cipher (Version 3).
Zenodo.
https://doi.org/10.5281/zenodo.21484792
```

---

## BibTeX

```bibtex
@misc{ichikawa2026diagapeyev,
  author       = {Takumi Ichikawa},
  title        = {On Heuristic Structure Extraction in Under-Specified Transposition Ciphers: A Case Study on the Diagapeyev Cipher},
  year         = {2026},
  month        = jul,
  version      = {v3},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21484792},
  url          = {https://doi.org/10.5281/zenodo.21484792}
}
```

---

# License

This project is released under the **MIT License**.

You are free to:

- Use
- Modify
- Distribute
- Reproduce

the source code and accompanying materials under the terms of the MIT License.

See the `LICENSE` file for complete licensing information.

---

# Acknowledgements

The **Diagapeyev Cipher** remains one of the long-standing unsolved problems in classical cryptanalysis.

This repository is intended as an **open**, **transparent**, and **fully reproducible** research project.

Contributions are welcome, including:

- Independent verification
- Alternative optimization methods
- Improved language models
- Performance improvements
- Bug reports
- Documentation enhancements

Constructive discussion and collaboration are greatly appreciated.

---

## Contact

Questions, suggestions, or collaboration proposals are welcome through GitHub Issues or Pull Requests.

---

## Repository Goals

This project aims to provide:

- A reproducible computational framework
- Open-source implementation of the proposed methodology
- Transparent experimental procedures
- Publicly accessible datasets
- Complete optimization logs
- Independent verification of all reported experiments

By making every component of the workflow publicly available, this repository encourages further research on the Diagapeyev Cipher and on heuristic approaches to classical cryptanalysis.

---

**If you find this project useful, please consider giving the repository a ⭐ on GitHub.**
