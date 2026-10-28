# PyTorch CUDA Example

A minimal PyTorch script that selects CUDA when it is available and otherwise
runs on the CPU. It prints the PyTorch version, selected device, and the result
of multiplying two small matrices.

## Requirements

- Python 3.9 or newer
- PyTorch

Install PyTorch using the instructions at <https://pytorch.org/get-started/locally/>
to choose a build compatible with your operating system and CUDA setup.

## Run

```bash
python torch_example.py
```