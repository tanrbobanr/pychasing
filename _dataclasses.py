from __future__                      import annotations as __annotations
import dataclasses as _dataclasses
from enum import Enum as _Enum
from dpyt.interfaces                 import _ext
from dpyt.interfaces.implementations import _types
from typing                          import (
    Optional as _Optional,
    Sequence as _Sequence,
    Union    as _Union,
    Any      as _Any
)

import sqlite3 as __sqlite3


@_dataclasses.dataclass(kw_only = True)
class Player:
    uuid           : _Any               = None
    discord_id     : int                = None
    username       : str                = None
    accounts       : _Sequence[Account] = None
    _acc_names     : list[str]      = _dataclasses.field(init = False)
    _acc_ids       : list           = _dataclasses.field(init = False)
    _acc_platforms : list[Platform] = _dataclasses.field(init = False)
    def __post_init__(self) -> None:
        self._acc_names     = [acc.name     for acc in self.accounts]
        self._acc_ids       = [acc.id       for acc in self.accounts]
        self._acc_platforms = [acc.platform for acc in self.accounts]


@_dataclasses.dataclass(kw_only = True)
class Account:
    name     : str      = None
    id       : _Any     = None
    platform : Platform = None


class Platform(_Enum):
    epic_games          = 0
    steam               = 1
    riot_games          = 2
    nintendo            = 3
    xbox_live           = 4
    playstation_network = 5
    origin              = 6
    activision_blizzard = 7
    battle_net          = 8


class PlayerConverter:
    def __init__(self) -> None:
        self.__players : list[Player] = []
        self.__uuids   : list[_Any]   = []
    

    def register(self, __player: Player, *, ignore: bool = True) -> None:
        if __player.uuid in self.__uuids:
            if not ignore:
                raise ValueError("a player with that uuid already exists")
            return
        self.__players.append(__player)
    

    def get_player_by_uuid(self, __uuid: _Any) -> _Optional[Player]:
        for __player in self.__players:
            if __player.uuid == __uuid:
                return __player
    

    def get_player_by_discord_id(self, __discord_id: _Any) -> _Optional[Player]:
        for __player in self.__players:
            if __player.discord_id == __discord_id:
                return __player
    

    def get_player_by_username(self, __username: str) -> _Optional[Player]:
        for __player in self.__players:
            if __player.username == __username:
                return __player
    

    def get_player_by_account_name(self, __account_name: str) -> _Optional[Player]:
        for __player in self.__players:
            if __account_name in __player._acc_names:
                return __player
    

    def get_player_by_account_id(self, __account_id: _Any) -> _Optional[Player]:
        for __player in self.__players:
            if __account_id in __player._acc_ids:
                return __player
    

    def get_player_by_account_platform(self, __account_platform: Platform) -> _Optional[Player]:
        for __player in self.__players:
            if __account_platform in __player._acc_platforms:
                return __player
    


@_dataclasses.dataclass
class RocketLeagueNCPGame:
    game_winner : str
    game_loser  : str


@_dataclasses.dataclass
class RocketLeagueNCPSeries:
    series_winner : str
    series_loser  : str
    league        : str = None
    conference    : str = None
    division      : str = None


@_dataclasses.dataclass
class RocketLeagueMacroStats:
    games_played       : int = None
    games_won          : int = None
    games_lost         : int = None
    games_won_by_ncp   : int = None
    games_lost_by_ncp  : int = None
    series_played      : int = None
    series_won         : int = None
    series_lost        : int = None
    series_won_by_ncp  : int = None
    series_lost_by_ncp : int = None
    duration           : int = None
    overtimes          : int = None
    overtime_seconds   : int = None


@_dataclasses.dataclass
class RocketLeagueBallStats:
    possession_time : float = None
    time_in_side    : float = None


@_dataclasses.dataclass
class RocketLeagueCoreStats:
    shots               : _types.num        = None
    shots_against       : _types.num        = None
    goals               : _types.num        = None
    goals_against       : _types.num        = None
    saves               : _types.num        = None
    assists             : _types.num        = None
    score               : _types.num        = None
    mvp                 : bool | _types.num = None
    shooting_percentage : _types.num        = None


@_dataclasses.dataclass
class RocketLeagueBoostStats:
    bpm                          : _types.num = None
    bcpm                         : _types.num = None
    avg_amount                   : _types.num = None
    amount_collected             : _types.num = None
    amount_stolen                : _types.num = None
    amount_collected_big         : _types.num = None
    amount_stolen_big            : _types.num = None
    amount_collected_small       : _types.num = None
    amount_stolen_small          : _types.num = None
    count_collected_big          : _types.num = None
    count_stolen_big             : _types.num = None
    count_collected_small        : _types.num = None
    count_stolen_small           : _types.num = None
    amount_overfill              : _types.num = None
    amount_overfill_stolen       : _types.num = None
    amount_used_while_supersonic : _types.num = None
    time_zero_boost              : _types.num = None
    percent_zero_boost           : _types.num = None
    time_full_boost              : _types.num = None
    percent_full_boost           : _types.num = None
    time_boost_0_25              : _types.num = None
    time_boost_25_50             : _types.num = None
    time_boost_50_75             : _types.num = None
    time_boost_75_100            : _types.num = None
    percent_boost_0_25           : _types.num = None
    percent_boost_25_50          : _types.num = None
    percent_boost_50_75          : _types.num = None
    percent_boost_75_100         : _types.num = None


@_dataclasses.dataclass
class RocketLeagueMovementStats:
    avg_speed                : _types.num = None
    total_distance           : _types.num = None
    time_supersonic_speed    : _types.num = None
    time_boost_speed         : _types.num = None
    time_slow_speed          : _types.num = None
    time_ground              : _types.num = None
    time_low_air             : _types.num = None
    time_high_air            : _types.num = None
    time_powerslide          : _types.num = None
    count_powerslide         : _types.num = None
    avg_powerslide_duration  : _types.num = None
    avg_speed_percentage     : _types.num = None
    percent_slow_speed       : _types.num = None
    percent_boost_speed      : _types.num = None
    percent_supersonic_speed : _types.num = None
    percent_ground           : _types.num = None
    percent_low_air          : _types.num = None
    percent_high_air         : _types.num = None


@_dataclasses.dataclass
class RocketLeaguePositioningStats:
    avg_distance_to_ball               : _types.num = None
    avg_distance_to_ball_possession    : _types.num = None
    avg_distance_to_ball_no_possession : _types.num = None
    avg_distance_to_mates              : _types.num = None
    time_defensive_third               : _types.num = None
    time_neutral_third                 : _types.num = None
    time_offensive_third               : _types.num = None
    time_defensive_half                : _types.num = None
    time_offensive_half                : _types.num = None
    time_behind_ball                   : _types.num = None
    time_infront_ball                  : _types.num = None
    time_most_back                     : _types.num = None
    time_most_forward                  : _types.num = None
    goals_against_while_last_defender  : _types.num = None
    time_closest_to_ball               : _types.num = None
    time_farthest_from_ball            : _types.num = None
    percent_defensive_third            : _types.num = None
    percent_offensive_third            : _types.num = None
    percent_neutral_third              : _types.num = None
    percent_defensive_half             : _types.num = None
    percent_offensive_half             : _types.num = None
    percent_behind_ball                : _types.num = None
    percent_infront_ball               : _types.num = None
    percent_most_back                  : _types.num = None
    percent_most_forward               : _types.num = None
    percent_closest_to_ball            : _types.num = None
    percent_farthest_from_ball         : _types.num = None


@_dataclasses.dataclass
class RocketLeagueDemoStats:
    inflicted : _types.num = None
    taken     : _types.num = None


@_dataclasses.dataclass
class RocketLeaguePlayerID:
    platform : str = None
    id       : str = None


@_dataclasses.dataclass
class RocketLeagueRank:
    id       : str = None
    tier     : int = None
    division : int = None
    name     : str = None
    mmr      : int = None


@_dataclasses.dataclass
class RocketLeagueCamera:
    fov              : int   = None
    height           : int   = None
    pitch            : int   = None
    distance         : int   = None
    stiffness        : float = None
    swivel_speed     : float = None
    transition_speed : float = None


@_dataclasses.dataclass
class BallchasingGroup:
    id   : str = None
    name : str = None
    link : str = None


@_dataclasses.dataclass
class BallchasingUploader: 
    steam_id    : str = None
    name        : str = None
    profile_url : str = None
    avatar      : str = None


@_dataclasses.dataclass
class RocketLeagueSeries:
    blue_team_name   : str
    orange_team_name : str
    games            : _Sequence[_Union[BallchasingReplay, RocketLeagueNCPGame]]
    league           : str = None
    conference       : str = None
    division         : str = None


    def identify_teams_by_roster_similarity(self) -> dict[str, str]:
        """Determines the team that played for each color for each game in a series based on initial starting rosters for each team."""
        ids: list[_Optional[dict[str, str]]] = []
        blue_roster                           = set()
        orange_roster                         = set()
        for game in self.games:
            if isinstance(game, RocketLeagueNCPGame):
                ids.append(None)
                continue
            if all(id is None for id in ids):
                ids.append({self.blue_team_name:"blue",self.orange_team_name:"orange"})
                blue_player_ids   = [player.id.id for player in game.blue.players]
                orange_player_ids = [player.id.id for player in game.orange.players]
                blue_roster      |= set(blue_player_ids)
                orange_roster    |= set(orange_player_ids)
                continue
            ids_temp          = {}
            blue_player_ids   = [player.id.id for player in game.blue.players]
            orange_player_ids = [player.id.id for player in game.orange.players]
            if _ext.list_similarity_score(blue_player_ids, blue_roster) >= _ext.list_similarity_score(blue_player_ids, orange_roster):
                ids_temp[self.blue_team_name]   = "blue"
                ids_temp[self.orange_team_name] = "orange"
                blue_roster   |= set(blue_player_ids)
                orange_roster |= set(orange_player_ids)
            else:
                ids_temp[self.blue_team_name]   = "orange"
                ids_temp[self.orange_team_name] = "blue"
                blue_roster   |= set(orange_player_ids)
                orange_roster |= set(blue_player_ids)
            ids.append(ids_temp)
        return ids


    def _get_match_results(self) -> list[tuple[tuple[str, int], tuple[str, int]]]:
        """Internal function used to get match results."""
        series_results: list[tuple[tuple[str, _Optional[int]], tuple[str, _Optional[int]]]] = []

        for team_colors, game in zip(self.identify_teams_by_roster_similarity(), self.games):
            if isinstance(game, RocketLeagueNCPGame):
                series_results.append(((game.game_winner, None), (game.game_loser, None)))
                continue
            team_1: BallchasingTeam = game.__getattribute__(team_colors[self.blue_team_name]) # team under blue_team_name
            team_2: BallchasingTeam = game.__getattribute__(team_colors[self.orange_team_name]) # team under orange_team_name
            series_results.append((
                (
                    self.blue_team_name if team_1.stats.core.goals > team_2.stats.core.goals else self.orange_team_name,
                    max([team_1.stats.core.goals, team_2.stats.core.goals])
                ),
                (
                    self.blue_team_name if team_1.stats.core.goals < team_2.stats.core.goals else self.orange_team_name,
                    min([team_1.stats.core.goals, team_2.stats.core.goals])
                )
            ))
        return series_results

    
    def _get_scoreline(self) -> tuple[tuple[str, int], tuple[str, int]]:
        """Internal function used to get the match scoreline."""
        scoreline = [0, 0]
        for [[winner, winner_score], [loser, loser_score]] in self._get_match_results():
            if winner == self.blue_team_name:
                scoreline[0] += 1
                continue
            if winner == self.orange_team_name:
                scoreline[1] += 1
                continue
        return ((self.blue_team_name, scoreline[0]), (self.orange_team_name, scoreline[1]))


    def get_winning_team(self) -> str:
        """Determines, then returns the name of the winning team."""
        scoreline = self._get_scoreline()
        return scoreline[0][0] if scoreline[0][1] > scoreline[1][1] else scoreline[1][0]


    def get_losing_team(self) -> str:
        """Determines, then returns the name of the losing team."""
        scoreline = self._get_scoreline()
        return scoreline[0][0] if scoreline[0][1] < scoreline[1][1] else scoreline[1][0]
        

    def get_winning_score(self) -> int:
        scoreline = self._get_scoreline()
        return max([i[1] for i in scoreline])
        
        
    def get_losing_score(self) -> int:
        scoreline = self._get_scoreline()
        return min([i[1] for i in scoreline])


class RocketLeagueStatBlock:


    def from_dict(
        __stats: dict
    ) -> RocketLeagueStatBlock:
            sb = RocketLeagueStatBlock()
            sb.ball        = sb.ball(**__stats["ball"])               if "ball" in __stats        else sb.ball()
            sb.core        = sb.core(**__stats["core"])               if "core" in __stats        else sb.core()
            sb.boost       = sb.boost(**__stats["boost"])             if "boost" in __stats       else sb.boost()
            sb.movement    = sb.movement(**__stats["movement"])       if "movement" in __stats    else sb.movement()
            sb.positioning = sb.positioning(**__stats["positioning"]) if "positioning" in __stats else sb.positioning()
            sb.demo        = sb.demo(**__stats["demo"])               if "demo" in __stats        else sb.demo()
            sb.macro       = sb.macro(**__stats["macro"])             if "macro" in __stats       else sb.macro()
            return sb

    
    def from_components(
        macro_stats       : _Optional[RocketLeagueMacroStats],
        ball_stats        : _Optional[RocketLeagueBallStats],
        core_stats        : _Optional[RocketLeagueCoreStats],
        boost_stats       : _Optional[RocketLeagueBoostStats],
        movement_stats    : _Optional[RocketLeagueMovementStats],
        positioning_stats : _Optional[RocketLeaguePositioningStats],
        demo_stats        : _Optional[RocketLeagueDemoStats]
    ) -> RocketLeagueStatBlock:
        sb = RocketLeagueStatBlock()
        sb.macro       = macro_stats       or sb.macro()
        sb.ball        = ball_stats        or sb.ball()
        sb.core        = core_stats        or sb.core()
        sb.boost       = boost_stats       or sb.boost()
        sb.movement    = movement_stats    or sb.movement()
        sb.positioning = positioning_stats or sb.positioning()
        sb.demo        = demo_stats        or sb.demo()
        return sb


    class macro(RocketLeagueMacroStats): ...
    class ball(RocketLeagueBallStats): ...
    class core(RocketLeagueCoreStats): ...
    class boost(RocketLeagueBoostStats): ...
    class movement(RocketLeagueMovementStats): ...
    class positioning(RocketLeaguePositioningStats): ...
    class demo(RocketLeagueDemoStats): ...


class BallchasingPlayer:
    start_time           : int              = None
    end_time             : float            = None
    name                 : str              = None
    car_id               : int              = None
    car_name             : str              = None
    steering_sensitivity : float            = None
    
    @staticmethod
    def from_dict(
        __player        : dict
    ) -> BallchasingPlayer:
        player = BallchasingPlayer()
        player.start_time           = __player["start_time"]           if "start_time"           in __player else None
        player.end_time             = __player["end_time"]             if "end_time"             in __player else None
        player.name                 = __player["name"]                 if "name"                 in __player else None
        player.car_id               = __player["car_id"]               if "car_id"               in __player else None
        player.steering_sensitivity = __player["steering_sensitivity"] if "steering_sensitivity" in __player else None
        player.id                   = player.id(**__player["id"])
        player.camera               = player.camera(**__player["camera"])
        player.stats                = player.stats.from_dict(__player["stats"])
        if "car_name" in __player:
            player.car_name = __player["car_name"]
        if "rank" in __player:
            player.rank = player.rank(**__player["rank"])
        else:
            player.rank = player.rank()
        return player
    
    @staticmethod
    def from_components(
        *,
        start_time           : int                   = None,
        end_time             : float                 = None,
        name                 : str                   = None,
        car_id               : int                   = None,
        car_name             : str                   = None,
        steering_sensitivity : float                 = None,
        id                   : RocketLeaguePlayerID  = None,
        camera               : RocketLeagueCamera    = None,
        rank                 : RocketLeagueRank      = None,
        stats                : RocketLeagueStatBlock = None
    ) -> BallchasingPlayer:
        player = BallchasingPlayer()
        player.start_time           = start_time
        player.end_time             = end_time
        player.name                 = name
        player.car_id               = car_id
        player.car_name             = car_name
        player.steering_sensitivity = steering_sensitivity
        player.id                   = id     or player.id()
        player.camera               = camera or player.camera()
        player.rank                 = rank   or player.rank()
        player.stats                = stats  or player.stats()
        return player


    class id(RocketLeaguePlayerID): ...
    class camera(RocketLeagueCamera): ...
    class rank(RocketLeagueRank): ...
    class stats(RocketLeagueStatBlock): ...


class BallchasingTeam:


    color   : str                     = None
    name    : str                     = None
    players : list[BallchasingPlayer] = None


    def from_dict(__team: dict) -> BallchasingTeam:
        team         = BallchasingTeam()
        team.color   = __team["color"] if "color" in __team else None
        team.name    = __team["name"]  if "name"  in __team else None
        players      = []
        for player in __team["players"]:
            player["stats"]["ball"] = {
                "possession_time" : __team["stats"]["ball"]["possession_time"],
                "time_in_side" : __team["stats"]["ball"]["time_in_side"]
            }
            players.append(BallchasingPlayer.from_dict(player))
        team.players = players
        team.stats   = team.stats.from_dict(__team["stats"])
        return team


    def from_components(
        *,
        color   : str                     = None,
        name    : str                     = None,
        players : list[BallchasingPlayer] = None,
        stats   : RocketLeagueStatBlock   = None
    ) -> BallchasingTeam:
        team         = BallchasingTeam()
        team.color   = color
        team.name    = name
        team.players = players
        team.stats   = stats or team.stats()
        return team


    class stats(RocketLeagueStatBlock): ...


class BallchasingReplay:
    id                : str                         = None
    link              : str                         = None
    created           : str                         = None
    status            : str                         = None
    rocket_league_id  : str                         = None
    match_guid        : str                         = None
    title             : str                         = None
    map_code          : str                         = None
    match_type        : str                         = None
    team_size         : int                         = None
    playlist_id       : str                         = None
    duration          : int                         = None
    overtime          : bool                        = None
    overtime_seconds  : int                         = None
    season            : int                         = None
    season_type       : str                         = None
    date              : str                         = None
    date_has_timezone : bool                        = None
    visibility        : str                         = None
    playlist_name     : str                         = None
    map_name          : str                         = None


    def from_dict(__replay: dict) -> BallchasingReplay:
        replay = BallchasingReplay()
        replay.id                = __replay["id"]                if "id"                in __replay else None
        replay.link              = __replay["link"]              if "link"              in __replay else None
        replay.created           = __replay["created"]           if "created"           in __replay else None
        replay.status            = __replay["status"]            if "status"            in __replay else None
        replay.rocket_league_id  = __replay["rocket_league_id"]  if "rocket_league_id"  in __replay else None
        replay.match_guid        = __replay["match_guid"]        if "match_guid"        in __replay else None
        replay.title             = __replay["title"]             if "title"             in __replay else None
        replay.map_code          = __replay["map_code"]          if "map_code"          in __replay else None
        replay.match_type        = __replay["match_type"]        if "match_type"        in __replay else None
        replay.team_size         = __replay["team_size"]         if "team_size"         in __replay else None
        replay.playlist_id       = __replay["playlist_id"]       if "playlist_id"       in __replay else None
        replay.duration          = __replay["duration"]          if "duration"          in __replay else None
        replay.overtime          = __replay["overtime"]          if "overtime"          in __replay else None
        replay.overtime_seconds  = __replay["overtime_seconds"]  if "overtime_seconds"  in __replay else None
        replay.season            = __replay["season"]            if "season"            in __replay else None
        replay.season_type       = __replay["season_type"]       if "season_type"       in __replay else None
        replay.date              = __replay["date"]              if "date"              in __replay else None
        replay.date_has_timezone = __replay["date_has_timezone"] if "date_has_timezone" in __replay else None
        replay.visibility        = __replay["visibility"]        if "visibility"        in __replay else None
        replay.playlist_name     = __replay["playlist_name"]     if "playlist_name"     in __replay else None
        replay.map_name          = __replay["map_name"]          if "map_name"          in __replay else None
        replay.groups            = replay.groups([BallchasingGroup(**group) for group in __replay["groups"]]) if "groups" in __replay else replay.groups()
        replay.max_rank          = replay.max_rank(**__replay["max_rank"]) if "max_rank" in __replay else replay.max_rank()
        replay.min_rank          = replay.min_rank(**__replay["min_rank"]) if "min_rank" in __replay else replay.min_rank()
        replay.uploader          = replay.uploader(**__replay["uploader"])
        replay.blue              = replay.blue.from_dict(__replay["blue"])
        replay.orange              = replay.orange.from_dict(__replay["orange"])
        return replay


    def from_components(
        id                : str                    = None,
        link              : str                    = None,
        created           : str                    = None,
        status            : str                    = None,
        rocket_league_id  : str                    = None,
        match_guid        : str                    = None,
        title             : str                    = None,
        map_code          : str                    = None,
        match_type        : str                    = None,
        team_size         : int                    = None,
        playlist_id       : str                    = None,
        duration          : int                    = None,
        overtime          : bool                   = None,
        overtime_seconds  : int                    = None,
        season            : int                    = None,
        season_type       : str                    = None,
        date              : str                    = None,
        date_has_timezone : bool                   = None,
        visibility        : str                    = None,
        playlist_name     : str                    = None,
        map_name          : str                    = None,
        groups            : list[BallchasingGroup] = None,
        max_rank          : RocketLeagueRank       = None,
        min_rank          : RocketLeagueRank       = None,
        uploader          : BallchasingUploader    = None,
        blue              : BallchasingTeam        = None,
        orange            : BallchasingTeam        = None
    ) -> BallchasingReplay:
        replay = BallchasingReplay()
        replay.id                = id
        replay.link              = link
        replay.created           = created
        replay.status            = status
        replay.rocket_league_id  = rocket_league_id
        replay.match_guid        = match_guid
        replay.title             = title
        replay.map_code          = map_code
        replay.match_type        = match_type
        replay.team_size         = team_size
        replay.playlist_id       = playlist_id
        replay.duration          = duration
        replay.overtime          = overtime
        replay.overtime_seconds  = overtime_seconds
        replay.season            = season
        replay.season_type       = season_type
        replay.date              = date
        replay.date_has_timezone = date_has_timezone
        replay.visibility        = visibility
        replay.playlist_name     = playlist_name
        replay.map_name          = map_name
        replay.groups            = groups   or replay.groups()
        replay.max_rank          = max_rank or replay.max_rank()
        replay.min_rank          = min_rank or replay.min_rank()
        replay.uploader          = uploader or replay.uploader()
        replay.blue              = blue     or replay.blue()
        replay.orange            = orange   or replay.orange()
        return replay


    class groups(list[BallchasingGroup]): ...
    class max_rank(RocketLeagueRank): ...
    class min_rank(RocketLeagueRank): ...
    class uploader(BallchasingUploader): ...
    class blue(BallchasingTeam): ...
    class orange(BallchasingTeam): ...


    def get_winning_team(self) -> BallchasingTeam:
        return self.blue if self.blue.stats.core.goals > self.orange.stats.core.goals else self.orange


    def get_losing_team(self) -> BallchasingTeam:
        return self.blue if self.blue.stats.core.goals < self.orange.stats.core.goals else self.orange


class SQLiteCredentials:
    sqlite_connections: dict[str, __sqlite3.Connection] = {}


@_dataclasses.dataclass
class RocketLeagueMatchDatabaseRow:
    id                                                   : int                         = None
    league                                               : _Optional[str]               = None
    conference                                           : _Optional[str]               = None
    division                                             : _Optional[str]               = None
    header                                               : str                         = None
    series_id                                            : int                         = None
    series_winner                                        : str                         = None
    series_loser                                         : str                         = None
    series_winner_score                                  : int                         = None
    series_loser_score                                   : int                         = None
    replay_id                                            : _Optional[str]               = None
    game_start_time                                      : _Optional[int]               = None
    game_id                                              : int                         = None
    game_winner                                          : str                         = None
    game_loser                                           : str                         = None
    game_winner_score                                    : int                         = None
    game_loser_score                                     : int                         = None
    overtime                                             : _Optional[bool]              = None
    overtime_seconds                                     : _Optional[int]               = None
    duration                                             : _Optional[int]               = None
    team                                                 : _Optional[str]               = None
    t_color                                              : _Optional[str]               = None
    player_id                                            : _Optional[int]               = None
    name                                                 : _Optional[str]               = None
    car_id                                               : _Optional[int]               = None
    car_name                                             : _Optional[str]               = None
    steering_sensitivity                                 : _Optional[float]             = None
    rank_id                                              : _Optional[str]               = None
    rank_tier                                            : _Optional[int]               = None
    rank_division                                        : _Optional[int]               = None
    rank_name                                            : _Optional[str]               = None
    id_platform                                          : _Optional[str]               = None
    id_id                                                : _Optional[str]               = None
    camera_fov                                           : _Optional[int]               = None
    camera_height                                        : _Optional[int]               = None
    camera_pitch                                         : _Optional[int]               = None
    camera_distance                                      : _Optional[int]               = None
    camera_stiffness                                     : _Optional[float]             = None
    camera_swivel_speed                                  : _Optional[float]             = None
    camera_transition_speed                              : _Optional[float]             = None
    stats_ball_possession_time                           : _Optional[float]             = None
    stats_ball_time_in_side                              : _Optional[float]             = None
    stats_core_shots                                     : _Optional[_types.num]        = None
    stats_core_shots_against                             : _Optional[_types.num]        = None
    stats_core_goals                                     : _Optional[_types.num]        = None
    stats_core_goals_against                             : _Optional[_types.num]        = None
    stats_core_saves                                     : _Optional[_types.num]        = None
    stats_core_assists                                   : _Optional[_types.num]        = None
    stats_core_score                                     : _Optional[_types.num]        = None
    stats_core_mvp                                       : _Optional[bool | _types.num] = None
    stats_core_shooting_percentage                       : _Optional[_types.num]        = None
    stats_boost_bpm                                      : _Optional[_types.num]        = None
    stats_boost_bcpm                                     : _Optional[_types.num]        = None
    stats_boost_avg_amount                               : _Optional[_types.num]        = None
    stats_boost_amount_collected                         : _Optional[_types.num]        = None
    stats_boost_amount_stolen                            : _Optional[_types.num]        = None
    stats_boost_amount_collected_big                     : _Optional[_types.num]        = None
    stats_boost_amount_stolen_big                        : _Optional[_types.num]        = None
    stats_boost_amount_collected_small                   : _Optional[_types.num]        = None
    stats_boost_amount_stolen_small                      : _Optional[_types.num]        = None
    stats_boost_count_collected_big                      : _Optional[_types.num]        = None
    stats_boost_count_stolen_big                         : _Optional[_types.num]        = None
    stats_boost_count_collected_small                    : _Optional[_types.num]        = None
    stats_boost_count_stolen_small                       : _Optional[_types.num]        = None
    stats_boost_amount_overfill                          : _Optional[_types.num]        = None
    stats_boost_amount_overfill_stolen                   : _Optional[_types.num]        = None
    stats_boost_amount_used_while_supersonic             : _Optional[_types.num]        = None
    stats_boost_time_zero_boost                          : _Optional[_types.num]        = None
    stats_boost_percent_zero_boost                       : _Optional[_types.num]        = None
    stats_boost_time_full_boost                          : _Optional[_types.num]        = None
    stats_boost_percent_full_boost                       : _Optional[_types.num]        = None
    stats_boost_time_boost_0_25                          : _Optional[_types.num]        = None
    stats_boost_time_boost_25_50                         : _Optional[_types.num]        = None
    stats_boost_time_boost_50_75                         : _Optional[_types.num]        = None
    stats_boost_time_boost_75_100                        : _Optional[_types.num]        = None
    stats_boost_percent_boost_0_25                       : _Optional[_types.num]        = None
    stats_boost_percent_boost_25_50                      : _Optional[_types.num]        = None
    stats_boost_percent_boost_50_75                      : _Optional[_types.num]        = None
    stats_boost_percent_boost_75_100                     : _Optional[_types.num]        = None
    stats_movement_avg_speed                             : _Optional[_types.num]        = None
    stats_movement_total_distance                        : _Optional[_types.num]        = None
    stats_movement_time_supersonic_speed                 : _Optional[_types.num]        = None
    stats_movement_time_boost_speed                      : _Optional[_types.num]        = None
    stats_movement_time_slow_speed                       : _Optional[_types.num]        = None
    stats_movement_time_ground                           : _Optional[_types.num]        = None
    stats_movement_time_low_air                          : _Optional[_types.num]        = None
    stats_movement_time_high_air                         : _Optional[_types.num]        = None
    stats_movement_time_powerslide                       : _Optional[_types.num]        = None
    stats_movement_count_powerslide                      : _Optional[_types.num]        = None
    stats_movement_avg_powerslide_duration               : _Optional[_types.num]        = None
    stats_movement_avg_speed_percentage                  : _Optional[_types.num]        = None
    stats_movement_percent_slow_speed                    : _Optional[_types.num]        = None
    stats_movement_percent_boost_speed                   : _Optional[_types.num]        = None
    stats_movement_percent_supersonic_speed              : _Optional[_types.num]        = None
    stats_movement_percent_ground                        : _Optional[_types.num]        = None
    stats_movement_percent_low_air                       : _Optional[_types.num]        = None
    stats_movement_percent_high_air                      : _Optional[_types.num]        = None
    stats_positioning_avg_distance_to_ball               : _Optional[_types.num]        = None
    stats_positioning_avg_distance_to_ball_possession    : _Optional[_types.num]        = None
    stats_positioning_avg_distance_to_ball_no_possession : _Optional[_types.num]        = None
    stats_positioning_avg_distance_to_mates              : _Optional[_types.num]        = None
    stats_positioning_time_defensive_third               : _Optional[_types.num]        = None
    stats_positioning_time_neutral_third                 : _Optional[_types.num]        = None
    stats_positioning_time_offensive_third               : _Optional[_types.num]        = None
    stats_positioning_time_defensive_half                : _Optional[_types.num]        = None
    stats_positioning_time_offensive_half                : _Optional[_types.num]        = None
    stats_positioning_time_behind_ball                   : _Optional[_types.num]        = None
    stats_positioning_time_infront_ball                  : _Optional[_types.num]        = None
    stats_positioning_time_most_back                     : _Optional[_types.num]        = None
    stats_positioning_time_most_forward                  : _Optional[_types.num]        = None
    stats_positioning_goals_against_while_last_defender  : _Optional[_types.num]        = None
    stats_positioning_time_closest_to_ball               : _Optional[_types.num]        = None
    stats_positioning_time_farthest_from_ball            : _Optional[_types.num]        = None
    stats_positioning_percent_defensive_third            : _Optional[_types.num]        = None
    stats_positioning_percent_offensive_third            : _Optional[_types.num]        = None
    stats_positioning_percent_neutral_third              : _Optional[_types.num]        = None
    stats_positioning_percent_defensive_half             : _Optional[_types.num]        = None
    stats_positioning_percent_offensive_half             : _Optional[_types.num]        = None
    stats_positioning_percent_behind_ball                : _Optional[_types.num]        = None
    stats_positioning_percent_infront_ball               : _Optional[_types.num]        = None
    stats_positioning_percent_most_back                  : _Optional[_types.num]        = None
    stats_positioning_percent_most_forward               : _Optional[_types.num]        = None
    stats_positioning_percent_closest_to_ball            : _Optional[_types.num]        = None
    stats_positioning_percent_farthest_from_ball         : _Optional[_types.num]        = None
    stats_demo_inflicted                                 : _Optional[int]               = None
    stats_demo_taken                                     : _Optional[int]               = None
