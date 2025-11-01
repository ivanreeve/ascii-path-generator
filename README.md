# ASCII Path Generator
A Python script that generates an ASCII tree of folder structures.

## Features
- **Folder path**: Required argument to specify which directory to analyze
- **Include files**: Use `-f` or `--files` flag to include files in the output (defaults to folders only)
- **Depth control**: Use `-d` or `--depth` followed by a number to limit how many levels deep to traverse
- **Custom output**: Use `-o` or `--output` to specify output filename (defaults to `tree_output.txt`)

## Usage examples

```bash
# Basic usage - folders only
python script.py /path/to/folder

# Include files with depth limit of 2 levels
python script.py /path/to/folder -f -d 2

# Custom output file
python script.py /path/to/folder --files --depth 3 --output my_tree.txt
```

## Example output
```
Folder structure of: /home/user/folder1
[D] = Directory, [F] = File

[D] folder1
├── [D] folder1.2
│   ├── [D] subfolder
│   └── [F] file.txt
└── [D] folder1.3
    ├── [F] doc.pdf
    └── [F] image.png
```

The script uses tree-style ASCII characters (`├──`, `└──`, `│`) for a clean, readable output and saves everything to a text file for easy sharing or documentation.
