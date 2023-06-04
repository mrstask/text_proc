import re


def validate_string(string):
    """Validates that the string consists of uppercase letters, numbers, math operators, and the equals sign.

    Args:
      string: The string to validate.

    Returns:
      True if the string is valid, False otherwise.
    """

    regex = re.compile(r"^[A-Z0-9+*\/\-= ()]+$")
    return regex.fullmatch(string) is not None


if __name__ == "__main__":
    lines = """
    A = 5 * 6 + B * (C + D);
    C = 3.2 – D;
    D = S + 8;
    X = S;
    S = 18;
    ?X
    """
    for line in lines.split(';'):
        if validate_string(line.strip()):
            print(f"{line} The string is valid.")
        else:
            print(f"{line}The string is not valid.")
