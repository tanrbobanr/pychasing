"""Constants used by ``types`` and ``client``.

:copyright: (c) 2022-present Tanner B. Corcoran
:license: MIT, see LICENSE for more details.
"""

__author__ = "Tanner B. Corcoran"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2022-present Tanner B. Corcoran"


class REQUEST_METHOD:
    GET = "GET"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
class OPERATION:
    PING = "ping"
    UPLOAD_REPLAY = "upload_replay"
    LIST_REPLAYS = "list_replays"
    GET_REPLAY = "get_replay"
    DELETE_REPLAY = "delete_replay"
    PATCH_REPLAY = "patch_replay"
    DOWNLOAD_REPLAY = "download_replay"
    CREATE_GROUP = "create_group"
    LIST_GROUPS = "list_groups"
    GET_GROUP = "get_group"
    DELETE_GROUP = "delete_group"
    PATCH_GROUP = "patch_group"
    MAPS = "maps"
    GET_THREEJS = "get_threejs"
    GET_TIMELINE = "get_timeline"
    EXPORT_CSV = "export_csv"
LIMITED_OPERATIONS = [
    "list_replays",
    "get_replay",
    "delete_replay",
    "patch_replay",
    "download_replay",
    "create_group",
    "list_groups",
    "get_group",
    "delete_group",
    "patch_group"
]
RATE_LIMITS = {
    "GRAND_CHAMPION" : (
        0.0625, # (list_replays)    1 / 16
        0.0625, # (get_replay)      1 / 16
        0.0625, # (delete_replay)   1 / 16
        0.0625, # (patch_replay)    1 / 16
        0.5,    # (download_replay) 1 / 2
        0.0625, # (create_group)    1 / 16
        0.0625, # (list_groups)     1 / 16
        0.0625, # (get_group)       1 / 16
        0.0625, # (delete_group)    1 / 16
        0.0625 # (patch_group)     1 / 16
    ),
    "CHAMPION" : (
        0.125, # (list_replays)    1 / 8
        0.125, # (get_replay)      1 / 8
        0.125, # (delete_replay)   1 / 8
        0.125, # (patch_replay)    1 / 8
        1.8,   # (download_replay) 3600 / 2000
        0.125, # (create_group)    1 / 8
        0.125, # (list_groups)     1 / 8
        0.125, # (get_group)       1 / 8
        0.125, # (delete_group)    1 / 8
        0.125 # (patch_group)     1 / 8
    ),
    "DIAMOND" : (
        1.8,  # (list_replays)    3600 / 2000
        0.72, # (get_replay)      3600 / 5000
        0.72, # (delete_replay)   3600 / 5000
        0.72, # (patch_replay)    3600 / 5000
        3.6,  # (download_replay) 3600 / 1000
        0.72, # (create_group)    3600 / 5000
        1.8,  # (list_groups)     3600 / 2000
        0.72, # (get_group)       3600 / 5000
        0.72, # (delete_group)    3600 / 5000
        0.72 # (patch_group)     3600 / 5000
    ),
    "GOLD" : (
        3.6, # (list_replays)    3600 / 1000
        1.8, # (get_replay)      3600 / 2000
        1.8, # (delete_replay)   3600 / 2000
        1.8, # (patch_replay)    3600 / 2000
        9,   # (download_replay) 3600 / 400
        1.8, # (create_group)    3600 / 2000
        3.6, # (list_groups)     3600 / 1000
        1.8, # (get_group)       3600 / 2000
        1.8, # (delete_group)    3600 / 2000
        1.8 # (patch_group)     3600 / 2000
    ),
    "REGULAR" : (
        7.2, # (list_replays)    3600 / 500
        3.6, # (get_replay)      3600 / 1000
        3.6, # (delete_replay)   3600 / 1000
        3.6, # (patch_replay)    3600 / 1000
        18,  # (download_replay) 3600 / 200
        3.6, # (create_group)    3600 / 1000
        7.2, # (list_groups)     3600 / 500
        3.6, # (get_group)       3600 / 1000
        3.6, # (delete_group)    3600 / 1000
        3.6 # (patch_group)     3600 / 1000
    )
}
RANK = (
    "unranked",
    "bronze-1",
    "bronze-2",
    "bronze-3",
    "silver-1",
    "silver-2",
    "silver-3",
    "gold-1",
    "gold-2",
    "gold-3",
    "platinum-1",
    "platinum-2",
    "platinum-3",
    "diamond-1",
    "diamond-2",
    "diamond-3",
    "champion-1",
    "champion-2",
    "champion-3",
    "grand-champion-1",
    "grand-champion-2",
    "grand-champion-3",
    "supersonic-legend"
)
PLAYLIST = (
    "unranked-duels",
    "unranked-doubles",
    "unranked-standard",
    "unranked-chaos",
    "private",
    "season",
    "offline",
    "ranked-duels",
    "ranked-doubles",
    "ranked-solo-standard",
    "ranked-standard",
    "snowday",
    "rocketlabs",
    "hoops",
    "rumble",
    "tournament",
    "dropshot",
    "ranked-hoops",
    "ranked-rumble",
    "ranked-dropshot",
    "ranked-snowday",
    "dropshot-rumble",
    "heatseeker"
)
PLATFORM = [
    "steam",
    "epic",
    "xbl",
    "psn",
    "switch"
]
MAP = (
    "arc_p",
    "arc_standard_p",
    "bb_p",
    "beach_night_p",
    "beach_p",
    "beachvolley",
    "chn_stadium_day_p",
    "chn_stadium_p",
    "cs_day_p",
    "cs_hw_p",
    "cs_p",
    "eurostadium_night_p",
    "eurostadium_p",
    "eurostadium_rainy_p",
    "eurostadium_snownight_p",
    "farm_night_p",
    "farm_p",
    "farm_upsidedown_p",
    "haunted_trainstation_p",
    "hoopsstadium_p",
    "labs_circlepillars_p",
    "labs_corridor_p",
    "labs_cosmic_p",
    "labs_cosmic_v4_p",
    "labs_doublegoal_p",
    "labs_doublegoal_v2_p",
    "labs_octagon_02_p",
    "labs_octagon_p",
    "labs_underpass_p",
    "labs_underpass_v0_p",
    "labs_utopia_p",
    "music_p",
    "neotokyo_p",
    "neotokyo_standard_p",
    "park_night_p",
    "park_p",
    "park_rainy_p",
    "shattershot_p",
    "stadium_day_p",
    "stadium_foggy_p",
    "stadium_p",
    "stadium_race_day_p",
    "stadium_winter_p",
    "throwbackstadium_p",
    "trainstation_dawn_p",
    "trainstation_night_p",
    "trainstation_p",
    "underwater_p",
    "utopiastadium_dusk_p",
    "utopiastadium_p",
    "utopiastadium_snow_p",
    "wasteland_night_p",
    "wasteland_night_s_p",
    "wasteland_p",
    "wasteland_s_p"
)
VISIBILITY = (
    "public",
    "unlisted",
    "private"
)
PATREON_TIER = (
    "grand_champion",
    "champion",
    "diamond",
    "gold",
    "none"
)
PLAYER_IDENTIFICATION = (
    "by-id",
    "by-name"
)
TEAM_IDENTIFICATION = (
    "by-distinct-players",
    "by-player-clusters"
)
MATCH_RESULT = (
    "win",
    "loss"
)
SORT_BY = (
    "replay-date",
    "upload-date",
    "created",
    "name"
)
SORT_DIR = (
    "asc",
    "desc"
)
GROUP_STATS = (
    "players",
    "teams",
    "players-games",
    "teams-games"
)
