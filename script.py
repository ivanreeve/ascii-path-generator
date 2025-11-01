import os
import argparse
from pathlib import Path


def build_tree(path, prefix="", include_files=False, max_depth=None, current_depth=0):
    """
    Recursively build ASCII tree structure of folders and optionally files.
    
    Args:
        path: Root directory path
        prefix: Current prefix for tree lines
        include_files: Whether to include files in output
        max_depth: Maximum depth to traverse (None = unlimited)
        current_depth: Current recursion depth
    
    Returns:
        List of formatted strings representing the tree
    """
    lines = []
    
    # Check if we've reached max depth
    if max_depth is not None and current_depth >= max_depth:
        return lines
    
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        return lines
    
    # Separate folders and files
    folders = [item for item in items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]
    
    # Combine based on include_files option
    display_items = folders + (files if include_files else [])
    
    if not display_items:
        return lines
    
    for i, item in enumerate(display_items):
        is_last = i == len(display_items) - 1
        is_folder = os.path.isdir(os.path.join(path, item))
        
        # Determine connector
        connector = "└── " if is_last else "├── "
        extension = "    " if is_last else "│   "
        
        # Add folder/file marker
        marker = "[D] " if is_folder else "[F] "
        lines.append(f"{prefix}{connector}{marker}{item}")
        
        # Recursively process folders
        if is_folder:
            item_path = os.path.join(path, item)
            sub_lines = build_tree(
                item_path,
                prefix + extension,
                include_files,
                max_depth,
                current_depth + 1
            )
            lines.extend(sub_lines)
    
    return lines


def main():
    parser = argparse.ArgumentParser(
        description="Generate ASCII tree of folder structure"
    )
    parser.add_argument(
        "path",
        help="Path to the folder to analyze"
    )
    parser.add_argument(
        "-f", "--files",
        action="store_true",
        help="Include files in the output"
    )
    parser.add_argument(
        "-d", "--depth",
        type=int,
        default=None,
        help="Maximum depth to traverse (default: unlimited)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: tree_output.txt)"
    )
    
    args = parser.parse_args()
    
    # Validate path
    if not os.path.isdir(args.path):
        print(f"Error: '{args.path}' is not a valid directory")
        return
    
    # Set output filename
    output_file = args.output or "tree_output.txt"
    
    # Build tree
    print(f"Generating tree for: {args.path}")
    lines = [f"Folder structure of: {os.path.abspath(args.path)}"]
    lines.append(f"[D] = Directory, [F] = File")
    lines.append("")
    lines.append(f"[D] {os.path.basename(args.path)}")
    
    root_lines = build_tree(
        args.path,
        prefix="",
        include_files=args.files,
        max_depth=args.depth
    )
    lines.extend(root_lines)
    
    # Write to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print(f"✓ Tree saved to: {output_file}")
    print(f"✓ Total lines: {len(lines)}")


if __name__ == "__main__":
    main()
