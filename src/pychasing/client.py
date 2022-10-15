"""The core functionality code for the wrapper.

:copyright: (c) 2022-present Tanner B. Corcoran
:license: MIT, see LICENSE for more details.
"""

__author__ = "Tanner B. Corcoran"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2022-present Tanner B. Corcoran"


import requests, typing, time, datetime, typing, httpprep, prepr
from . import constants, types


def _rate_limit(previous_timestamp: float, wait_length: float) -> float:
    """Wait a certain amount of time given a previous timestamp and interval.
    
    """
    current_timestamp = datetime.datetime.now().timestamp()
    timestamp_diff    = current_timestamp - previous_timestamp
    if timestamp_diff >= wait_length:
        return current_timestamp
    time.sleep(wait_length - timestamp_diff)
    return datetime.datetime.now().timestamp()


def _print_error(response: requests.Response) -> None:
    error_side = "Client" if 400 <= response.status_code < 500 else "Server" if 500 <= response.status_code < 600 else None
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
            
        print(f"\033[93m{response.status_code} {error_side} Error: {reason} {error_description}for url: {response.url}\033[0m")


class Client:
    def __init__(
        self,
        token              : str,
        auto_rate_limit    : bool,
        patreon_tier       : types.PatreonTierType
    ) -> None:
        self._token              = token
        self._auto_rate_limit    = auto_rate_limit
        self._patreon_tier       = patreon_tier
        self._call_timestamps    = {
            constants.OPERATION.LIST_REPLAYS    : 0,
            constants.OPERATION.GET_REPLAY      : 0,
            constants.OPERATION.DELETE_REPLAY   : 0,
            constants.OPERATION.PATCH_REPLAY    : 0,
            constants.OPERATION.DOWNLOAD_REPLAY : 0,
            constants.OPERATION.CREATE_GROUP    : 0,
            constants.OPERATION.LIST_GROUPS     : 0,
            constants.OPERATION.GET_GROUP       : 0,
            constants.OPERATION.DELETE_GROUP    : 0,
            constants.OPERATION.PATCH_GROUP     : 0
        }
    

    def __repr__(self) -> prepr.types.prepr_str:
        return prepr.prepr(self).args(self._token, self._auto_rate_limit, self._patreon_tier).build()
    

    def ping(
        self,
        *,
        print_error: bool = True
    ) -> requests.Response:
        """Ping the https://ballchasing.com servers.

        Parameters
        ----------
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
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
        response = requests.get(prepped_url.build(), headers=prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response


    def upload_replay(
        self,
        file            : typing.BinaryIO,
        visibility      : str,
        *,
        group           : str  = ...,
        print_error     : bool = True
    ) -> requests.Response:
        """Upload a replay to https://ballchasing.com.

        Parameters
        ----------
        file : BinaryIO
            The `.replay` file to be uploaded.
        visibility : str
            The visibility of the replay once uploaded. Keywords for this variable can
            be accessed through the `pychasing.types.Visibility` class.
        group : str, optional
            The group to assign this replay to once it is uploaded.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
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
        prepped_url.components.queries["visibility", "group"] = [visibility, group]

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Authorization = self._token
        
        # make request, print error, and return response
        response = requests.post(prepped_url.build(query_check=...), headers=prepped_headers.format_dict(), files={"file":file})
        if print_error:
            _print_error(response)
        return response


    def list_replays(
        self,
        *,
        next               : str                         = ...,
        title              : str                         = ...,
        player_names       : list[str]                   = ...,
        player_ids         : list[tuple[str, int | str]] = ...,
        playlist           : str                         = ...,
        season             : str                         = ...,
        match_result       : str                         = ...,
        min_rank           : str                         = ...,
        max_rank           : str                         = ...,
        pro                : bool                        = ...,
        uploader           : typing.Literal["me"] | int  = ...,
        group              : str                         = ...,
        map                : str                         = ...,
        created_before     : str                         = ...,
        created_after      : str                         = ...,
        replay_date_before : str                         = ...,
        replay_date_after  : str                         = ...,
        count              : int                         = ...,
        sort_by            : str                         = ...,
        sort_dir           : str                         = ...,
        print_error        : bool                        = True
    ) -> requests.Response:
        """List replays filtered by various criteria.

        Parameters
        ----------
        next : str, optional
            A continuation URL (which can be acquired with
            `<response_from_list_replays>.json()["next"]`). If defined, all other
            arguments will be ignored.
        title : str, optional
            Only include replays with the given title.
        player_names : list of str, optional
            Only include replays that include the given player(s) by display name.
        player_ids : list of tuple of str and (int or str), optional
            Only include replays that include the given player(s) by platform [0] and
            player ID [1]. Keywords for platform can be accessed through the
            pychasing.types.Platform class.
        playlist : str, optional
            Only include replays in a given playlist. Keywords for this variable can be
            accessed through the pychasing.types.Playlist class.
        season : str, optional
            Only include replays played in a given season. The value for this be
            "1", ..., "14" for the pre free-to-play seasons, and "f1", "f2", ... for the
            post free-to-play seasons.
        match_result : str, optional
            Only include replays that resulted in the given result (win/loss). Keywords
            for this variable can be accessed through the pychasing.types.MatchResult
            class.
        min_rank : str, optional
            Only include replays where all players are above a given minimum rank.
            Keywords for this variable can be accessed through the pychasing.types.Rank
            class.
        max_rank : str, optional
            Only include replays where all players are above a given maximum rank.
            Keywords for this variable can be accessed through the pychasing.types.Rank
            class.
        pro : bool, optional
            Only include replays where at least one player in the lobby is a pro player.
        uploader : "me" or int, optional
            Only include replays uploaded by the given user. If the value is set to
            "me", then only replays uploaded by the token holder will be returned, or if
            a SteamID64 is used, only replays uploaded by the given steam user will be
            returned.
        group : str, optional
            Only include replays that are direct children of the given group.
        map : str, optional
            Only include replays played on a specific map. Keywords for this variable
            can be accessed through the pychasing.types.Map class.
        created_before : str, optional
            Only include replays created before a given date, formatted as an RFC3339
            datetime string.
        created_after : str, optional
            Only include replays created after a given date, formatted as an RFC3339
            datetime string.
        replay_date_before : str, optional
            Only include replays played before a given date, formatted as an RFC3339
            datetime string.
        replay_date_after : str, optional
            Only include replays played after a given date, formatted as an RFC3339
            datetime string.
        count : int, optional, default=150
            The number of replays returned. Must be between 1 and 200 if defined.
        sort_by : str, optional, default="upload-date"
            Whether to sort by replay date or upload date. Keywords for this variable
            can be accessed through the pychasing.types.SortBy class.
        sort_dir : str, optional, default="desc"
            Whether to sort descending or ascending. Keywords for this variable can be
            accessed through the pychasing.types.SortDir class.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        Raises:
            ValueError: `count` is defined and is less than 0 or greater than 200.
        
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
                "title",
                "playlist",
                "season",
                "match-result",
                "min-rank",
                "max-rank",
                "pro",
                "uploader",
                "group",
                "map",
                "created-before",
                "created-after",
                "replay-date-before",
                "replay-date-after",
                "count",
                "sort-by",
                "sort-dir"
            ] = [
                title,
                playlist,
                season,
                match_result,
                min_rank,
                max_rank,
                "true" if pro is True else "false" if pro is False else ...,
                uploader,
                group,
                map,
                created_before,
                created_after,
                replay_date_before,
                replay_date_after,
                count,
                sort_by,
                sort_dir
            ]
            if player_names != ...:
                for name in player_names:
                    prepped_url.components.queries["player-name"] = name
            if player_ids != ...:
                for platform, id in player_ids:
                    prepped_url.components.queries["player-id"] = f"{platform}:{id}"
            url = prepped_url.build(query_check=...)
        # rate limit if enabled
        if self._auto_rate_limit:
            self._call_timestamps[constants.OPERATION.LIST_REPLAYS] = _rate_limit(self._call_timestamps[constants.OPERATION.LIST_REPLAYS], self._patreon_tier.LIST_REPLAYS)

        # make request, print error, and return response
        response = requests.get(url, headers=prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
    

    def get_replay(
        self,
        replay_id   : str,
        *,
        print_error : bool = True
    ) -> requests.Response:
        """Get more in-depth information for a specific replay.

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
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
            self._call_timestamps[constants.OPERATION.GET_REPLAY] = _rate_limit(self._call_timestamps[constants.OPERATION.GET_REPLAY], self._patreon_tier.GET_REPLAY)

        # make request, print error, and return response
        response = requests.get(prepped_url.build(), headers=prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
        

    def delete_replay(
        self,
        replay_id   : str,
        *,
        print_error : bool = True
    ) -> requests.Response:
        """Delete the given replay from https://ballchasing.com, so long as the replay is
        owned by the token holder.

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
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
            self._call_timestamps[constants.OPERATION.DELETE_REPLAY] = _rate_limit(self._call_timestamps[constants.OPERATION.DELETE_REPLAY], self._patreon_tier.DELETE_REPLAY)

        # make request, print error, and return response
        response = requests.delete(prepped_url.build(), headers=prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
        

    def patch_replay(
        self, 
        replay_id   : str,
        *,
        title       : str  = ...,
        visibility  : str  = ...,
        group       : str  = ...,
        print_error : bool = True
    ) -> requests.Response:
        """Patch the title, visibility, and/or group of a replay on
        https://ballchasing.com, so long as the replay is owned by the token holder.

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        title : str, optional
            Set the title of the replay.
        visibility : str, optional
            Set the visibility of the replay. Keywords for this variable can be accessed
            through the `pychasing.types.Visibility` class.
        group : str, optional
            Set the group of the replay. An empty string (`""`) will set the group to
            none.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
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
        payload["title", "visibility", "group"] = [title, visibility, group]

        # rate limit if enabled
        if self._auto_rate_limit:
            self._call_timestamps[constants.OPERATION.PATCH_REPLAY] = _rate_limit(self._call_timestamps[constants.OPERATION.PATCH_REPLAY], self._patreon_tier.PATCH_REPLAY)

        # make request, print error, and return response
        response = requests.patch(prepped_url.build(), headers=prepped_headers.format_dict(), json=payload.remove_values(...).to_dict())
        if print_error:
            _print_error(response)
        return response


    def download_replay(
        self,
        replay_id   : str,
        *,
        print_error : bool = True
    ) -> requests.Response:
        """Download a replay from https://ballchasing.com.

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        save_path : str, optional
            If defined, the replay content will be saved into the specified file (must
            be a `.replay` file).
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
        Warnings
        --------
        Replay files can be rather large (up to around 1.5mb). The HTTP request is set
        to `stream`, thus you should use `iter_content` when saving the replay to a
        file.

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
            self._call_timestamps[constants.OPERATION.DOWNLOAD_REPLAY] = _rate_limit(self._call_timestamps[constants.OPERATION.DOWNLOAD_REPLAY], self._patreon_tier.DOWNLOAD_REPLAY)

        # make request, print error, and return response
        response = requests.get(prepped_url.build(), headers=prepped_headers.format_dict(), stream=True)
        if print_error:
            _print_error(response)
        return response


    def create_group(
        self,
        name                  : str,
        player_identification : str,
        team_identification   : str,
        *,
        parent                : str  = ...,
        print_error           : bool = True
    ) -> requests.Response:
        """Create a replay group on https://ballchasing.com.

        Parameters
        ----------
        name : str
            The name of the group.
        player_identification : str
            Determines how to identify the same player across multiple replays - by
            account name, or account ID. Keywords for this variable can be accessed
            through the `pychasing.types.PlayerIdentification` class.
        team_identification : str
            Determines how to identify the same team across multiple replays - by
            distinct players (if teams have fixed rosters for every single games), or by
            player clusters (if subs are allowed between games). Keywords for this
            variable can be accessed through the `pychasing.types.TeamIdentification`
            class.
        parent : str, optional
            The parent group (group ID) to set as the parent of this group.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).

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
        payload["name", "player_identification", "team_identification", "parent"] = [name, player_identification, team_identification, parent]

        # rate limit if enabled
        if self._auto_rate_limit:
            self._call_timestamps[constants.OPERATION.CREATE_GROUP] = _rate_limit(self._call_timestamps[constants.OPERATION.CREATE_GROUP], self._patreon_tier.CREATE_GROUP)

        # make request, print error, and return response
        response = requests.post(prepped_url.build(), headers=prepped_headers.format_dict(), json=payload.remove_values(...).to_dict())
        if print_error:
            _print_error(response)
        return response
        

    def list_groups(
        self,
        *,
        next            : str        = ...,
        name            : str        = ...,
        creator         : str | int  = ...,
        group           : str        = ...,
        created_before  : str        = ...,
        created_after   : str        = ...,
        count           : int        = ...,
        sort_by         : str        = ...,
        sort_dir        : str        = ...,
        print_error     : bool       = True
    ) -> requests.Response:
        """List replay groups from https://ballchasing.com filtered by various criteria.

        Parameters
        ----------
        next : str, optional
            A continuation URL (which can be acquired with
            `<response_from_list_replays>.json()["next"]`). If defined, all other
            arguments will be ignored.
        name : str, optional
            Only include groups whose title contains the given text.
        creator : str or int, optional
            Only include replays uploaded by the given user (defined by a `SteamID64`).
        group : str, optional
            Only include replays that are direct or indirect children of the given group
            (defined by a group ID).
        created_before : str, optional
            Only include groups created before a given date, formatted as an RFC3339
            datetime string.
        created_after : str, optional
            Only include groups created after a given date, formatted as an RFC3339
            datetime string.
        replay_date_before : str, optional
            Only include replays played before a given date, formatted as an RFC3339
            datetime string.
        replay_date_after : str, optional
            Only include replays played after a given date, formatted as an RFC3339
            datetime string.
        count : int, optional, default=150
            The number of groups returned. Must be between 1 and 200 if defined.
        sort_by : str, optional, default="created"
            Whether to sort by creation date or name. Keywords for this variable can be
            accessed through the pychasing.types.SortBy class.
        sort_dir : str, optional, default="desc"
            Whether to sort descending or ascending. Keywords for this variable can be
            accessed through the pychasing.types.SortDir class.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).

        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        Raises:
            ValueError: `count` is defined and is less than 0 or greater than 200.
        
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
            prepped_url.components.queries[
                "name",
                "creator",
                "group",
                "created-before",
                "created-after",
                "count",
                "sort-by",
                "sort-dir"
            ] = [
                name,
                creator,
                group,
                created_before,
                created_after,
                count,
                sort_by,
                sort_dir
            ]
            url = prepped_url.build(query_check=...)

        # rate limit if enabled
        if self._auto_rate_limit:
            self._call_timestamps[constants.OPERATION.LIST_GROUPS] = _rate_limit(self._call_timestamps[constants.OPERATION.LIST_GROUPS], self._patreon_tier.LIST_GROUPS)

        # make request, print error, and return response
        response = requests.get(url, headers=prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response


    def get_group(
        self,
        group_id    : str,
        *,
        print_error : bool = True
    ) -> requests.Response:
        """Get information on a specific replay group from https://ballchasing.com.

        Parameters
        ----------
        group_id : str
            The ID of the group present in ballchasing's systems.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
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
            self._call_timestamps[constants.OPERATION.GET_GROUP] = _rate_limit(self._call_timestamps[constants.OPERATION.GET_GROUP], self._patreon_tier.GET_GROUP)

        # make request, print error, and return response
        response = requests.get(prepped_url.build(), headers=prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
    

    def delete_group(
        self,
        group_id     : str,
        *,
        print_error : bool = True
    ) -> requests.Response:
        """Delete a specific group (and all children groups) from https://ballchasing.com,
        so long as it is owned by the token holder.

        Parameters
        ----------
        group_id : str
            The ID of the group present in ballchasing's systems.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
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
            self._call_timestamps[constants.OPERATION.DELETE_GROUP] = _rate_limit(self._call_timestamps[constants.OPERATION.DELETE_GROUP], self._patreon_tier.DELETE_GROUP)

        # make request, print error, and return response
        response = requests.delete(prepped_url.build(), headers=prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
    

    def patch_group(
        self,
        group_id              : str,
        *,
        player_identification : str  = ...,
        team_identification   : str  = ...,
        parent                : str  = ...,
        shared                : bool = ...,
        print_error           : bool = True
    ) -> requests.Response:
        """Delete a specific group (and all children groups) from https://ballchasing.com,
        so long as it is owned by the token holder.

        Parameters
        ----------
        group_id : str
            The ID of the group present in ballchasing's systems.
        player_identification : str, optional
            Determines how to identify the same player across multiple replays - by
            account name, or account ID. Keywords for this variable can be accessed
            through the `pychasing.types.PlayerIdentification` class.
        team_identification : str, optional
            Determines how to identify the same team across multiple replays - by
            distinct players (if teams have fixed rosters for every single games), or by
            player clusters (if subs are allowed between games). Keywords for this
            variable can be accessed through the `pychasing.types.TeamIdentification`
            class.
        parent : str, optional
            The parent group (group ID) to set as the parent of this group.
        shared : bool, optional
            Set group sharing. If enabled, people with the link to the group may access
            its contents regardless of the individual visibility settings of its
            children.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
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
        payload["player_identification", "team_identification", "parent", "shared"] = [player_identification, team_identification, parent, shared]

        # rate limit if enabled
        if self._auto_rate_limit:
            self._call_timestamps[constants.OPERATION.PATCH_GROUP] = _rate_limit(self._call_timestamps[constants.OPERATION.PATCH_GROUP], self._patreon_tier.PATCH_GROUP)

        # make request, print error, and return response
        response = requests.patch(prepped_url.build(), headers=prepped_headers.format_dict(), json=payload.remove_values(...).to_dict())
        if print_error:
            _print_error(response)
        return response
    

    def maps(
        self,
        *,
        print_error: bool = True
    ) -> requests.Response:
        """Get a list of current maps.
        
        Parameters
        ----------
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
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
        response = requests.get(prepped_url.build(), headers=prepped_headers.format_dict())
        if print_error:
            _print_error(response)
        return response
    
    
    @staticmethod
    def get_threejs(
        replay_id   : str,
        *,
        cookie      : str = ...,
        print_error : bool = True
    ) -> requests.Response:
        """Get basic locational, rotational, and timestamp data from a given replay on
        https://ballchasing.com.

        This is a static method and does not require a token (or construction of the
        outer class). It is not rate-limited.

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        cookie : str, optional
            Not required, but if provided, you are able to use this method on private
            replays so long as they belong to the cookie-holder's account on
            ballchasing.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.

        
        Warnings
        --------
        This functionality is highly experimental. It accesses a back-end API used for
        populating site data (that notably does not require authorization headers). At
        any time, this API could become restricted or its functionality could change.

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
        response = requests.get(prepped_url.build(), headers=prepped_headers.format_dict(...))
        if print_error:
            _print_error(response)
        return response
    

    @staticmethod
    def get_timeline(
        replay_id   : str,
        *,
        cookie      : str = ...,
        print_error : bool = True
    ) -> requests.Response:
        """Get basic timeline data from a replay on https://ballchasing.com.

        This is a static method and does not require a token (or construction of the
        outer class). It is not rate-limited. 

        Parameters
        ----------
        replay_id : str
            The ID of the replay that is present in ballchasing's system.
        cookie : str, optional
            Not required, but if provided, you are able to use this method on private
            replays so long as they belong to the cookie-holder's account on
            ballchasing.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
        Returns
        -------
        requests.Response
            The `requests.Response` object returned from the HTTP request.
        
        Warnings
        --------
        This functionality is highly experimental. It accesses a back-end API used for
        populating site data (that notably does not require authorization headers). At
        any time, this API could become restricted or its functionality could change.
        
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
        response = requests.get(prepped_url.build(), headers=prepped_headers.format_dict(...))
        if print_error:
            _print_error(response)
        return response
    

    @staticmethod
    def export_csv(
        group_id    : str,
        stat        : str,
        *,
        cookie      : str = ...,
        print_error : bool = True
    ) -> requests.Response:
        """Get group statistics from a group on https://ballchasing.com.

        This is a static method and does not require a token (or construction of the
        outer class). It is not rate-limited. 

        Parameters
        ----------
        group_id : str
            The ID of the group that is present in ballchasing's system.
        stat : str
            The stat section (players, teams, players games, teams games) to export.
            Keywords for this variable can be accessed through the
            pychasing.types.GroupStats class.
        cookie : str, optional
            Not required, but if provided, you are able to use this method on private
            replays so long as they belong to the cookie-holder's account on
            ballchasing.
        print_error : bool, optional, default=True
            Prints an error message (that contains information about the error) if the
            request resulted in an HTTP error (i.e. status codes 400 through 599).
        
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
            path_segments=["dl", "stats", f"group-{stat}", group_id, f"{group_id}-{stat}.csv"]
        )

        # prepare headers
        prepped_headers = httpprep.Headers()
        prepped_headers.Cookie = cookie

        # make request, print error, and return response
        response = requests.get(prepped_url.build(), headers=prepped_headers.format_dict(...))
        if print_error:
            _print_error(response)
        return response
