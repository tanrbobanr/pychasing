"""Models used by ``client``.

:copyright: (c) 2022-present Tanner B. Corcoran
:license: MIT, see LICENSE for more details.
"""

__author__ = "Tanner B. Corcoran"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2022-present Tanner B. Corcoran"


import io


class Date(str):
    """A string that is formatted as an RFC3339 datetime upon instantiation.

    """
    def __init__(self, year: int, month: int, day: int, hour: int = ...,
        minute: int = ..., second: int = ...) -> None:
        """
        Arguments
        ---------
        year : int
        month : int
        day : int
        hour : int, optional, default=0
        minute : int, optional, default=0
        second : int, optional, default=0

        """
    def __new__(cls: "Date", year: int, month: int, day: int, hour: int = ...,
                minute: int = ..., second: int = ...) -> "Date":
        return (f"{year}-{month:02}-{day:02}T{hour!=... and hour or 0:02}:"
                f"{minute != ... and minute or 0:02}:"
                f"{second != ... and second or 0:02}Z")


class ReplayBuffer(io.BufferedReader):
    """An object that can be used to store a replay file in-memory before uploading.

    """
    def __init__(self, name: str, raw: bytes = ..., buffer_size: int = ...) -> None:
        self._name = name
        if raw == ...:
            self._buffer = io.BytesIO()
        else:
            self._buffer = io.BytesIO(raw)
        if buffer_size == ...:
            super().__init__(self._buffer)
        else:
            super().__init__(self._buffer, buffer_size)

    @property
    def name(self) -> str:
        return self._name
