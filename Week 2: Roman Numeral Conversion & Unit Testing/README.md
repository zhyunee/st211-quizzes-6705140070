# Week 2: Roman Numeral Conversion & Unit Testing

**Course:** 192-211 Automated Software Testing
**Student:** Phone pyae 6705140070

---

## Overview

This project implements a Roman numeral converter and validator in Python. The program provides two main conversion functions:

* `roman_to_integer` — converts a Roman numeral into a decimal integer.
* `integer_to_roman` — converts a decimal integer into a valid Roman numeral.

The project also includes an automated unit test suite using `pytest` to verify correct conversions, validation rules, boundary values, and error handling.

---

## Features & Validation Rules

The converter follows the standard rules of classical Roman numerals and supports values from **1 to 3999**.

### 1. Character Validity

The program accepts the standard Roman numeral characters:

`I`, `V`, `X`, `L`, `C`, `D`, and `M`.

Input is case-insensitive, so both uppercase and lowercase Roman numerals are supported.

### 2. Repetition Rules

* `V`, `L`, and `D` cannot be repeated.
* `I`, `X`, `C`, and `M` cannot appear more than three times consecutively.

For example:

* `III` → valid
* `IIII` → invalid
* `VV` → invalid

### 3. Subtractive Combinations

Only the standard subtractive combinations are accepted:

* `IV` → 4
* `IX` → 9
* `XL` → 40
* `XC` → 90
* `CD` → 400
* `CM` → 900

Other subtractive combinations are rejected as invalid.

### 4. Canonical Form Validation

After converting a Roman numeral to an integer, the program converts the integer back into its canonical Roman representation.

This prevents invalid or non-standard forms such as:

* `IIV`
* `IIX`
* `CMCC`
* `MCMC`

from being accepted.

### 5. Range Constraints

The converter supports integer values from:

**1 to 3999**

Values outside this range are rejected.

---

## Project Structure

```text
Week2RomanConversion/
├── roman.py          # Main implementation and interactive CLI
├── test_roman.py     # Automated unit tests using pytest
└── README.md         # Project documentation
```

---

## How to Run

### Prerequisites

The project requires:

* Python 3.8 or higher
* `pytest` for running the unit tests

Install `pytest` using:

```bash
pip install pytest
```

---

## Running the Interactive Program

Run `roman.py` from the project directory:

```bash
python roman.py
```

The program will ask the user to enter a Roman numeral and display its corresponding integer value.

### Example Usage

```text
Enter a Roman numeral: XIV
Integer: 14
Do you want to continue? (yes/no): yes

Enter a Roman numeral: mmxxvi
Integer: 2026
Do you want to continue? (yes/no): no

Goodbye!
```

---

## Running Unit Tests

The automated tests can be executed using `pytest`.

### Using pytest directly

```bash
pytest test_roman.py -v
```

### Using Python

```bash
python -m pytest test_roman.py -v
```

The test suite verifies:

* Standard Roman numeral conversions.
* Integer-to-Roman conversions.
* Boundary values such as `I = 1` and `MMMCMXCIX = 3999`.
* Lowercase Roman numeral input.
* Invalid characters.
* Empty input.
* Illegal repetitions.
* Invalid subtractive combinations.
* Non-canonical Roman numeral sequences.
* `ValueError` exception handling.
* Values outside the supported range.

---

## Testing

The unit tests are designed to verify both valid and invalid inputs. Positive test cases confirm that valid Roman numerals are converted correctly, while negative test cases ensure that invalid inputs raise the appropriate `ValueError` exception.

This provides confidence that the implementation follows the required Roman numeral rules and handles incorrect user input safely.

```

If you give me your **actual `roman.py` and `test_roman.py` files**, I can also make the README match your implementation exactly rather than assuming the functions and validation rules.

I can also make it look **more like a student GitHub assignment README**, including the instructor/collaborator information if that's what your Week 2 quiz requires.
```
