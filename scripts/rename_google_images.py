#!/usr/bin/env python3
"""
Rename files in the google_images directory to sequential numbers: 1.jpg, 2.png, ...
Usage: python scripts/rename_google_images.py [path]
If no path provided, defaults to ./google_images
"""
import sys
from pathlib import Path


def main(target_dir: Path):
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: {target_dir} does not exist or is not a directory")
        return 2

    # Collect files (skip classes.txt and any directories)
    files = [p for p in sorted(target_dir.iterdir()) if p.is_file() and p.name != 'classes.txt']
    if not files:
        print("No files to rename in", target_dir)
        return 0

    print(f"Found {len(files)} files in {target_dir}. Preparing to rename...")

    # First pass: rename to temporary names to avoid name collisions
    temp_mapping = []  # list of (temp_path, final_path)
    for idx, orig in enumerate(files, start=1):
        ext = orig.suffix.lower()  # include the dot
        temp_name = f".tmp_rename_{idx}{ext}"
        temp_path = target_dir / temp_name
        print(f"Temporarily renaming: {orig.name} -> {temp_path.name}")
        orig.rename(temp_path)
        final_path = target_dir / f"{idx}{ext}"
        temp_mapping.append((temp_path, final_path))

    # Second pass: move temps to final numeric names
    overwritten = 0
    for temp_path, final_path in temp_mapping:
        if final_path.exists():
            # If a final path already exists (unlikely because we used temps), remove it.
            print(f"Overwriting existing file: {final_path.name}")
            try:
                final_path.unlink()
                overwritten += 1
            except Exception as e:
                print(f"Failed to remove existing {final_path}: {e}")
                # attempt to skip
        print(f"Renaming: {temp_path.name} -> {final_path.name}")
        try:
            temp_path.rename(final_path)
        except Exception as e:
            print(f"Failed to rename {temp_path} -> {final_path}: {e}")

    print(f"Done. Renamed {len(temp_mapping)} files. Overwritten: {overwritten}")
    return 0


if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else ''
    target = Path(arg)
    code = main(target)
    sys.exit(code)
