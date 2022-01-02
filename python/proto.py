from abc import abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class Proto(Protocol):
    member: int

    @property
    @abstractmethod
    def prop(self) -> int:
        ...


class A(Proto):
    @property
    def member(self) -> int:
        return 42

    @property
    def prop(self) -> int:
        return 65


class B(Proto):
    member = 18

    prop = 32


# C is an abstract class!!
# Python cannot find the definition of prop in class's definition!
class C(Proto):
    def __init__(self, mem: int, prop: int) -> None:
        self.member = mem
        self.prop = prop


def pt(p: Proto) -> None:
    print(p.member, p.prop)


print(isinstance(A(), A))
pt(A())
print(isinstance(B(), B))
pt(B())
print(isinstance(C(), C))
pt(C())
