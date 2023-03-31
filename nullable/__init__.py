import enum
import typing as t

__all__ = ("Null", "Nullable", "NullableNoeOr")


class _NullType(enum.Enum):
    NULL = object()


T = t.TypeVar("T")

Null = _NullType.NULL
Nullable = t.Union[_NullType, T]
NullableNoneOr = t.Union[_NullType, None, T]
