"""Rate limiter for ``client``.

:copyright: (c) 2022-present Tanner B. Corcoran
:license: MIT, see LICENSE for more details.
"""

__author__ = "Tanner B. Corcoran"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2022-present Tanner B. Corcoran"


import collections
import datetime
import time


def rlim_burstonly(self: "RateLimit") -> None:
    current_dt = datetime.datetime.now().timestamp()
    print(current_dt - self.last)
    if (diff := current_dt - self.last) < self.burst_seconds:
        self.last = current_dt + (addl := self.burst_seconds - diff)
        time.sleep(addl)
        return
    self.last = current_dt


def rlim(self: "RateLimit") -> None:
    current_dt = datetime.datetime.now().timestamp()
    addl = 0
    if (diff := current_dt - self.stack[-1]) < self.burst_seconds:
        addl = self.burst_seconds - diff
    if (diff := current_dt - self.stack[0]) < self.max_seconds:
        addl = self.max_seconds - diff
    self.stack.append(current_dt + addl)
    if addl:
        time.sleep(addl)


class RateLimit:
    def __init__(self, burst_quota_per_second: int, max_quota: int = None,
                 max_seconds: int = None, *, safe_start: bool = False) -> None:
        self.burst_seconds = 1 / burst_quota_per_second
        if max_quota and max_seconds:
            self.max_quota = max_quota
            self.max_seconds = max_seconds
            if safe_start:
                t = datetime.datetime.now().timestamp()
                s = t - max_seconds
                a = max_seconds / max_quota
                stack = [s + a * i for i in range(max_quota)]
            else:
                stack = [0]
            self.stack = collections.deque(stack, max_quota)
            self.callfunc = rlim
        else:
            self.last = 0
            self.callfunc = rlim_burstonly
    
    def __call__(self) -> None:
        self.callfunc(self)
