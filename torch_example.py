"""A minimal PyTorch example that uses CUDA when available."""

import torch


def main() -> None:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"PyTorch: {torch.__version__}")
    print(f"Device: {device}")

    # Create two small matrices on the selected device and multiply them.
    a = torch.tensor([[1.0, 2.0], [3.0, 4.0]], device=device)
    b = torch.tensor([[5.0, 6.0], [7.0, 8.0]], device=device)
    result = a @ b

    print("A @ B:")
    print(result)
    print(f"Sum of result: {result.sum().item()}")


if __name__ == "__main__":
    main()
