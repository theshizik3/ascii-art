# ASCII Converter

Turn images into monochrome ASCII art from the command line — print the result to your terminal or save it as a text file.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run from the project root:

```bash
python3 -m src /path/to/image --width 40
```

Customize the character set and save the result:

```bash
python3 -m src /path/to/image \\
  --width 40 \\
  --chars '@%#*+=-:. ' \\
  --charw 1 \\
  --output /path/to/output
```

Available options: `--width`, `--height`, `--charw`, `--chars`, and `--output`.

> By default, output is printed to the terminal and `--charw` is `2`.

## License

[MIT](LICENSE) © 2026 Gorozhankin Andrey
