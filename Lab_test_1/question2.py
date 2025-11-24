from typing import Sequence, Union
import inspect

def calc(a,b,c):
    # a is list, b is int, c bool
    r = 0
    for i in a: 
        if c:
            r = r + i*b
        else:
            r = r + i
    return r
    Number = Union[int, float]

    def calculate_total(values: Sequence[Number], multiplier: int = 1, apply_multiplier: bool = False) -> Number:
        """
        Compute the sum of a sequence of numbers.

        If apply_multiplier is True, each item is multiplied by `multiplier` before summing.

        Parameters
        - values: Sequence of int or float
        - multiplier: int multiplier applied to each value when apply_multiplier is True
        - apply_multiplier: whether to apply the multiplier to each value

        Returns
        - Sum of the (possibly multiplied) values

        Examples
        >>> calculate_total([1, 2, 3])
        6
        >>> calculate_total([1, 2, 3], multiplier=10, apply_multiplier=True)
        60
        """
        if not isinstance(multiplier, int):
            raise TypeError("multiplier must be an int")
        total: Number = 0
        for v in values:
            if not isinstance(v, (int, float)):
                raise TypeError("values must contain only int or float")
            total += v * multiplier if apply_multiplier else v
        return total

    def calc_compat(a, b, c):
        """
        Backwards-compatible wrapper matching the original calc(a, b, c) signature.

        Delegates to calculate_total while preserving behavior.
        """
        return calculate_total(a, multiplier=b, apply_multiplier=bool(c))

    def generate_docs() -> str:
        """
        Produce a simple, automatic textual documentation for all functions defined in this module.
        """
        docs = []
        for name, obj in globals().items():
            if inspect.isfunction(obj) and obj.__module__ == __name__:
                sig = inspect.signature(obj)
                doc = inspect.getdoc(obj) or ""
                docs.append(f"{name}{sig}\n{doc}")
        return "\n\n".join(docs)

    if __name__ == "__main__":
        # Basic smoke tests and documentation output
        assert calculate_total([1, 2, 3]) == 6
        assert calculate_total([1, 2, 3], multiplier=2, apply_multiplier=True) == 12
        assert calc_compat([1, 2, 3], 2, True) == 12
        print(generate_docs())