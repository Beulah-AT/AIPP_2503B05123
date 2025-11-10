import argparse
import sys
import time

#!/usr/bin/env python3
"""
factorial_cli.py

Contains both recursive and iterative implementations of factorial
and a small CLI to test them.
"""



def factorial_recursive(n: int) -> int:
    """Recursive factorial. Raises RecursionError for too deep recursion."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """Iterative factorial (safe for large n within memory/time limits)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Compute factorial (recursive or iterative).")
    p.add_argument("n", type=int, help="non-negative integer")
    p.add_argument(
        "-m",
        "--method",
        choices=("iterative", "recursive", "both"),
        default="both",
        help="which implementation to run (default: both)",
    )
    p.add_argument(
        "-t",
        "--time",
        action="store_true",
        help="display execution time for each method",
    )
    return p.parse_args(argv)


def run_method(name: str, func, n: int, show_time: bool):
    try:
        if show_time:
            t0 = time.perf_counter()
            res = func(n)
            t1 = time.perf_counter()
            print(f"{name}: {res}")
            print(f"{name} time: {(t1 - t0):.6f} sec")
        else:
            print(f"{name}: {func(n)}")
    except RecursionError:
        print(f"{name}: RecursionError (stack too deep for n={n})")
    except Exception as e:
        print(f"{name}: error: {e}")


def main(argv=None):
    args = parse_args(argv)
    n = args.n
    if n < 0:
        print("Error: n must be non-negative", file=sys.stderr)
        return 2

    if args.method in ("iterative", "both"):
        run_method("Iterative", factorial_iterative, n, args.time)

    if args.method in ("recursive", "both"):
        run_method("Recursive", factorial_recursive, n, args.time)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())