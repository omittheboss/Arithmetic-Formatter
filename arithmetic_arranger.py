def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = {"top": [], "bottom": [], "line": [], "answer": []}
    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        arranged_problems["top"].append(num1.rjust(width))
        arranged_problems["bottom"].append(operator + " " + num2.rjust(width - 2))
        arranged_problems["line"].append('-' * width)

        if show_answers:
            result = str(eval(problem))
            arranged_problems["answer"].append(result.rjust(width))

    arranged_format = "\n".join([
        "    ".join(arranged_problems["top"]),
        "    ".join(arranged_problems["bottom"]),
        "    ".join(arranged_problems["line"])
    ])

    if show_answers:
        arranged_format += "\n" + "    ".join(["    ".join(arranged_problems["answer"])])

    return arranged_format
