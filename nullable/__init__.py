import enum
import typing as t

__all__ = ("Null", "NullType", "Nullable", "NullableNoneOr")


class NullType(enum.Enum):
    NULL = object()


T = t.TypeVar("T")

Null = NullType.NULL
Nullable = t.Union[NullType, T]
NullableNoneOr = t.Union[NullType, None, T]
