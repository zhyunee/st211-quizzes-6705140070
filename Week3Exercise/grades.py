def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0-100.")
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    return "F"

print(letter_grade(85))  # Output: A
print(letter_grade(75))  # Output: B
print(letter_grade(65))  # Output: C
print(letter_grade(50))  # Output: F
