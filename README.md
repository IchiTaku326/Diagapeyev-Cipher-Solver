# Diagapeyev-Cipher-Solver

This repository contains the computational framework, source code, and experimental logs used in the following research paper.

## Paper Information
**Title**: On Heuristic Structure Extraction in Under-Specified Transposition Ciphers: A Case Study on the Diagapeyev Cipher  
**Author**: Takumi Ichikawa  
**DOI**: [10.5281/zenodo.21022129](https://doi.org/10.5281/zenodo.21022129)

## Project Overview
This project applies a heuristic optimization framework to the Diagapeyev Cipher, investigating structural extraction methods. This repository provides the necessary code and data to ensure the reproducibility of the study.

## Contents
- `/src`: Python source code used for decryption experiments.
- `/logs`: Decryption logs for each phase and matrix configurations corresponding to peak scores.
- `/data`: Cryptograms and datasets used in the experiments.

## Experimental Results (Highest Score)
The following 6x6 matrix yielded the highest log-score (15.84) observed during our heuristic search.

| Row | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Г | Я | Ж | Ю | Ц | - |
| 2 | Э | С | Ч | К | З | - |
| 3 | Ф | Н | П | Ы | Л | - |
| 4 | Ш | Е | И | В | Б | - |
| 5 | А | О | М | Р | Т | - |
| 6 | Д | У | Щ | - | Х | - |

## License
This repository is provided for research purposes to ensure the reproducibility and verification of the reported results.
