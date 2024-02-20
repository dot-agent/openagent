# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

from nextpy.ai import engine


def test_subtract():
    """Basic test of `subtract`."""
    program = engine(
        """Write a number: {{set 'user_response' (subtract 20 variable)}}"""
    )
    assert program(variable=10)["user_response"] == 10
    assert abs(program(variable=20.1)["user_response"] + 0.1) < 1e-5


def test_subtract_infix():
    program = engine("""Write a number: {{set 'user_response' (20 - variable)}}""")
    assert program(variable=10)["user_response"] == 10
    assert abs(program(variable=20.1)["user_response"] + 0.1) < 1e-5
