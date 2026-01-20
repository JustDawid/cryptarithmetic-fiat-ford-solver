# Cryptarithmetic Solver: FIAT + FORD = AUTA

## Overview
This project is a Python-based solver for a classic **Cryptarithmetic (Verbal Arithmetic)** puzzle.
The goal is to replace letters with digits to satisfy the following mathematical equation:

$$FIAT + FORD = AUTA$$

The script uses a brute-force approach with permutations to find the unique mapping of letters to digits.

## The Rules
1.  **Unique Digits:** Each letter corresponds to a unique digit from the range **1 to 8**.
2.  **Equation:** The sum of the words must be mathematically correct.
3.  **Constraint:** The puzzle includes a specific condition implemented in the code: $R = 2 \times I$.

## How it Works
The script utilizes the `itertools.permutations` library to generate all possible combinations of assigning digits to the letters: F, I, A, T, O, R, U, D.

1.  **Permutation Generation:** Iterates through all permutations of digits 1-8.
2.  **Optimization:** Early rejection of permutations that do not satisfy the condition $R = 2 \times I$.
3.  **Validation:** Calculates the numeric value of words `FIAT`, `FORD`, and `AUTA` and checks if the addition holds true.
4.  **Decoding:** Once the solution is found, the script uses a specific key `[7, 1, 2, 4]` to decode a hidden word based on the solved digit mapping.

## Usage
### Prerequisites
* Python 3.x

### Running the script
```bash
python main.py
