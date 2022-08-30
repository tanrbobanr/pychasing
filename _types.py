from __future__      import annotations as __annotations
"""
`discord.py` Tools
~~~~~~~~~~~~~~~~~~~

A set of wrappers and tools for `discord.py`.

DISCLAIMER: You are not permitted to use, modify,
or redistribute any portion of this code without 
the direct consent of the author.

:copyright: (c) 2022-present tanrbobanr

@author: C., Tanner; tanrbobanr; tannerbcorcoran@gmail.com
"""


__title__ = "Discord/Python Tools"
__author__ = "C., Tanner; tanrbobanr; tannerbcorcoran@gmail.com"
__copyright__ = "Copyright 2022-present tanrbobanr"
__version__ = "1.0.5"

from discord.ext import commands as _commands
from discord     import app_commands as _app_commands
from typing      import (
    Union as _Union,
    Coroutine as _Coroutine,
    Callable as _Callable,
    Literal as _Literal,
    Any as _Any
)
from dpyt.interfaces.implementations import (
    _exceptions  as _exceptions,
    _dataclasses as _dataclasses
)

from datetime import datetime as _datetime
from abc import (
    ABC as _ABC,
    abstractmethod as _abstractmethod
)

import discord as _discord
import sqlite3 as _sqlite3


num = _Union[int, float]
JsonParsable = _Union[list, dict, int, float, str, tuple]


AnyBallchasingRank = [
    "unranked", "bronze-1", "bronze-2", "bronze-3", "silver-1",
    "silver-2", "silver-3", "gold-1", "gold-2", "gold-3",
    "platinum-1", "platinum-2", "platinum-3", "diamond-1", "diamond-2",
    "diamond-3", "champion-1", "champion-2", "champion-3", "grand-champion-1",
    "grand-champion-2", "grand-champion-3", "supersonic-legend"
]


AnyBallchasingPlaylist=[
    "unranked-duels", "unranked-doubles", "unranked-standard", "unranked-chaos", "private",
    "season", "offline", "ranked-duels", "ranked-doubles", "ranked-solo-standard",
    "ranked-standard", "snowday", "rocketlabs", "hoops", "rumble",
    "tournament", "dropshot", "ranked-hoops", "ranked-rumble", "ranked-dropshot",
    "ranked-snowday", "dropshot-rumble", "heatseeker"
]


AnyBallchasingPlatform=[
    "steam", "epic", "xbl", "psn", "switch"
]


AnyBallchasingMap=[
    "arc_p", "arc_standard_p", "bb_p", "beach_night_p", "beach_p",
    "beachvolley", "chn_stadium_day_p", "chn_stadium_p", "cs_day_p", "cs_hw_p",
    "cs_p", "eurostadium_night_p", "eurostadium_p", "eurostadium_rainy_p", "eurostadium_snownight_p",
    "farm_night_p", "farm_p", "farm_upsidedown_p", "haunted_trainstation_p", "hoopsstadium_p",
    "labs_circlepillars_p", "labs_corridor_p", "labs_cosmic_p", "labs_cosmic_v4_p", "labs_doublegoal_p",
    "labs_doublegoal_v2_p", "labs_octagon_02_p", "labs_octagon_p", "labs_underpass_p", "labs_underpass_v0_p",
    "labs_utopia_p", "music_p", "neotokyo_p", "neotokyo_standard_p", "park_night_p",
    "park_p", "park_rainy_p", "shattershot_p", "stadium_day_p", "stadium_foggy_p",
    "stadium_p", "stadium_race_day_p", "stadium_winter_p", "throwbackstadium_p", "trainstation_dawn_p",
    "trainstation_night_p", "trainstation_p", "underwater_p", "utopiastadium_dusk_p", "utopiastadium_p",
    "utopiastadium_snow_p", "wasteland_night_p", "wasteland_night_s_p", "wasteland_p", "wasteland_s_p"
]


AnyBallchasingVisibilty = [
    "public", "unlisted", "private"
]


AnyBallchasingPatreonTier = [
    "grand_champion",
    "champion",
    "diamond",
    "gold",
    "none"
]


AnyGoogleSpreadsheetHorizontalAlignment = ["left", "center", "right", "general", "general-left", "general-right", "normal", None]


AnyGoogleSpreadsheetWrapStrategy = ["WRAP", "OVERFLOW", "CLIP", None]


AnyGoogleSpreadsheetFontLine = ["underline", "line-through", "none"]


AnyGoogleSpreadsheetFontStyle = ["italic", "normal", None]


AnyGoogleSpreadsheetFontWeight = ["bold", "normal", None]


AnyGoogleSpreadsheetVerticalAlignment = ["top", "middle", "bottom", None]


AnyGoogleFileAccessType = ["ANYONE", "ANYONE_WITH_LINK", "DOMAIN", "DOMAIN_WITH_LINK", "PRIVATE"]


AnyGoogleFilePermissionType = [
    "VIEW", "EDIT", "COMMENT", "OWNER", "ORGANIZER",
    "FILE_ORGANIZER", "NONE"
]


AnyGoogleMimeType = [
    "application/vnd.google-apps.document", "application/vnd.google-apps.drive-sdk", "application/vnd.google-apps.drawing", "application/vnd.google-apps.file", "application/vnd.google-apps.folder",
    "application/vnd.google-apps.form", "application/vnd.google-apps.fusiontable", "application/vnd.google-apps.jam", "application/vnd.google-apps.map","application/vnd.google-apps.presentation",
    "application/vnd.google-apps.script", "application/vnd.google-apps.shortcut", "application/vnd.google-apps.site", "application/vnd.google-apps.spreadsheet"
]


class GoogleSpreadsheetHorizontalAlignment:
    (
        LEFT, CENTER, RIGHT, GENERAL, GENERAL_LEFT,
        GENERAL_RIGHT, NORMAL, NONE
    ) = AnyGoogleSpreadsheetHorizontalAlignment


class GoogleSpreadsheetWrapStrategy:
    (WRAP, OVERFLOW, CLIP, NONE) = AnyGoogleSpreadsheetWrapStrategy


class GoogleSpreadsheetFontLine:
    (UNDERLINE, LINE_THROUGH, NONE) = AnyGoogleSpreadsheetFontLine


class GoogleSpreadsheetFontStyle:
    (ITALIC, NORMAL, NONE) = AnyGoogleSpreadsheetFontStyle


class GoogleSpreadsheetFontWeight:
    (BOLD, NORMAL, NONE) = AnyGoogleSpreadsheetFontWeight


class GoogleSpreadsheetVerticalAlignment:
    (TOP, MIDDLE, BOTTOM, NONE) = AnyGoogleSpreadsheetVerticalAlignment


class GoogleFileAccessType:
    (ANYONE, ANYONE_WITH_LINK, DOMAIN, DOMAIN_WITH_LINK, PRIVATE) = AnyGoogleFileAccessType


class GoogleFilePermissionType:
    (
        VIEW, EDIT, COMMENT, OWNER, ORGANIZER,
        FILE_ORGANIZER, NONE
    ) = AnyGoogleFilePermissionType


class GoogleMimeType:
    (
        GOOGLE_DOCS, THIRD_PARTY_SHORTCUT, GOOGLE_DRAWING, GOOGLE_DRIVE_FILE, GOOGLE_DRIVE_FOLDER,
        GOOGLE_FORMS, GOOGLE_FUSION_TABLES, GOOGLE_JAMBOARD, GOOGLE_MY_MAPS, GOOGLE_SLIDES,
        GOOGLE_APPS_SCRIPT, GOOGLE_SHORTCUT, GOOGLE_SITES, GOOGLE_SHEETS
    ) = AnyGoogleMimeType


class CheckType:
    def __init__(self) -> None:
        self.raise_: _Union[_app_commands.CheckFailure, _commands.CheckFailure] = ...
    def predicate(self, utx: _Union[_commands.Context, _discord.Interaction]) -> bool: ...


class ROLE:
    def mention(id: int) -> str:
        return f"<@&{id}>"


class TEXTCHANNEL:
    def mention(id: int) -> str:
        return f"<#{id}>"


class MEMBER:
    def mention(id: int) -> str:
        return f"<@!{id}>"


class GUILD:
    def mention(id: int) -> str:
        raise _exceptions.Unmentionable()


class CATEGORYCHANNEL:
    def mention(id: int) -> str:
        raise _exceptions.Unmentionable()


class VOICECHANNEL:
    def mention(id: int) -> str:
        return f"<#{id}>"


class BotType(_commands.Bot):
    __name__ = "BotConstructor"


    def __init__(
        self,
        command_prefix              : str,
        application_errors_channels : list[int],
        application_errors_pings    : list[list[int]],
        intents                     : _discord.Intents,
        *,
        status                      : _discord.Status   = ...,
        activity                    : _discord.Activity = ...,
        enabled                     : bool               = ...,
        modules_path                : str                = ...,
        view_operation              : _Coroutine        = ...
    ) -> None:
        self.enabled                     = ...
        self.application_errors_channels = ...
        self.application_errors_pings    = ...
        self.modules_path                = ...
        self.view_operation              = ...


    async def setup_hook(self) -> None:
        ...


    async def send_error(self, utx: _Union[_commands.Context, _discord.Interaction]) -> None:
        ...


class EmbedFieldType:


    def __init__(
        self,
        name   : str,
        value  : str,
        *,
        inline : bool = ...
    ) -> None:
        self.name   = ...
        self.value  = ...
        self.inline = ...


class EmbedWrapperType(_discord.Embed):


    def __init__(
        self,
        *,
        title           : str                       = ...,
        title_url       : str                       = ...,
        author          : str                       = ...,
        author_url      : str                       = ...,
        author_icon_url : str                       = ...,
        description     : str                       = ...,
        timestamp       : _Union[_datetime, bool] = ...,
        fields          : list[EmbedFieldType]      = ...,
        color           : int                       = ...,
        footer          : str                       = ...,
        footer_url      : str                       = ...,
        thumbnail_url   : str                       = ...,
        image_url       : str                       = ...
    ) -> None:
        self.__title           = ...
        self.__title_url       = ...
        self.__author          = ...
        self.__author_url      = ...
        self.__author_icon_url = ...
        self.__description     = ...
        self.__timestamp       = ...
        self.__fields          = ...
        self.__color           = ...
        self.__footer          = ...
        self.__footer_url      = ...
        self.__thumbnail_url   = ...
        self.__image_url       = ...


    def new_from_base(
        self,
        *,
        title           : str                       = ...,
        title_url       : str                       = ...,
        author          : str                       = ...,
        author_url      : str                       = ...,
        author_icon_url : str                       = ...,
        description     : str                       = ...,
        timestamp       : _Union[_datetime, bool] = ...,
        fields          : list[EmbedFieldType]      = ...,
        color           : int                       = ...,
        footer          : str                       = ...,
        footer_url      : str                       = ...,
        thumbnail_url   : str                       = ...,
        image_url       : str                       = ...
    ) -> EmbedWrapperType:
        ...


class BallchasingPatreonTier:
    list_replays    : float
    get_replay      : float
    delete_replay   : float
    patch_replay    : float
    download_replay : float
    create_group    : float
    list_groups     : float
    get_group       : float
    delete_group    : float
    patch_group     : float


class Ballchasing:


    class Rank:
        (
            UNRANKED, BRONZE_1, BRONZE_2, BRONZE_3, SILVER_1,
            SILVER_2, SILVER_3, GOLD_1, GOLD_2, GOLD_3,
            PLATINUM_1, PLATINUM_2, PLATINUM_3, DIAMOND_1, DIAMOND_2,
            DIAMOND_3, CHAMPION_1, CHAMPION_2, CHAMPION_3, GRAND_CHAMPION_1,
            GRAND_CHAMPION_2, GRAND_CHAMPION_3, SUPERSONIC_LEGEND
        ) = AnyBallchasingRank


    class Playlist:
        (
            UNRANKED_DUELS, UNRANKED_DOUBLES, UNRANKED_STANDARD, UNRANKED_CHAOS, PRIVATE,
            SEASON, OFFLINE, RANKED_DUELS, RANKED_DOUBLES, RANKED_SOLO_STANDARD,
            RANKED_STANDARD, SNOWDAY, ROCKETLABS, HOOPS, RUMBLE,
            TOURNAMENT, DROPSHOT, RANKED_HOOPS, RANKED_RUMBLE, RANKED_DROPSHOT,
            RANKED_SNOWDAY, DROPSHOT_RUMBLE, HEATSEEKER
        ) = AnyBallchasingPlaylist


    class Platform:
        (
            STEAM, EPIC, XBL, PSN, SWITCH
        ) = AnyBallchasingPlatform


    class Map:
        (
            ARC_P, ARC_STANDARD_P, BB_P, BEACH_NIGHT_P, BEACH_P,
            BEACHVOLLEY, CHN_STADIUM_DAY_P, CHN_STADIUM_P, CS_DAY_P, CS_HW_P,
            CS_P, EUROSTADIUM_NIGHT_P, EUROSTADIUM_P, EUROSTADIUM_RAINY_P, EUROSTADIUM_SNOWNIGHT_P,
            FARM_NIGHT_P, FARM_P, FARM_UPSIDEDOWN_P, HAUNTED_TRAINSTATION_P, HOOPSSTADIUM_P,
            LABS_CIRCLEPILLARS_P, LABS_CORRIDOR_P, LABS_COSMIC_P, LABS_COSMIC_V4_P, LABS_DOUBLEGOAL_P,
            LABS_DOUBLEGOAL_V2_P, LABS_OCTAGON_02_P, LABS_OCTAGON_P, LABS_UNDERPASS_P, LABS_UNDERPASS_V0_P,
            LABS_UTOPIA_P, MUSIC_P, NEOTOKYO_P, NEOTOKYO_STANDARD_P, PARK_NIGHT_P,
            PARK_P, PARK_RAINY_P, SHATTERSHOT_P, STADIUM_DAY_P, STADIUM_FOGGY_P,
            STADIUM_P, STADIUM_RACE_DAY_P, STADIUM_WINTER_P, THROWBACKSTADIUM_P, TRAINSTATION_DAWN_P,
            TRAINSTATION_NIGHT_P, TRAINSTATION_P, UNDERWATER_P, UTOPIASTADIUM_DUSK_P, UTOPIASTADIUM_P,
            UTOPIASTADIUM_SNOW_P, WASTELAND_NIGHT_P, WASTELAND_NIGHT_S_P, WASTELAND_P, WASTELAND_S_P,
            STARBASE_ARC, STARBASE_ARC_STANDARD, CHAMPIONS_FIELD_NFL, SALTY_SHORES_NIGHT, SALTY_SHORES,
            SALTY_SHORES_VOLLEY, FORBIDDEN_TEMPLE_DAY, FORBIDDEN_TEMPLE, CHAMPIONS_FIELD_DAY, RIVALS_ARENA,
            CHAMPIONS_FIELD, MANNFIELD_NIGHT, MANNFIELD, MANNFIELD_STORMY, MANNFIELD_SNOWY,
            FARMSTEAD_NIGHT, FARMSTEAD, FARMSTEAD_THE_UPSIDE_DOWN, URBAN_CENTRAL_HAUNTED, DUNK_HOUSE,
            PILLARS, CORRIDOR, COSMIC, COSMIC, DOUBLE_GOAL,
            DOUBLE_GOAL, OCTAGON, OCTAGON, UNDERPASS, UNDERPASS_,
            UTOPIA_RETRO, NEON_FIELDS, NEO_TOKYO, NEO_TOKYO_STANDARD, BECKWITH_PARK_MIDNIGHT,
            BECKWITH_PARK, BECKWITH_PARK_STORMY, CORE_707, DFH_STADIUM_DAY, DFH_STADIUM_STORMY,
            DFH_STADIUM, DFH_STADIUM_CIRCUIT, DFH_STADIUM_SNOWY, THROWBACK_STADIUM, URBAN_CENTRAL_DAWN,
            URBAN_CENTRAL_NIGHT, URBAN_CENTRAL, AQUADOME, UTOPIA_COLISEUM_DUSK, UTOPIA_COLISEUM,
            UTOPIA_COLISEUM_SNOWY, WASTELAND_NIGHT, WASTELAND_STANDARD_NIGHT, WASTELAND, WASTELAND_STANDARD
        ) = AnyBallchasingMap + AnyBallchasingMap


    class PatreonTier:
        class GrandChampion(BallchasingPatreonTier):
            list_replays    = 1 / 16
            get_replay      = 1 / 16
            delete_replay   = 1 / 16
            patch_replay    = 1 / 16
            download_replay = 1 / 2
            create_group    = 1 / 16
            list_groups     = 1 / 16
            get_group       = 1 / 16
            delete_group    = 1 / 16
            patch_group     = 1 / 16
        
        
        class Champion(BallchasingPatreonTier):
            list_replays    = 1 / 8
            get_replay      = 1 / 8
            delete_replay   = 1 / 8
            patch_replay    = 1 / 8
            download_replay = 3600 / 2000
            create_group    = 1 / 8
            list_groups     = 1 / 8
            get_group       = 1 / 8
            delete_group    = 1 / 8
            patch_group     = 1 / 8
        

        class Diamond(BallchasingPatreonTier):
            list_replays    = 3600 / 2000
            get_replay      = 3600 / 5000
            delete_replay   = 3600 / 5000
            patch_replay    = 3600 / 5000
            download_replay = 3600 / 1000
            create_group    = 3600 / 5000
            list_groups     = 3600 / 2000
            get_group       = 3600 / 5000
            delete_group    = 3600 / 5000
            patch_group     = 3600 / 5000
        

        class Gold(BallchasingPatreonTier):
            list_replays    = 3600 / 1000
            get_replay      = 3600 / 2000
            delete_replay   = 3600 / 2000
            patch_replay    = 3600 / 2000
            download_replay = 3600 / 400
            create_group    = 3600 / 2000
            list_groups     = 3600 / 1000
            get_group       = 3600 / 2000
            delete_group    = 3600 / 2000
            patch_group     = 3600 / 2000
        

        class Regular(BallchasingPatreonTier):
            list_replays    = 3600 / 500
            get_replay      = 3600 / 1000
            delete_replay   = 3600 / 1000
            patch_replay    = 3600 / 1000
            download_replay = 3600 / 200
            create_group    = 3600 / 1000
            list_groups     = 3600 / 500
            get_group       = 3600 / 1000
            delete_group    = 3600 / 1000
            patch_group     = 3600 / 1000


    class Visibility:
        (
            PUBLIC, UNLISTED, PRIVATE
        ) = AnyBallchasingVisibilty


class SQLiteCredentialsType:
    sqlite_connections: dict[str, _sqlite3.Connection] = ...


class SQLiteExecutionType(SQLiteCredentialsType):
    def __init__(self, fp: str, query: str, vars: tuple, vars_unchecked: tuple) -> None: ...
    def __repr__(self) -> str: ...
    def fetchone(self) -> tuple: ...
    def fetchall(self) -> list[tuple]: ...
    def fetchmany(self, batch_size: int) -> list[tuple]: ...
    def cursor(self) -> _sqlite3.Cursor: ...
    def commit(self) -> None: ...


class SQLiteIOManagerType(_ABC):
    @_abstractmethod
    def __init__(self, fp: str, *, timeout: float = ...) -> None: ...
    @_abstractmethod
    def __repr__(self) -> str: ...
    @_abstractmethod
    def execute(self, query: str, vars: tuple = ..., *, vars_unchecked: tuple = ...) -> SQLiteExecutionType: ...
    @_abstractmethod
    def cursor(self) -> _sqlite3.Cursor: ...
    @_abstractmethod
    def connection(self) -> _sqlite3.Connection: ...
    @_abstractmethod
    def __del__(self) -> None: ...


class RocketLeagueMatchDataManagerType(_ABC):
    @_abstractmethod
    def __init__(self, sqlite_manager: SQLiteIOManagerType, table_name: str ) -> None: ...
    @_abstractmethod
    def add_match(self, series: _Union[_dataclasses.RocketLeagueSeries, _dataclasses.RocketLeagueNCPSeries], player_converter: _Callable[[str, str], int] = ...) -> None: ...
    @_abstractmethod
    def get_stats(self, preprocessing: _Literal["tot", "avgpg", "avgps"], round_: bool, round_digits: int = ..., league: str = ..., conference: str = ..., division: str = ..., player_id: int = ..., id_id: str = ..., id_platform: str = ..., name: str = ..., team: str = ...) -> _dataclasses.RocketLeagueStatBlock: ...
    @_abstractmethod
    def get_leaderboard(self, stat: str, group_by: _Literal["id_platform", "id_id", "name", "player_id", "team"], display_name: _Literal["id_platform", "id_id", "name", "player_id", "team"], ppt: _Literal["tot", "avgpg", "avgps"], sort_dir: _Literal["asc", "desc"], round_: bool, round_digits: int, *,league: _Any = None, conference: _Any = None, division: _Any = None) -> dict[str, dict[str, str | int | float]]: ...
    @_abstractmethod 
    def get_game(self, game_id : int) -> _dataclasses.BallchasingReplay | _dataclasses.RocketLeagueNCPGame: ...
    @_abstractmethod
    def get_series(self, series_id : int ) -> _dataclasses.RocketLeagueSeries | _dataclasses.RocketLeagueNCPSeries: ...

class OperationType(dict):
    def __init__(self) -> None: ...
    def begin_track(self, user: int) -> None: ...
    def end_track(self, user: int) -> None: ...


class OperationTrackerType(_ABC):
    def __init__(self, defaults: list[str] = ...) -> None: ...
    def __getitem__(self, __key: _Any) -> OperationType: ...
    def current_tracks(self) -> dict[str, list[tuple[int, int]]]: ...

