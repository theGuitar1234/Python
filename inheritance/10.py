#DTO, Record, Projection, Struct, Mapper in Python -> Dataclass
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class EmployeeDTO:
    name: str
    dept: str
    salary: float

    list: List[str]
    optional: Optional[int]

employeeDTO = EmployeeDTO('John', 'computer Lab', 100.2)
print(employeeDTO.dept)

#These are some Python 3.13 stuff

def func(x: int) -> int:
    return x
print(func(3))
print(func("hello"))