"""Helper types.

:copyright: (c) 2022 Tanner B. Corcoran
:license: MIT, see LICENSE for more details.
"""

__author__ = "Tanner B. Corcoran"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2022 Tanner B. Corcoran"


from . import constants


JsonParsable = dict | list | str | int


class PatreonTierType:
    LIST_REPLAYS    : float
    GET_REPLAY      : float
    DELETE_REPLAY   : float
    PATCH_REPLAY    : float
    DOWNLOAD_REPLAY : float
    CREATE_GROUP    : float
    LIST_GROUPS     : float
    GET_GROUP       : float
    DELETE_GROUP    : float
    PATCH_GROUP     : float
    __raw__         : dict[str, float]


class Rank:
    (
        UNRANKED,
        BRONZE_1,
        BRONZE_2,
        BRONZE_3,
        SILVER_1,
        SILVER_2,
        SILVER_3,
        GOLD_1,
        GOLD_2,
        GOLD_3,
        PLATINUM_1,
        PLATINUM_2,
        PLATINUM_3,
        DIAMOND_1,
        DIAMOND_2,
        DIAMOND_3,
        CHAMPION_1,
        CHAMPION_2,
        CHAMPION_3,
        GRAND_CHAMPION_1,
        GRAND_CHAMPION_2,
        GRAND_CHAMPION_3,
        SUPERSONIC_LEGEND
    ) = constants.RANK

    
class Playlist:
    (
        UNRANKED_DUELS,
        UNRANKED_DOUBLES,
        UNRANKED_STANDARD,
        UNRANKED_CHAOS,
        PRIVATE,
        SEASON,
        OFFLINE,
        RANKED_DUELS,
        RANKED_DOUBLES,
        RANKED_SOLO_STANDARD,
        RANKED_STANDARD,
        SNOWDAY,
        ROCKETLABS,
        HOOPS,
        RUMBLE,
        TOURNAMENT,
        DROPSHOT,
        RANKED_HOOPS,
        RANKED_RUMBLE,
        RANKED_DROPSHOT,
        RANKED_SNOWDAY,
        DROPSHOT_RUMBLE,
        HEATSEEKER
    ) = constants.PLAYLIST


class Platform:
    (
        STEAM,
        EPIC,
        XBL,
        PSN,
        SWITCH
    ) = constants.PLATFORM


class Map:
    (
        ARC_P,
        ARC_STANDARD_P,
        BB_P,
        BEACH_NIGHT_P,
        BEACH_P,
        BEACHVOLLEY,
        CHN_STADIUM_DAY_P,
        CHN_STADIUM_P,
        CS_DAY_P,
        CS_HW_P,
        CS_P,
        EUROSTADIUM_NIGHT_P,
        EUROSTADIUM_P,
        EUROSTADIUM_RAINY_P,
        EUROSTADIUM_SNOWNIGHT_P,
        FARM_NIGHT_P,
        FARM_P,
        FARM_UPSIDEDOWN_P,
        HAUNTED_TRAINSTATION_P,
        HOOPSSTADIUM_P,
        LABS_CIRCLEPILLARS_P,
        LABS_CORRIDOR_P,
        LABS_COSMIC_P,
        LABS_COSMIC_V4_P,
        LABS_DOUBLEGOAL_P,
        LABS_DOUBLEGOAL_V2_P,
        LABS_OCTAGON_02_P,
        LABS_OCTAGON_P,
        LABS_UNDERPASS_P,
        LABS_UNDERPASS_V0_P,
        LABS_UTOPIA_P,
        MUSIC_P,
        NEOTOKYO_P,
        NEOTOKYO_STANDARD_P,
        PARK_NIGHT_P,
        PARK_P,
        PARK_RAINY_P,
        SHATTERSHOT_P,
        STADIUM_DAY_P,
        STADIUM_FOGGY_P,
        STADIUM_P,
        STADIUM_RACE_DAY_P,
        STADIUM_WINTER_P,
        THROWBACKSTADIUM_P,
        TRAINSTATION_DAWN_P,
        TRAINSTATION_NIGHT_P,
        TRAINSTATION_P,
        UNDERWATER_P,
        UTOPIASTADIUM_DUSK_P,
        UTOPIASTADIUM_P,
        UTOPIASTADIUM_SNOW_P,
        WASTELAND_NIGHT_P,
        WASTELAND_NIGHT_S_P,
        WASTELAND_P,
        WASTELAND_S_P,
        STARBASE_ARC,
        STARBASE_ARC_STANDARD,
        CHAMPIONS_FIELD_NFL,
        SALTY_SHORES_NIGHT,
        SALTY_SHORES,
        SALTY_SHORES_VOLLEY,
        FORBIDDEN_TEMPLE_DAY,
        FORBIDDEN_TEMPLE,
        CHAMPIONS_FIELD_DAY,
        RIVALS_ARENA,
        CHAMPIONS_FIELD,
        MANNFIELD_NIGHT,
        MANNFIELD,
        MANNFIELD_STORMY,
        MANNFIELD_SNOWY,
        FARMSTEAD_NIGHT,
        FARMSTEAD,
        FARMSTEAD_THE_UPSIDE_DOWN,
        URBAN_CENTRAL_HAUNTED,
        DUNK_HOUSE,
        PILLARS,
        CORRIDOR,
        COSMIC,
        COSMIC,
        DOUBLE_GOAL,
        DOUBLE_GOAL,
        OCTAGON,
        OCTAGON,
        UNDERPASS,
        UNDERPASS_,
        UTOPIA_RETRO,
        NEON_FIELDS,
        NEO_TOKYO,
        NEO_TOKYO_STANDARD,
        BECKWITH_PARK_MIDNIGHT,
        BECKWITH_PARK,
        BECKWITH_PARK_STORMY,
        CORE_707,
        DFH_STADIUM_DAY,
        DFH_STADIUM_STORMY,
        DFH_STADIUM,
        DFH_STADIUM_CIRCUIT,
        DFH_STADIUM_SNOWY,
        THROWBACK_STADIUM,
        URBAN_CENTRAL_DAWN,
        URBAN_CENTRAL_NIGHT,
        URBAN_CENTRAL,
        AQUADOME,
        UTOPIA_COLISEUM_DUSK,
        UTOPIA_COLISEUM,
        UTOPIA_COLISEUM_SNOWY,
        WASTELAND_NIGHT,
        WASTELAND_STANDARD_NIGHT,
        WASTELAND,
        WASTELAND_STANDARD
    ) = constants.MAP + constants.MAP


class PatreonTier:
    class GrandChampion(PatreonTierType):
        (
            LIST_REPLAYS,
            GET_REPLAY,
            DELETE_REPLAY,
            PATCH_REPLAY,
            DOWNLOAD_REPLAY,
            CREATE_GROUP,
            LIST_GROUPS,
            GET_GROUP,
            DELETE_GROUP,
            PATCH_GROUP
        ) = constants.RATE_LIMITS["GRAND_CHAMPION"]
        __raw__ = {k:v for k, v in zip(constants.LIMITED_OPERATIONS, constants.RATE_LIMITS["GRAND_CHAMPION"])}
    
    
    class Champion(PatreonTierType):
        (
            LIST_REPLAYS,
            GET_REPLAY,
            DELETE_REPLAY,
            PATCH_REPLAY,
            DOWNLOAD_REPLAY,
            CREATE_GROUP,
            LIST_GROUPS,
            GET_GROUP,
            DELETE_GROUP,
            PATCH_GROUP
        ) = constants.RATE_LIMITS["CHAMPION"]
        __raw__ = {k:v for k, v in zip(constants.LIMITED_OPERATIONS, constants.RATE_LIMITS["CHAMPION"])}
    

    class Diamond(PatreonTierType):
        (
            LIST_REPLAYS,
            GET_REPLAY,
            DELETE_REPLAY,
            PATCH_REPLAY,
            DOWNLOAD_REPLAY,
            CREATE_GROUP,
            LIST_GROUPS,
            GET_GROUP,
            DELETE_GROUP,
            PATCH_GROUP
        ) = constants.RATE_LIMITS["DIAMOND"]
        __raw__ = {k:v for k, v in zip(constants.LIMITED_OPERATIONS, constants.RATE_LIMITS["DIAMOND"])}
    

    class Gold(PatreonTierType):
        (
            LIST_REPLAYS,
            GET_REPLAY,
            DELETE_REPLAY,
            PATCH_REPLAY,
            DOWNLOAD_REPLAY,
            CREATE_GROUP,
            LIST_GROUPS,
            GET_GROUP,
            DELETE_GROUP,
            PATCH_GROUP
        ) = constants.RATE_LIMITS["GOLD"]
        __raw__ = {k:v for k, v in zip(constants.LIMITED_OPERATIONS, constants.RATE_LIMITS["GOLD"])}
    

    class Regular(PatreonTierType):
        (
            LIST_REPLAYS,
            GET_REPLAY,
            DELETE_REPLAY,
            PATCH_REPLAY,
            DOWNLOAD_REPLAY,
            CREATE_GROUP,
            LIST_GROUPS,
            GET_GROUP,
            DELETE_GROUP,
            PATCH_GROUP
        ) = constants.RATE_LIMITS["REGULAR"]
        __raw__ = {k:v for k, v in zip(constants.LIMITED_OPERATIONS, constants.RATE_LIMITS["REGULAR"])}


class Visibility:
    (
        PUBLIC,
        UNLISTED,
        PRIVATE
    ) = constants.VISIBILITY


class PlayerIdentification:
    (
        BY_ID,
        BY_NAME
    ) = constants.PLAYER_IDENTIFICATION


class TeamIdentification:
    (
        BY_DISTINCT_PLAYERS,
        BY_PLAYER_CLUSTERS
    ) = constants.TEAM_IDENTIFICATION


class MatchResult:
    (
        WIN,
        LOSS
    ) = constants.MATCH_RESULT


class SortBy:
    (
        REPLAY_DATE,
        REPLAY_UPLOAD_DATE,
        GROUP_CREATED,
        GROUP_NAME
    ) = constants.SORT_BY


class SortDir:
    (
        ASC,
        DESC
    ) = constants.SORT_DIR


class GroupStats:
    (
        PLAYERS,
        TEAMS,
        PLAYERS_GAMES,
        TEAMS_GAMES
    ) = constants.GROUP_STATS
