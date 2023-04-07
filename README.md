# nullable
Typed Null support

```py
import typing as t
from dataclasses import dataclass

from nullable import Null, NullType, Nullable, NullableNoneOr

# valid typehints:
val: int | NullType = Null
val: Nullable[int] = Null

val: int | None | NullType = Null
val: NullableNoneOr[int] = Null

# example usage:
@dataclass
class Settings:
    is_cool: bool
    countdown: t.Optional[int]

    def alter(
        self,
        *,
        is_cool: Nullable[bool] = Null,
        countdown: NullableNoneOr[int] = Null,
    ) -> None:
        if is_cool is not Null:
            self.is_cool = is_cool
        if countdown is not Null:
            self.countdown = countdown
```
