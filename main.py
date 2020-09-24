import argparse
from itertools import product

# Define constants.
SUDOKU_CAGE_SIDE = 3
SUDOKU_SIDE = 9
SUDOKU_LENGTH = SUDOKU_SIDE * SUDOKU_SIDE

VALID_STR_DIGITS = [str(i) for i in range(1, SUDOKU_SIDE + 1)]


def swap_character(string, c, i):
    """Given a string, a character c, and an index i, replace the character at index i
    in the string with c."""
    return string[:i] + c + string[i + 1 :]


def clean_string(string):
    """Clean a string by stripping all non-digit or non-space characters, and either
    right-padding it or trimming it."""
    allowed_characters = set(VALID_STR_DIGITS + [" "])  # 1-9 and [space].
    return "".join(c for c in string if c in allowed_characters).ljust(
        SUDOKU_LENGTH, " "
    )[:SUDOKU_LENGTH]


def pretty_print(string):
    """Prettyprint a sudoku string."""
    string = clean_string(string)
    line_fill = "\n║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n"
    line_top = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    line_separator_small = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    line_separator_big = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    line_bottom = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"
    print(
        line_fill.join(
            [
                line_top,
                line_separator_small,
                line_separator_small,
                line_separator_big,
                line_separator_small,
                line_separator_small,
                line_separator_big,
                line_separator_small,
                line_separator_small,
                line_bottom,
            ]
        ).format(*string)
    )


def check_digit_duplicate(iterable):
    """Given an iterable of either digits or spaces, return True if it contains no
    duplicated digits. Return False otherwise."""
    iterable = [i for i in iterable if i != " "]
    return len(iterable) == len(set(iterable))


def get_row(string, index):
    """Given a cleaned sudoku string and an index, return the row containing that index.
    The index is 0-indexed."""
    start = index // SUDOKU_SIDE * SUDOKU_SIDE  # index of the left element in row.
    end = start + SUDOKU_SIDE
    return (string[i] for i in range(start, end))


def get_column(string, index):
    """Given a cleaned sudoku string and an index, return the column containing that
    index. The index is 0-indexed."""
    remainder = index % SUDOKU_SIDE
    return (string[SUDOKU_SIDE * i + remainder] for i in range(SUDOKU_SIDE))


def get_cage(string, index):
    """Given a cleaned sudoku string and an index, return the cage containing that
    index. The index is 0-indexed."""
    cage_row = index // SUDOKU_SIDE // SUDOKU_CAGE_SIDE
    cage_col = index % SUDOKU_SIDE // SUDOKU_CAGE_SIDE
    start = (cage_row * SUDOKU_CAGE_SIDE * SUDOKU_SIDE) + (cage_col * SUDOKU_CAGE_SIDE)
    offsets = (
        i + SUDOKU_SIDE * j
        for i, j in product(range(SUDOKU_CAGE_SIDE), range(SUDOKU_CAGE_SIDE))
    )
    return (string[start + offset] for offset in offsets)


def check_index(string, index):
    """Given a sudoku string and an index, return if the row, column, or cage containing
    that index is free of any constraint violations. The index is 0-indexed."""
    string = clean_string(string)
    return (
        check_digit_duplicate(get_row(string, index))
        and check_digit_duplicate(get_column(string, index))
        and check_digit_duplicate(get_cage(string, index))
    )


def solve(string):
    """Given a sudoku string, attempt to find a solution. Return a solution if found,
    otherwise return None."""
    string = clean_string(string)
    solution = solve_recursive(string, 0)
    if solution:
        return solution
    else:
        return None


def solve_recursive(string, index):
    """Given a partial sudoku string and an index to start working from, attempt to find
    a solution. Works recursively."""

    # Termination case. If we get this far then row/column/cage constraints have held
    # up, thus we are done.
    if index == SUDOKU_LENGTH:
        return string

    # If there is already a number provided, move on to the next space.
    if string[index] != " ":
        return solve_recursive(string, index + 1)

    # Otherwise there is no number provided, so we should try our own. Recursively try
    # each digit that could go into it.
    for digit in VALID_STR_DIGITS:
        temp_string = swap_character(string, digit, index)
        if check_index(temp_string, index):
            potential_solution = solve_recursive(temp_string, index + 1)
            if potential_solution is not False:
                return potential_solution

    # If we have iterated through all of the digits and didn't get anything good back,
    # then there is no solution.
    return False


def main(string):
    pretty_print(string)
    solution = solve(string)
    if solution:
        pretty_print(solution)
    else:
        print("No solution found!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve a sudoku puzzle")
    parser.add_argument("string", type=str, help="Sudoku puzzle in string format")
    args = parser.parse_args()
    main(args.string)
