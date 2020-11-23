import ci_course

"""
Test the function `greet` in functionality.py
"""
def test_greet():
    assert ci_course.greet() == "Hello "
    assert ci_course.greet("Fergus") == "Hello Fergus"


"""
Test the function `minimum` in functionality.py
"""
def test_minimum():
    assert ci_course.minimum(1, 2, 3) == 1
    assert ci_course.minimum(1.2, 2.3) == 1.2
    assert ci_course.minimum(-1.2, -3) == -3
