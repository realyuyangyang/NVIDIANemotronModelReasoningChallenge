#!/usr/bin/env python3
'''Validate notebook structure and Python syntax without executing GPU code.'''

from __future__ import annotations

import ast
import sys
from pathlib import Path

import nbformat
from nbformat.validator import validate


def validate_notebook(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        notebook = nbformat.read(path, as_version=4)
        validate(notebook)
    except Exception as exc:  # noqa: BLE001
        return [f"{path}: invalid notebook structure: {exc}"]

    for index, cell in enumerate(notebook.cells):
        if cell.cell_type != "code" or not cell.source.strip():
            continue
        try:
            ast.parse(cell.source, filename=f"{path}:cell-{index}")
        except SyntaxError as exc:
            errors.append(f"{path}: code cell {index} has invalid Python syntax: {exc}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    notebooks = sorted((root / "notebooks").glob("*.ipynb"))
    if not notebooks:
        print("No notebooks found.", file=sys.stderr)
        return 1

    errors: list[str] = []
    for notebook in notebooks:
        notebook_errors = validate_notebook(notebook)
        errors.extend(notebook_errors)
        if not notebook_errors:
            print(f"OK: {notebook.relative_to(root)}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(notebooks)} notebooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
