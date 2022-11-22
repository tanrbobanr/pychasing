"""Enumerations used by ``client``.

:copyright: (c) 2022-present Tanner B. Corcoran
:license: MIT, see LICENSE for more details.
"""

__author__ = "Tanner B. Corcoran"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2022-present Tanner B. Corcoran"

import enum


class Operation(enum.Enum):
    ping="ping"
    upload_replay="upload_replay"
    list_replays="list_replays"
    get_replay="get_replay"
    delete_replay="delete_replay"
    patch_replay="patch_replay"
    download_replay="download_replay"
    create_group="create_group"
    list_groups="list_groups"
    get_group="get_group"
    delete_group="delete_group"
    patch_group="patch_group"
    maps="maps"
    get_threejs="get_threejs"
    get_timeline="get_timeline"
    export_csv="export_csv"

class PatreonTier(enum.Enum):
    grand_champion={
        Operation.list_replays: (16,),
        Operation.get_replay: (16,),
        Operation.delete_replay: (16,),
        Operation.patch_replay: (16,),
        Operation.download_replay: (2,),
        Operation.create_group: (16,),
        Operation.list_groups: (16,),
        Operation.get_group: (16,),
        Operation.delete_group: (16,),
        Operation.patch_group: (16,)
    }
    champion={
        Operation.list_replays: (8,),
        Operation.get_replay: (8,),
        Operation.delete_replay: (8,),
        Operation.patch_replay: (8,),
        Operation.download_replay: (2, 2000, 3600),
        Operation.create_group: (8,),
        Operation.list_groups: (8,),
        Operation.get_group: (8,),
        Operation.delete_group: (8,),
        Operation.patch_group: (8,)
    }
    diamond={
        Operation.list_replays: (4, 2000, 3600),
        Operation.get_replay: (4, 5000, 3600),
        Operation.delete_replay: (4, 5000, 3600),
        Operation.patch_replay: (4, 5000, 3600),
        Operation.download_replay: (2, 1000, 3600),
        Operation.create_group: (4, 5000, 3600),
        Operation.list_groups: (4, 2000, 3600),
        Operation.get_group: (4, 5000, 3600),
        Operation.delete_group: (4, 5000, 3600),
        Operation.patch_group: (4, 5000, 3600)
    }
    gold={
        Operation.list_replays: (2, 1000, 3600),
        Operation.get_replay: (2, 2000, 3600),
        Operation.delete_replay: (2, 2000, 3600),
        Operation.patch_replay: (2, 2000, 3600),
        Operation.download_replay: (2, 400, 3600),
        Operation.create_group: (2, 2000, 3600),
        Operation.list_groups: (2, 1000, 3600),
        Operation.get_group: (2, 2000, 3600),
        Operation.delete_group: (2, 2000, 3600),
        Operation.patch_group: (2, 2000, 3600)
    }
    regular={
        Operation.list_replays: (2, 500, 3600),
        Operation.get_replay: (2, 1000, 3600),
        Operation.delete_replay: (2, 1000, 3600),
        Operation.patch_replay: (2, 1000, 3600),
        Operation.download_replay: (1, 200, 3600),
        Operation.create_group: (2, 1000, 3600),
        Operation.list_groups: (2, 500, 3600),
        Operation.get_group: (2, 1000, 3600),
        Operation.delete_group: (2, 1000, 3600),
        Operation.patch_group: (2, 1000, 3600)
    }
    none=regular

class Rank(enum.Enum):
    unranked="unranked"
    bronze_1="bronze-1"
    bronze_2="bronze-2"
    bronze_3="bronze-3"
    silver_1="silver-1"
    silver_2="silver-2"
    silver_3="silver-3"
    gold_1="gold-1"
    gold_2="gold-2"
    gold_3="gold-3"
    platinum_1="platinum-1"
    platinum_2="platinum-2"
    platinum_3="platinum-3"
    diamond_1="diamond-1"
    diamond_2="diamond-2"
    diamond_3="diamond-3"
    champion_1="champion-1"
    champion_2="champion-2"
    champion_3="champion-3"
    grand_champion_1="grand-champion-1"
    grand_champion_2="grand-champion-2"
    grand_champion_3="grand-champion-3"
    supersonic_legend="supersonic-legend"

class Playlist(enum.Enum):
    unranked_duels="unranked-duels"
    unranked_doubles="unranked-doubles"
    unranked_standard="unranked-standard"
    unranked_chaos="unranked-chaos"
    private="private"
    season="season"
    offline="offline"
    ranked_duels="ranked-duels"
    ranked_doubles="ranked-doubles"
    ranked_solo_standard="ranked-solo-standard"
    ranked_standard="ranked-standard"
    snowday="snowday"
    rocketlabs="rocketlabs"
    hoops="hoops"
    rumble="rumble"
    tournament="tournament"
    dropshot="dropshot"
    ranked_hoops="ranked-hoops"
    ranked_rumble="ranked-rumble"
    ranked_dropshot="ranked-dropshot"
    ranked_snowday="ranked-snowday"
    dropshot_rumble="dropshot-rumble"
    heatseeker="heatseeker"

class Platform(enum.Enum):
    steam="steam"
    epic="epic"
    xbl="xbl"
    psn="psn"
    switch="switch"

class Map(enum.Enum):
    arc_p="arc_p"
    arc_standard_p="arc_standard_p"
    bb_p="bb_p"
    beach_night_p="beach_night_p"
    beach_p="beach_p"
    beachvolley="beachvolley"
    chn_stadium_day_p="chn_stadium_day_p"
    chn_stadium_p="chn_stadium_p"
    cs_day_p="cs_day_p"
    cs_hw_p="cs_hw_p"
    cs_p="cs_p"
    eurostadium_night_p="eurostadium_night_p"
    eurostadium_p="eurostadium_p"
    eurostadium_rainy_p="eurostadium_rainy_p"
    eurostadium_snownight_p="eurostadium_snownight_p"
    farm_hw_p="farm_hw_p"
    farm_night_p="farm_night_p"
    farm_p="farm_p"
    farm_upsidedown_p="farm_upsidedown_p"
    haunted_trainstation_p="haunted_trainstation_p"
    hoopsstadium_p="hoopsstadium_p"
    labs_circlepillars_p="labs_circlepillars_p"
    labs_corridor_p="labs_corridor_p"
    labs_cosmic_p="labs_cosmic_p"
    labs_cosmic_v4_p="labs_cosmic_v4_p"
    labs_doublegoal_p="labs_doublegoal_p"
    labs_doublegoal_v2_p="labs_doublegoal_v2_p"
    labs_octagon_02_p="labs_octagon_02_p"
    labs_octagon_p="labs_octagon_p"
    labs_underpass_p="labs_underpass_p"
    labs_underpass_v0_p="labs_underpass_v0_p"
    labs_utopia_p="labs_utopia_p"
    music_p="music_p"
    neotokyo_p="neotokyo_p"
    neotokyo_standard_p="neotokyo_standard_p"
    park_night_p="park_night_p"
    park_p="park_p"
    park_rainy_p="park_rainy_p"
    shattershot_p="shattershot_p"
    stadium_day_p="stadium_day_p"
    stadium_foggy_p="stadium_foggy_p"
    stadium_p="stadium_p"
    stadium_race_day_p="stadium_race_day_p"
    stadium_winter_p="stadium_winter_p"
    throwbackstadium_p="throwbackstadium_p"
    trainstation_dawn_p="trainstation_dawn_p"
    trainstation_night_p="trainstation_night_p"
    trainstation_p="trainstation_p"
    underwater_p="underwater_p"
    utopiastadium_dusk_p="utopiastadium_dusk_p"
    utopiastadium_p="utopiastadium_p"
    utopiastadium_snow_p="utopiastadium_snow_p"
    wasteland_night_p="wasteland_night_p"
    wasteland_night_s_p="wasteland_night_s_p"
    wasteland_p="wasteland_p"
    wasteland_s_p="wasteland_s_p"

class Visibility(enum.Enum):
    public="public"
    unlisted="unlisted"
    private="private"

class Season(enum.Enum):
    old_1="1"
    old_2="2"
    old_3="3"
    old_4="4"
    old_5="5"
    old_6="6"
    old_7="7"
    old_8="8"
    old_9="9"
    old_10="10"
    old_11="11"
    old_12="12"
    old_13="13"
    old_14="14"
    f2p_1="f1"
    f2p_2="f2"
    f2p_3="f3"
    f2p_4="f4"
    f2p_5="f5"
    f2p_6="f6"
    f2p_7="f7"
    f2p_8="f8"
    f2p_9="f9"
    f2p_10="f10"
    f2p_11="f11"
    f2p_12="f12"
    f2p_13="f13"
    f2p_14="f14"
    f2p_15="f15"
    f2p_16="f16"
    f2p_17="f17"
    f2p_18="f18"
    f2p_19="f19"
    f2p_20="f20"
    f2p_21="f21"
    f2p_22="f22"
    f2p_23="f23"
    f2p_24="f24"
    f2p_25="f25"
    f2p_26="f26"
    f2p_27="f27"
    f2p_28="f28"
    f2p_29="f29"
    f2p_30="f30"
    
class PlayerIdentification(enum.Enum):
    by_id="by-id"
    by_name="by-name"

class TeamIdentification(enum.Enum):
    by_distinct_players="by-distinct-players"
    by_player_clusters="by-player-clusters"

class MatchResult(enum.Enum):
    win="win"
    loss="loss"

class ReplaySortBy(enum.Enum):
    replay_date="replay-date"
    upload_date="upload-date"

class GroupSortBy(enum.Enum):
    created="created"
    name="name"

class SortDirection(enum.Enum):
    asc="asc"
    desc="desc"

class GroupStats(enum.Enum):
    players="players"
    teams="teams"
    players_games="players-games"
    teams_games="teams-games"
