# typing is a Python module that gives extra tools for type hints, especially for complex data types.
from typing import List, Dict, Tuple, Optional, Union
numbers: List[int] = [1, 2, 3]

student: Dict[str, int] = {
    "marks": 90
}

point: Tuple[int, int] = (10, 20)

def find_user(name: Optional[str]) -> None:
    print(name)

def process(data: Union[int, str]) -> None:
    print(data)

def square_all(nums: List[int]) -> List[int]:
    return [n * n for n in nums]