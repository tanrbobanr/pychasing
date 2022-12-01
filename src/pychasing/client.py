"""The core functionality code for the wrapper.

:copyright: (c) 2022-present Tanner B. Corcoran
:license: MIT, see LICENSE for more details.
"""

__author__ = "Tanner B. Corcoran"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2022-present Tanner B. Corcoran"


from . import rate_limit
from . import enums
from . import models
import requests
import typing
import httpprep
import prepr

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


def _print_error(response: requests.Response) -> None:
    """Print out an error code from a `requests.Response` if an HTTP error is
    encountered.
    
    """
    error_side = ("Client" if 400 <= response.status_code < 500 else "Server"
                  if 500 <= response.status_code < 600 else None)
    if error_side:
        if isinstance(response.reason, bytes):
            try:
                reason = response.reason.decode("utf-8")
            except UnicodeDecodeError:
                reason = response.reason.decode("iso-8859-1")
        else:
            reason = response.reason
        try:
            response_json = response.json()
        except requests.JSONDecodeError:
            response_json = None
        error_description = ""
        if response_json and "error" in response_json:
            error_description = "(" + response_json["error"] + ") "
            
        print(f"\033[93m{response.status_code} {error_side} Error: {reason} "
              f"{error_description}for url: {response.url}\033[0m")


def p(v):
    """Return `v` if `v` is `...` or a `str`, else return `v.value`.
    
    """
    return v if v == ... or isinstance(v, str) else v.value


class Client:
    """The main class used to interact with the Ballchasing API.
    
    """
    def __init__(self, token: str, auto_rate_limit: bool,
                 patreon_tier: enums.PatreonTier,
                 rate_limit_safe_start: bool = False) -> None:
        """
        Arguments
        ---------
        token : str
            A ballchasing API key (acquirable
            from https://ballchasing.com/upload).
        auto_rate_limit : bool
            If `True`, the client will automatically limit API calls according
            to the given Patreon tier.
        patreon_tier : enums.PatreonTier
            The token-holder's Ballchasing Patreon tier.
        rate_limit_safe_start : bool, optional, default=False
            If `True`, the rate limiter will start out as fully maxed out on API
            calls.

        """
        self._token = token
        self._auto_rate_limit = auto_rate_limit
        self._patreon_tier: typing.Dict[enums.Operation, typing.Tuple[int, ...]] = (
            patreon_tier.value)
        self._rate_limit_safe_start = rate_limit_safe_start
        if auto_rate_limit:
            self._rate_limiters = {k:rate_limit.RateLimit(*v,
                                         safe_start=rate_limit_safe_start)
                                   for k, v in self._patreon_tier.items()}

    def __repr__(self, *args, **kwargs) -> prepr.pstr:
        return prepr.prepr(self).args(self._token, self._auto_rate_limit,
            self._patreon_tier).kwarg("rate_limit_safe_start",
            self._rate_limit_safe_start, False).build(*args, **kwargs)
    
    def ping(self, *, print_error: bool = True) -> requests.Response:
        """Ping the https://ballchasing.com servers.

        Arguments
        ---------
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        """
        # prepare URL
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["api"]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token
        
        # make request, print error, and return response
        response = requests.get(prepped_url.build(), headers=
                                prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response

    def upload_replay(self, file: typing.BinaryIO,
                      visibility: typing.Union[str, enums.Visibility],
                      *, group: str  = ...,
                      print_error: bool = True) -> requests.Response:
        """Upload a replay to https://ballchasing.com.

        Parameters
        ----------
        file : BinaryIO
            The `.replay` file to be uploaded.
        visibility : str or Visibility
            The visibility of the replay once uploaded.
        group : str, optional
            The group to assign this replay to once it is uploaded.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        """
        # prepare URL
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["api", "v2", "upload"]
        )
        prepped_url.components.queries["visibility", "group"] = [
                p(visibility), group]

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token
        
        # make request, print error, and return response
        response = requests.post(prepped_url.build(query_check=...),
                                 headers=prepped_headers.format_dict(),
                                 files={"file":file})
        if print_error:
            _print_error(response)
        return response

    def list_replays(self, *, next: str = ..., title: str = ...,
                     player_names: typing.List[str] = ...,
                     player_ids: typing.List[typing.Tuple[str, typing.Union[
                        int, str]]] = ...,
                     playlists: typing.List[typing.Union[str, 
                        enums.Playlist]] = ...,
                     season: typing.Union[str, enums.Season] = ...,
                     match_result: typing.Union[str, enums.MatchResult] = ...,
                     min_rank: typing.Union[str, enums.Rank] = ...,
                     max_rank: typing.Union[str, enums.Rank] = ...,
                     pro: bool = ...,
                     uploader: typing.Union[Literal["me"], str, int]  = ...,
                     group: str = ..., map: typing.Union[str, enums.Map] = ...,
                     created_before: typing.Union[models.Date, str] = ...,
                     created_after: typing.Union[models.Date, str] = ...,
                     replay_date_before: typing.Union[models.Date, str] = ...,
                     replay_date_after: typing.Union[models.Date, str] = ...,
                     count: int = ...,
                     sort_by: typing.Union[str, enums.ReplaySortBy] = ...,
                     sort_dir: typing.Union[str, enums.SortDirection] = ...,
                     print_error: bool = True) -> requests.Response:
        """List replays filtered by various criteria.

        Parameters
        ----------
        next : str, optional
            A continuation URL (which can be acquired with
            `<response from list_replays>.json()["next"]`). If defined, all
            other arguments will be ignored.
        title : str, optional
            Only include replays with the given title.
        player_names : list of str, optional
            Only include replays that include the given player(s) by display
            name.
        player_ids : list of tuple of str and (int or str), optional
            Only include replays that include the given player(s) by platform
            [0] and player ID [1].
        playlist : list of (str or Playlist), optional
            Only include replays in the given playlist(s).
        season : str or Season, optional
            Only include replays played in a given season.
        match_result : str or MatchResult, optional
            Only include replays that resulted in the given result (win/loss).
        min_rank : str or Rank, optional
            Only include replays where all players are above a given minimum
            rank.
        max_rank : str or Rank, optional
            Only include replays where all players are above a given maximum
            rank.
        pro : bool, optional
            Only include replays where at least one player in the lobby is a pro
            player.
        uploader : "me" or int or str, optional
            Only include replays uploaded by the given user. If the value is set
            to "me", then only replays uploaded by the token holder will be
            returned, or if a SteamID64 is used, only replays uploaded by the
            given steam user will be returned.
        group : str, optional
            Only include replays that are direct children of the given group.
        map : str or Map, optional
            Only include replays played on a specific map.
        created_before : Date or str, optional
            Only include replays created before a given date, formatted as an
            RFC3339 datetime string.
        created_after : Date or str, optional
            Only include replays created after a given date, formatted as an
            RFC3339 datetime string.
        replay_date_before : Date or str, optional
            Only include replays played before a given date, formatted as an
            RFC3339 datetime string.
        replay_date_after : Date or str, optional
            Only include replays played after a given date, formatted as an
            RFC3339 datetime string.
        count : int, optional, default=150
            The number of replays returned. Must be between 1 and 200 
            (inclusive) if defined.
        sort_by : str or ReplaySortBy, optional, default=
        ReplaySortBy.upload_date
            Whether to sort by replay date or upload date.
        sort_dir : str or SortDirection, optional, default=SortDirection.desc
            Whether to sort descending or ascending.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        Raises:
            ValueError: `count` is defined and is less than 0 or greater than
            200.
        
        """
        if count != ... and 1 > count > 200:
            raise ValueError("\"count\" must be between 1 and 200")

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token

        # make request
        if next != ...:
            # set url
            url = next
        else:
            # prepare url
            prepped_url = httpprep.URL(
                protocol="https",
                domain="ballchasing",
                top_level_domain="com",
                path_segments=["api", "replays"]
            )
            prepped_url.components.queries[
                "title", "season", "match-result", "min-rank", "max-rank",
                "pro", "uploader", "group", "map", "created-before",
                "created-after", "replay-date-before", "replay-date-after",
                "count", "sort-by", "sort-dir"] = [
                title, p(season), p(match_result), p(min_rank), p(max_rank),
                str(pro).lower() if isinstance(pro, bool) else ...,
                uploader, group, p(map), created_before, created_after,
                replay_date_before, replay_date_after, count, p(sort_by),
                p(sort_dir)]
            if player_names != ...:
                for name in player_names:
                    prepped_url.components.queries["player-name"] = name
            if player_ids != ...:
                for platform, id in player_ids:
                    prepped_url.components.queries["player-id"] = (f"{platform}"
                                                                   f":{id}")
            if playlists != ...:
                for playlist in playlists:
                    prepped_url.components.queries["playlist"] = p(playlist)
            url = prepped_url.build(query_check=...)

        # rate limit if enabled
        if self._auto_rate_limit:
            self._rate_limiters[enums.Operation.list_replays]()

        # make request, print error, and return response
        response = requests.get(url, headers=prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
    
    def get_replay(self, replay_id: str, *,
                   print_error: bool = True) -> requests.Response:
        """Get more in-depth information for a specific replay.

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["api", "replays", replay_id]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token

        # rate limit if enabled
        if self._auto_rate_limit:
            self._rate_limiters[enums.Operation.get_replay]()

        # make request, print error, and return response
        response = requests.get(prepped_url.build(), headers=
                                prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
        
    def delete_replay(self, replay_id: str, *,
                      print_error: bool = True) -> requests.Response:
        """Delete the given replay from https://ballchasing.com, so long as the
        replay is owned by the token holder.

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["api", "replays", replay_id]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token

        # rate limit if enabled
        if self._auto_rate_limit:
            self._rate_limiters[enums.Operation.delete_replay]()

        # make request, print error, and return response
        response = requests.delete(prepped_url.build(), headers=
                                   prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
        
    def patch_replay(self, replay_id: str, *, title: str = ...,
                     visibility: typing.Union[str, enums.Visibility] = ...,
                     group: str = ...,
                     print_error: bool = True) -> requests.Response:
        """Patch the title, visibility, and/or group of a replay on
        https://ballchasing.com, so long as the replay is owned by the token
        holder.

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        title : str, optional
            Set the title of the replay.
        visibility : str or Visibility, optional
            Set the visibility of the replay.
        group : str, optional
            Set the group of the replay. An empty string (`""`) will set the
            group to none.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["api", "replays", replay_id]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token

        # prepare payload
        payload = httpprep.OverloadDict()
        payload["title", "visibility", "group"] = [title, p(visibility), group]

        # rate limit if enabled
        if self._auto_rate_limit:
            self._rate_limiters[enums.Operation.patch_replay]()

        # make request, print error, and return response
        response = requests.patch(prepped_url.build(),
                                  headers=prepped_headers.format_dict(),
                                  json=payload.remove_values(...).to_dict())
        if print_error:
            _print_error(response)
        return response

    def download_replay(self, replay_id: str, *,
                        print_error: bool = True) -> requests.Response:
        """Download a replay from https://ballchasing.com.

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Warnings
        --------
        Replay files can be rather large (up to around 1.5mb). The HTTP request
        is set to `stream`, thus you should use `iter_content` when saving the
        replay to a file.

        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["api", "replays", replay_id, "file"]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token

        # rate limit if enabled
        if self._auto_rate_limit:
            self._rate_limiters[enums.Operation.download_replay]()

        # make request, print error, and return response
        response = requests.get(prepped_url.build(),
                                headers=prepped_headers.format_dict(),
                                stream=True)
        if print_error:
            _print_error(response)
        return response

    def create_group(self, name: str,
                     player_identification: typing.Union[str,
                        enums.PlayerIdentification],
                     team_identification: typing.Union[str,
                        enums.TeamIdentification], *,
                     parent: str = ...,
                     print_error: bool = True) -> requests.Response:
        """Create a replay group on https://ballchasing.com.

        Parameters
        ----------
        name : str
            The name of the group.
        player_identification : str or PlayerIdentification
            Determines how to identify the same player across multiple replays -
            by account name, or account ID.
        team_identification : str or TeamIdentification
            Determines how to identify the same team across multiple replays -
            by distinct players (if teams have fixed rosters for every single
            games), or by player clusters (if subs are allowed between games).
        parent : str, optional
            The parent group (group ID) to set as the parent of this group.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).

        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["api", "groups"]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token

        # prepare payload
        payload = httpprep.OverloadDict()
        payload["name", "player_identification", "team_identification",
                "parent"] = [name, p(player_identification),
                             p(team_identification), parent]

        # rate limit if enabled
        if self._auto_rate_limit:
            self._rate_limiters[enums.Operation.create_group]()

        # make request, print error, and return response
        response = requests.post(prepped_url.build(), headers=
                                 prepped_headers.format_dict(),
                                 json=payload.remove_values(...).to_dict())
        if print_error:
            _print_error(response)
        return response
        
    def list_groups(self, *, next: str = ..., name: str = ...,
                    creator: typing.Union[str, int] = ..., group: str = ...,
                    created_before: typing.Union[models.Date, str] = ...,
                    created_after: typing.Union[models.Date, str] = ...,
                    count: int = ...,
                    sort_by: typing.Union[str, enums.GroupSortBy] = ...,
                    sort_dir: typing.Union[str, enums.SortDirection] = ...,
                    print_error: bool = True) -> requests.Response:
        """List replay groups from https://ballchasing.com filtered by various
        criteria.

        Parameters
        ----------
        next : str, optional
            A continuation URL (which can be acquired with
            `<response from list_groups>.json()["next"]`). If defined, all
            other arguments will be ignored.
        name : str, optional
            Only include groups whose title contains the given text.
        creator : str or int, optional
            Only include replays uploaded by the given user (defined by a
            `SteamID64`).
        group : str, optional
            Only include replays that are direct or indirect children of the
            given group (defined by a group ID).
        created_before : Date or str, optional
            Only include groups created before a given date, formatted as an
            RFC3339 datetime string.
        created_after : Date or str, optional
            Only include groups created after a given date, formatted as an
            RFC3339 datetime string.
        count : int, optional, default=150
            The number of groups returned. Must be between 1 and 200 (inclusive)
            if defined.
        sort_by : str | GroupSortBy, optional, default=GroupSortBy.created
            Whether to sort by creation date or name. Keywords for this variable
            can be accessed through the `pychasing.types.SortBy` class.
        sort_dir : str | SortDirection, optional, default=SortDirection.desc
            Whether to sort descending or ascending. Keywords for this variable
            can be accessed through the `pychasing.types.SortDir` class.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).

        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        Raises:
            ValueError: `count` is defined and is less than 0 or greater than
            200.
        
        """
        if count != ... and 1 > count > 200:
            raise ValueError("\"count\" must be between 1 and 200")
        
        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token

        # make request
        if next != ...:
            # set url
            url = next
        else:
            # prepare url
            prepped_url = httpprep.URL(
                protocol="https",
                domain="ballchasing",
                top_level_domain="com",
                path_segments=["api", "groups"]
            )
            prepped_url.components.queries["name", "creator", "group",
                                           "created-before", "created-after",
                                           "count", "sort-by", "sort-dir"] = [
                                           name, creator, group, created_before,
                                           created_after, count, p(sort_by),
                                           p(sort_dir)]
            url = prepped_url.build(query_check=...)

        # rate limit if enabled
        if self._auto_rate_limit:
            self._rate_limiters[enums.Operation.list_groups]()

        # make request, print error, and return response
        response = requests.get(url, headers=prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response

    def get_group(self, group_id: str, *,
                  print_error: bool = True) -> requests.Response:
        """Get information on a specific replay group from
        https://ballchasing.com.

        Parameters
        ----------
        group_id : str
            The ID of the group present in ballchasing's systems.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["api", "groups", group_id]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token

        # rate limit if enabled
        if self._auto_rate_limit:
            self._rate_limiters[enums.Operation.get_group]()

        # make request, print error, and return response
        response = requests.get(prepped_url.build(), headers=
                                prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
    
    def delete_group(self, group_id: str, *,
                     print_error: bool = True) -> requests.Response:
        """Delete a specific group (and all children groups) from
        https://ballchasing.com, so long as it is owned by the token holder.

        Parameters
        ----------
        group_id : str
            The ID of the group present in ballchasing's systems.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["api", "groups", group_id]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token

        # rate limit if enabled
        if self._auto_rate_limit:
            self._rate_limiters[enums.Operation.delete_group]()

        # make request, print error, and return response
        response = requests.delete(prepped_url.build(), headers=
                                   prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
    
    def patch_group(self, group_id: str, *,
        player_identification: typing.Union[str,
            enums.PlayerIdentification] = ...,
        team_identification: typing.Union[str, enums.TeamIdentification] = ...,
        parent: str = ..., shared: bool = ...,
        print_error: bool = True) -> requests.Response:
        """Delete a specific group (and all children groups) from
        https://ballchasing.com, so long as it is owned by the token holder.

        Parameters
        ----------
        group_id : str
            The ID of the group present in ballchasing's systems.
        player_identification : str or PlayerIdentification, optional
            Determines how to identify the same player across multiple replays -
            by account name, or account ID.
        team_identification : str or TeamIdentification, optional
            Determines how to identify the same team across multiple replays -
            by distinct players (if teams have fixed rosters for every single
            games), or by player clusters (if subs are allowed between games).
        parent : str, optional
            The parent group (group ID) to set as the parent of this group.
        shared : bool, optional
            Set group sharing. If enabled, people with the link to the group may
            access its contents regardless of the individual visibility settings
            of its children.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["api", "groups", group_id]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token

        # prepare payload
        payload = httpprep.OverloadDict()
        payload["player_identification", "team_identification", "parent",
                "shared"] = [p(player_identification),
                             p(team_identification), parent, shared]

        # rate limit if enabled
        if self._auto_rate_limit:
            self._rate_limiters[enums.Operation.patch_group]()

        # make request, print error, and return response
        response = requests.patch(prepped_url.build(), headers=
                                  prepped_headers.format_dict(),
                                  json=payload.remove_values(...).to_dict())
        if print_error:
            _print_error(response)
        return response
    
    def maps(self, *, print_error: bool = True) -> requests.Response:
        """Get a list of current maps.
        
        Parameters
        ----------
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.

        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["api", "maps"]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token

        # make request, print error, and return response
        response = requests.get(prepped_url.build(), headers=
                                prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
    
    @staticmethod
    def get_threejs(replay_id: str, *, cookie: str = ...,
                    print_error: bool = True) -> requests.Response:
        """Get basic locational, rotational, and timestamp data from a given
        replay on https://ballchasing.com.

        This is a static method and does not require a token (or construction of
        the outer class). It is not rate-limited.

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        cookie : str, optional
            Not required, but if provided, you are able to use this method on
            private replays so long as they belong to the cookie-holder's
            account on ballchasing.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.

        
        Warnings
        --------
        This functionality is highly experimental. It accesses a back-end API
        used for populating site data (that notably does not require
        authorization headers). At any time, this API could become restricted or
        its functionality could change.

        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["dyn", "replay", replay_id, "threejs"]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Cookie = cookie

        # make request, print error, and return response
        response = requests.get(prepped_url.build(), headers=
                                prepped_headers.format_dict(...))
        if print_error:
            _print_error(response)
        return response
    
    @staticmethod
    def get_timeline(replay_id: str, *, cookie: str = ...,
                    print_error: bool = True) -> requests.Response:
        """Get basic timeline data from a replay on https://ballchasing.com.

        This is a static method and does not require a token (or construction of
        the outer class). It is not rate-limited. 

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        cookie : str, optional
            Not required, but if provided, you are able to use this method on
            private replays so long as they belong to the cookie-holder's
            account on ballchasing.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        Warnings
        --------
        This functionality is highly experimental. It accesses a back-end API
        used for populating site data (that notably does not require
        authorization headers). At any time, this API could become restricted or
        its functionality could change.
        
        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["dyn", "replay", replay_id, "timeline"]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Cookie = cookie

        # make request, print error, and return response
        response = requests.get(prepped_url.build(), headers=
                                prepped_headers.format_dict(...))
        if print_error:
            _print_error(response)
        return response
    
    @staticmethod
    def export_csv(group_id: str, stat: typing.Union[str, enums.GroupStats], *,
                   cookie: str = ...,
                   print_error: bool = True) -> requests.Response:
        """Get group statistics from a group on https://ballchasing.com.

        This is a static method and does not require a token (or construction of
        the outer class). It is not rate-limited. 

        Parameters
        ----------
        group_id : str
            The ID of the group that is present in ballchasing's system.
        stat : str or GroupStats
            The stat section (players, teams, players games, teams games) to
            export.
        cookie : str, optional
            Not required, but if provided, you are able to use this method on
            private replays so long as they belong to the cookie-holder's
            account on ballchasing.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error)
            if the request resulted in an HTTP error (i.e. status codes 400
            through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.

        """
        # prepare url
        prepped_url = httpprep.URL(
            protocol="https",
            domain="ballchasing",
            top_level_domain="com",
            path_segments=["dl", "stats", f"group-{p(stat)}", group_id,
                           f"{group_id}-{p(stat)}.csv"]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Cookie = cookie

        # make request, print error, and return response
        response = requests.get(prepped_url.build(), headers=
                                prepped_headers.format_dict(...))
        if print_error:
            _print_error(response)
        return response
