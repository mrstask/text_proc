import re
from typing import Dict, List, Tuple

def extract_equations(input_string: str) -> List[str]:
    """
    Extract all equations from the input string.

    Args:
        input_string: The string to search for equations.

    Returns:
        A list of equations found in the string.
    """
    input_string = input_string.replace("–", "-")
    equation_pattern = r"^[\w\d.+*\/\-= ()]+"
    matches = re.finditer(equation_pattern, input_string, re.MULTILINE)
    return [match.group().strip() for match in matches if match.group().strip()]


def extract_target_variable(input_string: str) -> str:
    """
    Extract the target variable from the input string.

    Args:
        input_string: The string to search for the target variable.

    Returns:
        The target variable found in the string.
    """
    matches = re.finditer(r"\?([A-Z]+)", input_string, re.MULTILINE)
    return [match.groups() for match in matches][0][0]


def evaluate_expression(equations: Dict[str, str], target_variable: str) -> float:
    """
    Evaluate the expression for the target variable.

    Args:
        equations: A dictionary of equations.
        target_variable: The variable to evaluate.

    Returns:
        The evaluated result of the expression.
    """
    target_expression = equations[target_variable]
    while not target_expression.isnumeric():
        try:
            return eval(target_expression)
        except NameError as e:
            target_expression = handle_name_error(e.name, target_expression, equations)


def handle_name_error(missing_var: str, equation: str, equations: Dict[str, str]) -> str:
    """
    Handle a NameError exception by replacing the missing variable in the equation.

    Args:
        missing_var: The missing variable.
        equation: The equation.
        equations: A dictionary of equations.

    Returns:
        The equation with the missing variable replaced.
    """
    return equation.replace(missing_var, equations[missing_var])


def parse_equation(equation_string: str) -> Tuple[str, str]:
    """
    Parse the equation string into a variable and an expression.

    Args:
        equation_string: The string to parse.

    Returns:
        A tuple of the variable and the expression.
    """
    regex = re.compile(r"^(.*?)=(.*)$")
    match = regex.match(equation_string)
    return match.group(1).strip(), match.group(2).strip()


def create_equation_dictionary(equations: List[str]) -> Dict[str, str]:
    """
    Create a dictionary with the variable as the key and the equation as the value.

    Args:
        equations: A list of equations.

    Returns:
        A dictionary with the variable as the key and the equation as the value.
    """
    equation_dict = {}
    for equation in equations:
        variable, expression = parse_equation(equation)
        equation_dict[variable] = expression
    return equation_dict


if __name__ == "__main__":
    input_lines = """
    X = 5 * 6 + B * (C + D);
    C = 3.2 - D;
    D = S + 8;
    B = S;
    S = 18;
    ?X
    """
    equations = extract_equations(input_lines)
    target_variable = extract_target_variable(input_lines)
    equations = create_equation_dictionary(equations)
    print(evaluate_expression(equations, target_variable))
