from __future__ import annotations

class Point:
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def __repr__(self) -> str:
        return self.__str__()

    def __gt__(self, other : Point) -> bool:
        return self.x > other.x and self.y > other.y

    def __ge__(self, other : Point) -> bool:
        return self.x >= other.x and self.y >= other.y

    def __lt__(self, other : Point) -> bool:
        return self.x < other.x and self.y < other.y

    def __le__(self, other : Point) -> bool:
        return self.x <= other.x and self.y <= other.y

    def __eq__(self, other : Point) -> bool:
        return (self.x, self.y) == (other.x, other.y)
