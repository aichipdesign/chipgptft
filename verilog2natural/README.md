# RTL Design Analysis and Mutation Tools

This repository provides scripts for analyzing and modifying HDL code.

## Scripts

### `funca_gen.py`

- **Function**: Analyzes partial functionality of RTL design.

- Usage

  ```python
  python funca_gen.py
  ```

### `mask_gen.py`

- **Function**: Generates new HDL code with random masks.

- Usage

  ```python
  python mask_gen.py
  ```

### `modify_gen.py`

- **Function**: Injects mutants into HDL code to create modified versions.

- Usage

  ```python
  python modify_gen.py
  ```

## Important Notes

- **HDL Code Path**: Update the HDL code path in each script.
- **Output JSON Path**: Set the path for output JSON files.
- **File Scope**: Define the range of files to be processed.

## Getting Started

1. Clone the repository.
2. Modify paths and parameters in the scripts.
3. Run the desired script.