## 📝 Explanatory Article
For a high-level conceptual overview, methodology breakdown, and visualization of the heuristic search process, check out the official explanatory article on Medium:

👉 **[Decrypting the Diagapeyev Cipher: A Heuristic Approach to Under-Specified Transposition](https://medium.com/@takumiichikawa3126/the-diagapeyev-cipher-has-remained-an-unresolved-cryptographic-puzzle-for-over-eight-decades-7dd805764b8e)**

# Diagapeyev-Cipher-Solver
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21022129.svg)](https://doi.org/10.5281/zenodo.21022129)

This repository contains the computational framework, source code, and experimental logs used in the following research paper.

## Paper Information

**Title**: On Heuristic Structure Extraction in Under-Specified Transposition Ciphers: A Case Study on the Diagapeyev Cipher
**Author**: Takumi Ichikawa
**DOI**: [10.5281/zenodo.21022129](https://doi.org/10.5281/zenodo.21022129)

## Project Overview

This project applies a heuristic optimization framework to the Diagapeyev Cipher, investigating structural extraction methods. This repository provides the necessary code and data to ensure the reproducibility of the study.

## Contents

```text
.
├── src/      # Python source code used for decryption experiments
├── logs/     # Decryption logs for each phase and matrix configurations corresponding to peak scores
└── data/     # Cryptograms and datasets used in the experiments
```

## Usage

### 1. Basic Decryption

To run the decryption script and verify the primary decryption structure:

```bash
python src/solver.py
```

This script implements the decryption logic using a 6×6 Straddling Checkerboard, utilizing a cycle of keys (30, 40) to extract the underlying structure.

### 2. Heuristic Search

To run the optimization framework used to derive the optimal matrix:

```bash
python src/optimizer.py
```

This script performs a heuristic search by anchoring high-frequency characters in the 6×6 matrix and maximizing the score based on the target language's linguistic structure.

## Experimental Results (Highest Score)

The following 6×6 matrix yielded the highest log-score (15.84) observed during our heuristic search.

| Row |  1  |  2  |  3  |  4  |  5  |  6  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|  1  |  Г  |  Я  |  Ж  |  Ю  |  Ц  |  -  |
|  2  |  Э  |  С  |  Ч  |  К  |  З  |  -  |
|  3  |  Ф  |  Н  |  П  |  Ы  |  Л  |  -  |
|  4  |  Ш  |  Е  |  И  |  В  |  Б  |  -  |
|  5  |  А  |  О  |  М  |  Р  |  Т  |  -  |
|  6  |  Д  |  У  |  Щ  |  -  |  Х  |  -  |

## Sample Output: Observed Linguistic Fragments

By applying the optimal 6x6 matrix configuration shown above, our post-processing framework yields the following candidate fragments:

```text
ВОВ: БОЕВАЯ ЗАДАЧА УСТАНОВЛЕНА, П
ОДРАЗДЕЛЕНИЯМ НАЧАТЬ ДВИЖЕНИЕ В
СЕКТОР А.

These fragments show high linguistic coherence based on our trigram model. Please note that these should be interpreted as structural patterns emergent from the heuristic scoring function, rather than definitive historical plaintext. Researchers are encouraged to verify these outputs by running the `src/solver.py` script provided in this repository.

## License

This repository is provided for research purposes to ensure the reproducibility and verification of the reported results.

How to Cite
If you use this research or code in your work, please cite it as follows:

Ichikawa, T. (2026). On Heuristic Structure Extraction in Under-Specified Transposition Ciphers: A Case Study on the Diagapeyev Cipher [Data set]. Zenodo. https://doi.org/10.5281/zenodo.21022129
