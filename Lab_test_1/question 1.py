from typing import Generic, TypeVar, List, Optional, Iterator

T = TypeVar("T")

class Stack(Generic[T]):
    """Simple LIFO stack implementation."""

    def __init__(self, items: Optional[Iterator[T]] = None) -> None:
        self._data: List[T] = []
        if items is not None:
            for item in items:
                self.push(item)

    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self._data.append(item)

    def pop(self) -> T:
        """Remove and return the top item. Raises IndexError if empty."""
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> T:
        """Return the top item without removing it. Raises IndexError if empty."""
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data

    def size(self) -> int:
        return len(self._data)

    def clear(self) -> None:
        self._data.clear()

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data!r})"


# Example usage:
# s = Stack[int]()
# s.push(1)
# s.push(2)
# print(s.peek())  # 2
# print(s.pop())   # 2
# print(s.pop())   # 1
