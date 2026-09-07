import pytest
from grades import letter_grade


def test_boundary_a_grade():
    assert letter_grade(80) == "A"
#why not test with 85 is that, the boundary is 80, so we want to test the boundary value itself, not a value above it. Testing the boundary value ensures that the function correctly handles the edge case.
    assert letter_grade(79) == "B"
    
def test_boundary_pass_fail():
    assert letter_grade(60) == "C" #lowest pass
    assert letter_grade(59) == "F" #just failed
    
def test_minmal_valid():
    assert letter_grade(0) == "F"

def test_maximum_valid():
    assert letter_grade(100) == "A"
    
def test_below_minimal_invalid():
    with pytest.raises(ValueError):
        letter_grade(-1)
        
