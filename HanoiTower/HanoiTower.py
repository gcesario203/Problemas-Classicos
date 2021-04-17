from typing import List, Generic, TypeVar
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs: int = 5
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1,num_discs+1):
    tower_a.push(i)


counter_plays: int = 0
def solve_hanoi(begin: Stack[int], end: Stack[int],temp: Stack[int], discs: int):
    if discs == 1:
        end.push(begin.pop())
    else:
        solve_hanoi(begin, temp, end, discs - 1)
        solve_hanoi(begin, end, temp, 1 )
        solve_hanoi(temp, end, begin, discs - 1)

solve_hanoi(tower_a,tower_c,tower_b, num_discs)

print(repr(tower_a))
print(repr(tower_b))
print(repr(tower_c))