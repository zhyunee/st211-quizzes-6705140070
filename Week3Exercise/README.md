# Week 3: Unit Testing Best Practices & Boundary Value Analysis

**Course:** 192-211 Automated Software Testing
**Student:** Phone Pyae (6705140070)

---

## Overview

This repository contains the exercises and automated test suites for **Week 3** of the Automated Software Testing course.

The main focus of this week's exercises is to learn and demonstrate important unit testing practices in Python using `pytest`, including:

* **Focused Unit Testing**
* **Boundary Value Analysis (BVA)**
* **Equivalence Partitioning**
* **Test Independence**
* **Shared State and Test Dependencies**
* **Exception Testing using `pytest.raises`**

---

## Exercise Details & Concepts

### 1. Bank Account Operations (`bank.py` & `test_bank.py`)

The first exercise focuses on testing basic bank account operations.

#### Implementation (`bank.py`)

The `BankAccount` class provides:

* `deposit(amount)` — adds money to the account.
* `withdraw(amount)` — removes money from the account.

The implementation also validates invalid operations:

* Depositing a non-positive amount raises `ValueError`.
* Withdrawing more money than the available balance raises `ValueError`.

#### Testing Approach (`test_bank.py`)

The test suite demonstrates the difference between focused and overly broad tests.

Focused tests include:

* `test_deposit_increases_balance`
* `test_withdraw_decreases_balance`

Each test checks one specific behavior.

The exercise also includes `test_everything_at_once`, which demonstrates a less desirable testing approach where multiple operations are combined into one test. This can make it more difficult to identify which operation caused a failure.

---

### 2. Grade Classification & Boundary Value Analysis (`grades.py` & `test_grades.py`)

The second exercise focuses on grade classification and **Boundary Value Analysis (BVA)**.

#### Implementation (`grades.py`)

The `letter_grade(score)` function classifies scores as:

| Score  | Grade |
| ------ | ----- |
| 80–100 | A     |
| 70–79  | B     |
| 60–69  | C     |
| 0–59   | F     |

Scores outside the valid range of **0–100** raise a `ValueError`.

#### Testing Approach (`test_grades.py`)

The tests focus on important boundary values rather than only testing typical values.

Examples include:

* `80` → `A`
* `79` → `B`
* `60` → `C`
* `59` → `F`
* `0` → valid minimum
* `100` → valid maximum
* `-1` → invalid value

This demonstrates how Boundary Value Analysis can identify errors that may occur at or around decision boundaries.

---

### 3. Test Independence vs. Shared State

The third exercise demonstrates the difference between dependent and independent tests.

#### Dependent Tests (`test_dependent.py`)

The dependent test file uses a shared `BankAccount` object.

For example, one test may deposit money before another test attempts to withdraw it.

This creates **test dependency**, meaning the result of one test can depend on another test running first.

This is considered a testing anti-pattern because tests may fail when their execution order changes.

#### Independent Tests (`test_independent.py`)

The independent test file creates a new `BankAccount` instance for each test.

Each test therefore starts with a clean state.

This makes the tests:

* Independent
* Reproducible
* Easier to debug
* Safe to execute in different orders

---

## Project Structure

```text
Week3Exercise/
├── bank.py               # BankAccount class implementation
├── test_bank.py          # Unit tests for bank account operations
├── grades.py             # Grade classification implementation
├── test_grades.py        # Boundary value and exception tests
├── test_dependent.py     # Demonstration of dependent tests
├── test_independent.py   # Demonstration of independent tests
└── README.md             # Project documentation
```

---

## How to Run

### Prerequisites

The project requires:

* Python 3.8+
* `pytest`

Install `pytest` if it is not already installed:

```bash
pip install pytest
```

---

## Running the Programs

The Python programs can be run directly from the project directory:

```bash
python bank.py
```

```bash
python grades.py
```

---

## Running Unit Tests

To run all tests in the project:

```bash
python -m pytest -v
```

### Running Individual Test Suites

To test the bank account operations:

```bash
python -m pytest test_bank.py -v
```

To test the grade classification and boundary values:

```bash
python -m pytest test_grades.py -v
```

To test independent test cases:

```bash
python -m pytest test_independent.py -v
```

To demonstrate the dependent tests:

```bash
python -m pytest test_dependent.py -v
```

---

## Test Suite

The test suite demonstrates several important unit testing techniques.

### Unit Testing

The bank account tests verify that deposits and withdrawals correctly change the account balance.

### Boundary Value Analysis

The grade tests verify values around important boundaries such as:

```text
80 → A
79 → B

60 → C
59 → F

0   → valid
100 → valid
-1  → invalid
```

### Exception Testing

Invalid inputs are tested using `pytest.raises(ValueError)` to ensure that the program correctly rejects invalid values.

### Test Independence

The independent tests create their own objects instead of relying on shared state. This prevents one test from affecting another.

---

## Example Test Execution

A successful test run should produce output similar to:

```text
============================= test session starts =============================
collected 12 items

test_bank.py::test_deposit_increases_balance PASSED
test_bank.py::test_withdraw_decreases_balance PASSED
test_bank.py::test_everything_at_once PASSED
test_dependent.py::test_a_deposit PASSED
test_dependent.py::test_b_withdraw PASSED
test_grades.py::test_boundary_a_grade PASSED
test_grades.py::test_boundary_pass_fail PASSED
test_grades.py::test_minmal_valid PASSED
test_grades.py::test_maximum_valid PASSED
test_grades.py::test_below_minimal_invalid PASSED
test_independent.py::test_deposit_independent PASSED
test_independent.py::test_withdraw_independent PASSED

============================= 12 passed =============================
```

---

## Conclusion

This week's exercises demonstrate how well-designed unit tests can improve software quality and reliability.

The exercises show the importance of:

* Testing one behavior at a time.
* Testing values at important boundaries.
* Testing invalid inputs and exceptions.
* Avoiding shared state between test cases.
* Keeping tests independent and reproducible.

These practices help create unit test suites that are easier to maintain, understand, and debug.
