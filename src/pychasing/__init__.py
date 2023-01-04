"""A full-functionality wrapper for the https://ballchasing.com API.

:copyright: (c) 2022 Tanner B. Corcoran
:license: MIT, see LICENSE for more details.
"""

__title__ = "pychasing"
__author__ = "Tanner B. Corcoran"
__email__ = "tannerbcorcoran@gmail.com"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2022 Tanner B. Corcoran"
__version__ = "0.1.4"
__description__ = "A full-functionality wrapper for the https://ballchasing.com API"
__url__ = "https://github.com/tanrbobanr/pychasing"
__download_url__ = "https://pypi.org/project/pychasing/"


__all__ = (
    "Client",
    "PatreonTier",
    "Rank",
    "Playlist",
    "Platform",
    "Map",
    "Visibility",
    "Season",
    "PlayerIdentification",
    "TeamIdentification",
    "MatchResult",
    "ReplaySortBy",
    "GroupSortBy",
    "SortDirection",
    "GroupStats",
    "Date",
    "ReplayBuffer"
)


from .client import Client
from .enums import PatreonTier
from .enums import Rank
from .enums import Playlist
from .enums import Platform
from .enums import Map
from .enums import Visibility
from .enums import Season
from .enums import PlayerIdentification
from .enums import TeamIdentification
from .enums import MatchResult
from .enums import ReplaySortBy
from .enums import GroupSortBy
from .enums import SortDirection
from .enums import GroupStats
from .models import Date
from .models import ReplayBuffer
