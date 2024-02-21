from arithmetic_arranger import arithmetic_arranger

def test_arithmetic_arranger():
    # Test Case 1
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    show_answers = True
    result = arithmetic_arranger(problems, show_answers)
    expected_output = (
        "   32      3801      45      123\n"
        "+ 698    -    2    + 43    +  49\n"
        "-----    ------    ----    -----"
    )
    assert result == expected_output, f"Test Case 1 Failed: Expected {expected_output}, got {result}"

    # Test Case 2
    problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
    show_answers = True
    result = arithmetic_arranger(problems, show_answers)
    expected_output = (
        "  32         1      9999      523\n"
        "+  8    - 3801    + 9999    -  49\n"
        "----    ------    ------    -----"
    )
    assert result == expected_output, f"Test Case 2 Failed: Expected {expected_output}, got {result}"

    # Test Case 3
    problems = ["12 + 345", "678 - 9", "87 + 6543", "21 - 8765"]
    show_answers = True  # Lets check the outputs for now
    result = arithmetic_arranger(problems, show_answers)
    expected_output = (
        "  12      678      87      21\n"
        "+345    -   9    +6543    -8765\n"
        "----    ------    -----    -----"
    )
    assert result == expected_output, f"Test Case 3 Failed: Expected {expected_output}, got {result}"

    # Test Case 4
    problems = ["1234 + 5678", "8765 - 4321", "987 + 654", "321 - 999"]
    show_answers = True
    result = arithmetic_arranger(problems, show_answers)
    expected_output = (
        " 1234      8765      987      321\n"
        "+5678    -4321    + 654    -999\n"
        "-----    ------    ----    -----"
    )
    assert result == expected_output, f"Test Case 4 Failed: Expected {expected_output}, got {result}"

    # Add more test cases if needed
