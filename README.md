# sudoku-brute-force

Simple sudoku brute forcer.

## Caveats

This solver uses brute force (essentially a DFS search across the state space of possible solutions) and no heuristics whatsoever, so cleverly constructed input can tie this program up for minutes to hours. See [here](https://www.flickr.com/photos/npcomplete/2361922699) for more information, as well as an example that is included in this repo under `sample/adversarial.txt`.

## Format

Sudoku puzzles are converted to a string by writing the digits and spaces in reading order; i.e., the first (top) row is written out from left to right, then the second row, and so forth until the last row. All characters that are not digits `1-9` or `[space]` are ignored. Thus separators such as newlines or pipes can be used for readability.

Ex. the puzzle:

```text
╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
║   │   │ 5 ║   │   │   ║ 1 │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 6 │ 1 ║   │   │   ║ 2 │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │   ║ 3 │ 8 │   ║   │   │   ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║   │ 2 │   ║   │   │   ║   │   │ 4 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │   ║   │ 3 │   ║   │   │ 9 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 1 │ 3 ║ 5 │   │   ║   │   │ 2 ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ 9 │   │   ║   │   │ 2 ║   │ 4 │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │   ║   │   │   ║   │ 7 │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 4 │   │   ║   │ 5 │ 9 ║   │   │ 3 ║
╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
```

can be written as:

```text
"  5   1  | 61   2  |   38    | 2      4|    3   9| 135    2|9    2 4 |       7 |4   59  3"
```

## Usage

### Command line

From the command line, call `main.py` and provide a string argument in the above format.

### Direct function call

Import as `from main import solve` and call `solve()` with a string argument in the above format.

## Example usage

```text
> python main.py "  5   1   61   2     38     2      4    3   9 135    29    2 4        7 4   59  3"
╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
║   │   │ 5 ║   │   │   ║ 1 │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 6 │ 1 ║   │   │   ║ 2 │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │   ║ 3 │ 8 │   ║   │   │   ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║   │ 2 │   ║   │   │   ║   │   │ 4 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │   ║   │ 3 │   ║   │   │ 9 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 1 │ 3 ║ 5 │   │   ║   │   │ 2 ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ 9 │   │   ║   │   │ 2 ║   │ 4 │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │   ║   │   │   ║   │ 7 │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 4 │   │   ║   │ 5 │ 9 ║   │   │ 3 ║
╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
║ 8 │ 4 │ 5 ║ 9 │ 2 │ 6 ║ 1 │ 3 │ 7 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 3 │ 6 │ 1 ║ 4 │ 7 │ 5 ║ 2 │ 9 │ 8 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 2 │ 9 │ 7 ║ 3 │ 8 │ 1 ║ 4 │ 6 │ 5 ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ 7 │ 2 │ 9 ║ 6 │ 1 │ 8 ║ 3 │ 5 │ 4 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 5 │ 8 │ 4 ║ 2 │ 3 │ 7 ║ 6 │ 1 │ 9 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 6 │ 1 │ 3 ║ 5 │ 9 │ 4 ║ 7 │ 8 │ 2 ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ 9 │ 3 │ 8 ║ 7 │ 6 │ 2 ║ 5 │ 4 │ 1 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 1 │ 5 │ 2 ║ 8 │ 4 │ 3 ║ 9 │ 7 │ 6 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 4 │ 7 │ 6 ║ 1 │ 5 │ 9 ║ 8 │ 2 │ 3 ║
╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
```
