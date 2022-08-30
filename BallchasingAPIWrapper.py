from dpyt.interfaces                 import _ext
from dpyt.interfaces.implementations import _exceptions, _types
from typing                          import Literal, BinaryIO, Union, Optional

import requests, json, time


class Ballchasing:


    def __init__(
        self,
        token           : str,
        auto_rate_limit : bool,
        patreon_tier    : _types.BallchasingPatreonTier
    ):
        """
        A wrapper for the https://www.ballchasing.com API.

        Arguments
        ---------
        `token` -> `str`
            
            The user's Ballchasing token.
        
        `auto_rate_limit` -> `bool`

            If True, each function will automatically pause and re-run when the rate limit is exceeded. If False, the RateLimitExceeded exception will be raised instead.
        
        `patreon_tier` -> `BallchasingPatreonTier`

            The user's Ballchasing Patreon tier (`Regular` if none).
        """
        _ext.EnforceVars(Ballchasing.__init__).enforce(
            token, "token", type_ = str
        ).enforce(
            auto_rate_limit, "auto_rate_limit", type_ = bool
        )
        self.repr            = _ext.make_repr(Ballchasing, (token,))
        self.auth            = {"Authorization":token}
        self.auth_json       = {"Authorization":token,"Content-Type":"application/json"}
        self.auto_rate_limit = auto_rate_limit
        self.patreon_tier    = patreon_tier


    def __repr__(self) -> str:
        return self.repr


    def ping(
        self,
        *,
        return_response : bool = ...
    ) -> Union[dict, requests.Response]:
        """
        Used to check if the API key is correct or if the Ballchasing API is reachable.

        Arguments
        ---------
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.

        Returns
        -------
        `Union[dict, requests.Response]`

        Raises
        ------
        `MissingAPIKey`
        
        
            If the API key is missing or invalid.
        
        
        `APIUnaccessible`
        
        
            If the API is down.
        """
        _ext.EnforceVars(Ballchasing.ping).enforce(
            return_response, "return_response", type_ = bool, filter_ = "x != ..."
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        URL="https://ballchasing.com/api/"
        RESPONSE=requests.get(URL, headers=self.auth)
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 200: return RESPONSE.json()
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)


    def upload_replay(
        self,
        file            : BinaryIO,
        visibility      : _types.Ballchasing.Visibility,
        *,
        group           : str  = ...,
        return_response : bool = ...
    ) -> Union[dict, requests.Response]:
        """
        Uploads a `.replay` file to the key-holder's Ballchasing account.
        
        Arguments
        ---------
        `file` -> `BinaryIO`
        
            The `.replay` file to upload, as a bytestream.
        
        `visibility` -> `Literal["public", "unlisted", "private"]`
        
            The visibility of the replay once uploaded.
        
        `group` -> `str`
        
            The group to assign the replay to upon upload.
        
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.

        Returns
        -------
        `Union[dict, requests.Response]`

        Raises
        ------
        `InvalidInput`
        
            If the replay file is invalid, or the inputs are incorrect.
        
        `DuplicateReplay`
    
            If the replay file has already been uploaded to the account.
        
        `APIUnaccessible`
        
            If the API is down.
        
        `MissingAPIKey`
        
            If the API key is missing or invalid.
        """
        _ext.EnforceVars(Ballchasing.upload_replay).enforce(
            group, "group", type_ = str, filter_ = "x != ..."
        ).enforce(
            return_response, "return_response", type_ = bool, filter_ = "x != ..."
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        arguments = _ext.format_url_query_parameters([
            (visibility, "visibility"),
            (group, "group")
        ])
        URL=f"https://ballchasing.com/api/v2/upload?{arguments}"
        RESPONSE=requests.post(URL, headers=self.auth, files={"file":file})
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 201: return RESPONSE.json()
            case 400: raise _exceptions.Ballchasing.InvalidInput()
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 409: raise _exceptions.Ballchasing.DuplicateReplay()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)


    def list_replays(
        self, 
        *,
        title              : str                                                       = ...,
        player_names       : list[str]                                                 = ...,
        player_ids         : list[tuple[_types.Ballchasing.Platform, Union[int, str]]] = ...,
        playlist           : _types.Ballchasing.Playlist                               = ...,
        season             : str                                                       = ...,
        match_result       : Literal["win", "loss"]                                    = ...,
        min_rank           : _types.Ballchasing.Rank                                   = ...,
        max_rank           : _types.Ballchasing.Rank                                   = ...,
        pro                : bool                                                      = ...,
        uploader           : Union[Literal["me"], int]                                 = ...,
        group              : str                                                       = ...,
        map                : _types.Ballchasing.Map                                    = ...,
        created_before     : str                                                       = ...,
        created_after      : str                                                       = ...,
        replay_date_before : str                                                       = ...,
        replay_date_after  : str                                                       = ...,
        count              : int                                                       = ...,
        sort_by            : Literal["replay-date", "upload-date"]                     = ...,
        sort_dir           : Literal["asc", "desc"]                                    = ...,
        return_response    : bool                                                      = ...
    ) -> Union[dict, requests.Response]:
        """
        Gets a list of simplified replay data given a set of defined parameters.

        Arguments
        ---------
        `title` -> `str`
        
            Filter by title of replay.
        
        `player_name` -> `list[str]`
        
            Filter by player name(s).
        
        `player_id` -> `list[tuple[Platform, Union[int, str]]]`
        
            Filter by a list of of player IDs, each defined as a tuple containing the player's platform and corresponding identifier.
        
        `playlist` -> `Playlist`
        
            Filter by playlist.
        
        `season` -> `str`
        
            Filter by season. `1` through `14` for pre-free-to-play, and `f1`, `f2`, etc. for post-free-to-play.
        
        `match_result` -> `Literal["win", "loss"]`
        
            Filter by match result.
        
        `min_rank` -> `Rank`
        
            Filter by minimum rank.
        
        `max_rank` -> `Rank`
        
            Filter by maximum rank.
        
        `pro` -> `bool`
        
            Filter by professional status.
        
        `uploader` -> `Union[Literal["me"], int]`
        
            Filter by uploader (`me` or `SteamID64`).
        
        `group` -> `str`
        
            Filter by group (only acquire replay in direct group; child groups are ignored).
        
        `map` -> `Map`
        
            Filter by map.
        
        `created_before` -> `str`
        
            Filter by replay upload date.
        
        `created_after` -> `str`
        
            Filter by replay upload date.
        
        `replay_date_before` -> `str`
        
            Filter by replay creation date.
        
        `replay_date_after` -> `str`
        
            Filter by replay creation date.
        
        `count` -> `int`
        
            The amount of replays to acquire. Must be between `1` and `200`.
        
        `sort_by` -> `Literal["replay-date", "upload-date"]`
        
            Whether or not to sort by the replay creation date or the replay upload date.
        
        `sort_dir` -> `Literal["asc", "desc"]`
        
            The direction of the sort.
        
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.

        Returns
        -------
        `Union[dict, requests.Response]`

        Raises
        ------
        `ValueError`
            If neither `player_name` nor `player_id` is defined.
        `ValueError`
            If `count` is defined and is not between `0` and `200`.
        `MissingAPIKey`
            If the API key is missing or invalid.
        `APIUnaccessible`
            If the API is down.
        """
        _ext.EnforceVars(Ballchasing.list_replays).enforce(
            [title, playlist, match_result, min_rank, max_rank, group, map, created_before, created_after, replay_date_before, replay_date_after, sort_by, sort_dir], ["title", "playlist", "match_result", "min_rank", "max_rank", "group", "map", "created_before", "created_after", "replay_date_before", "replay_date_after", "sort_by", "sort_dir"], type_ = str, filter_ = "x != ..."
        ).enforce(
            player_names, "player_names", operations = ["isinstance(x, list)", "all(isinstance(pname, str) for pname in x)"], filter_ = "x != ..."
        ).enforce(
            player_ids, "player_ids", operations = ["isinstance(x, list)", "all(isinstance(ptuple, (list, tuple)) and len(ptuple) == 2 for ptuple in x)", "all(isinstance(ptuple[0], str) and isinstance(ptuple[1], (int, str)) for ptuple in x)"], filter_ = "x != ..."
        ).enforce(
            count, "count", operations = ["isinstance(x, int)", "0 < x < 200"], filter_ = "x != ..."
        ).enforce(
            [return_response, pro], ["return_response", "pro"], type_ = bool, filter_ = "x != ..."
        )
        [player_names, player_ids, return_response] = _ext.set_defaults(
            [player_names, player_ids, return_response],
            [[], [], False]
        )
        if player_names == ... and player_ids == ...:
            raise ValueError("At least one of \"player_name\" or \"player_id\" must be defined.")
        arguments = _ext.format_url_query_parameters([
            (title, "title"),
            *[(player_name, "player_name") for player_name in player_names],
            *[(f"{platform}:{id}", "player_name") for platform, id in player_ids],
            (playlist, "playlist"),
            (season, "season"),
            (match_result, "match-result"),
            (min_rank, "min-rank"),
            (max_rank, "max-rank"),
            (pro, "pro", True),
            ("uploader", uploader),
            (group, "group"),
            (map, "map"),
            (created_before, "created-before"),
            (created_after, "created-after"),
            (replay_date_before, "replay-date-before"),
            (replay_date_after, "replay-date-after"),
            (count, "count"),
            (sort_by, "sort-by"),
            (sort_dir, "sort-dir")
        ])
        URL=f"https://ballchasing.com/api/replays?{arguments}"
        RESPONSE=requests.get(URL, headers=self.auth)
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 200: return RESPONSE.json()
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case 429:
                if self.auto_rate_limit is True:
                    time.sleep(self.patreon_tier.list_replays)
                    return self.list_replays(
                        title              = title,
                        player_names       = player_names,
                        player_ids         = player_ids,
                        playlist           = playlist,
                        season             = season,
                        match_result       = match_result,
                        min_rank           = min_rank,
                        max_rank           = max_rank,
                        pro                = pro,
                        uploader           = uploader,
                        group              = group,
                        map                = map,
                        created_before     = created_before,
                        created_after      = created_after,
                        replay_date_before = replay_date_before,
                        replay_date_after  = replay_date_after,
                        count              = count,
                        sort_by            = sort_by,
                        sort_dir           = sort_dir,
                        return_response    = return_response
                    )
                else:
                    raise _exceptions.Ballchasing.RateLimitExceeded()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)


    def get_replay(
        self,
        replay_id       : str,
        *,
        return_response : bool = ...
    ) -> Union[dict, requests.Response]:
        """
        Gets detailed information on a single replay uploaded to Ballchasing.

        Arguments
        ---------
        `replay_id` -> `str`
        
            The ID of the replay.
        
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.

        Returns
        -------
        `Union[dict, requests.Response]`

        Raises
        ------
        `PendingReplay`
        
            If the replay being accessed is still processing.
        
        `FailedReplay`
        
            If the replay being accessed is failed to process.
        
        `MissingAPIKey`
        
            If the API key is missing or invalid.
        
        `APIUnaccessible`
        
            If the API is down.
        """
        _ext.EnforceVars(Ballchasing.get_replay).enforce(
            return_response, "return_response", type_ = bool, filter_ = "x != ..."
        ).enforce(
            replay_id, "replay_id", type_ = str
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        URL="https://ballchasing.com/api/replays/" + replay_id
        RESPONSE=requests.get(URL, headers=self.auth)
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 200:
                RESPONSE=RESPONSE.json()
                status = RESPONSE["status"]
                if status == "ok":
                    return RESPONSE
                elif status == "pending":
                    raise _exceptions.Ballchasing.PendingReplay()
                elif status == "failed":
                    raise _exceptions.Ballchasing.FailedReplay
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case 429:
                if self.auto_rate_limit is True:
                    time.sleep(self.patreon_tier.get_replay)
                    return self.get_replay(
                        replay_id,
                        return_response = return_response
                    )
                else:
                    raise _exceptions.Ballchasing.RateLimitExceeded()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)


    def delete_replay(
        self,
        replay_id       : str,
        *,
        return_response : bool = ...
    ) -> Optional[requests.Response]:
        """
        Deletes the replay with the corresponding `replay ID` that has been uploaded to Ballchasing by the key-holder.

        Arguments
        ---------
        `replay_id` -> `str`
        
            The ID of the replay.
        
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.

        Returns
        -------
        `Optional[requests.Response]`

        Raises
        ------
        `MissingAPIKey`
        
            If the API key is missing or invalid.
        
        `APIUnaccessible`
        
            If the API is down.
        """
        _ext.EnforceVars(Ballchasing.delete_replay).enforce(
            return_response, "return_response", type_ = bool, filter_ = "x != ..."
        ).enforce(
            replay_id, "replay_id", type_ = str
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        URL="https://ballchasing.com/api/replays/" + replay_id
        RESPONSE=requests.delete(URL, headers=self.auth)
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 204: return
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case 429:
                if self.auto_rate_limit is True:
                    time.sleep(self.patreon_tier.delete_replay)
                    return self.delete_replay(
                        replay_id,
                        return_response = return_response
                    )
                else:
                    raise _exceptions.Ballchasing.RateLimitExceeded()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)
    
    
    def patch_replay(
        self, 
        replay_id       : str,
        *,
        title           : str                           = ...,
        visibility      : _types.Ballchasing.Visibility = ...,
        group           : str                           = ...,
        return_response : bool                          = ...
    ) -> Optional[requests.Response]:
        """
        Used to patch one (or more) of the replay's patchable values.

        Arguments
        ---------
        `replay_id` -> `str`
        
            The id of the replay to patch.
        
        `title` -> `str`
        
            The title of the replay.
        
        `visibility` -> `Visibility`
        
            The visibility of the replay.
        
        `group` -> `str`
        
            The group that the replay resides in. Should be an empty string (`""`) to unassign from replay group.
        
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.

        Returns
        -------
        `Optional[requests.Response]`

        Raises
        ------
        `ValueError`
        
            If none of the optional variables are defined.
        
        `MissingAPIKey`
        
            If the API key is missing or invalid.
        
        `APIUnaccessible`
        
            If the API is down.
        """
        _ext.EnforceVars(Ballchasing.patch_replay).enforce(
            return_response, "return_response", type_ = bool, filter_ = "x != ..."
        ).enforce(
            [title, visibility, group, replay_id], ["title", "visibility", "group", "replay_id"], type_ = str, filter_ = "x != ..."
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        data=_ext.kwargs_(
            ["title", "visibility", "group"],
            [title, visibility, group]
        )
        if len(data) == 0:
            raise ValueError("At least one of \"title\", \"visibility\" or \"group\" must be defined.")
        URL="https://ballchasing.com/api/replays/" + replay_id
        RESPONSE=requests.patch(URL, headers=self.auth_json, data=json.dumps(data, separators=[",",":"]))
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 204: return
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case 429:
                if self.auto_rate_limit is True:
                    time.sleep(self.patreon_tier.patch_replay)
                    return self.patch_replay(
                        replay_id,
                        title           = title,
                        visibility      = visibility,
                        group           = group,
                        return_response = return_response
                    )
                else:
                    raise _exceptions.Ballchasing.RateLimitExceeded()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)


    def download_replay(
        self,
        replay_id       : str,
        *,
        return_response : bool = ...
    ) -> Union[bytes, requests.Response]:
        """
        Downloads a replay.

        Arguments
        ---------
        `replay_id` -> `str`
        
            The ID of the replay.
        
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.

        Returns
        -------
        `Union[BinaryIO, requests.Response]`

        Raises
        ------
        `PendingReplay`
        
            If the replay being accessed is still processing.
        
        `FailedReplay`
        
            If the replay being accessed is failed to process.
        
        `MissingAPIKey`
        
            If the API key is missing or invalid.
        
        `APIUnaccessible`
        
            If the API is down.
        """
        _ext.EnforceVars(Ballchasing.download_replay).enforce(
            return_response, "return_response", type_ = bool, filter_ = "x != ..."
        ).enforce(
            replay_id, "replay_id", type_ = str
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        URL="https://ballchasing.com/api/replays/" + replay_id + "/file"
        RESPONSE=requests.get(URL, headers=self.auth)
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 200: return RESPONSE.content
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case 429:
                if self.auto_rate_limit is True:
                    time.sleep(self.patreon_tier.download_replay)
                    return self.download_replay(
                        replay_id,
                        return_response = return_response
                    )
                else:
                    raise _exceptions.Ballchasing.RateLimitExceeded()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)


    def create_group(
        self,
        name                  : str,
        player_identification : Literal["by-id", "by-name"],
        team_identification   : Literal["by-distinct-players", "by-player-clusters"],
        *,
        parent                : str  = ...,
        return_response       : bool = ...
    ) -> Union[dict, requests.Response]:
        """
        Creates a group with specified parameters.

        Arguments
        ---------
        `name` -> `str`
        
            The name of the created group.
        
        `player_identification` -> `Literal["by-id", "by-name"]`
        
            How players are identified across the replays in the group.
        
        `team_identification` -> `Literal["by-distinct-players", "by-player-clusters"]`
        
            How teams are to be identified between replays. `by-distinct-players` means they will be grouped by fixed roster, whereas `by-player-clusters` means they will be grouped less strictly.
        
        `parent` -> `str`
        
            The parent group to assign this group to.
        
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.

        Returns
        -------
        `Union[dict, requests.Response]`

        Raises
        ------
        `MissingAPIKey`
        
            If the API key is missing or invalid.
        
        `APIUnaccessible`
        
            If the API is down.
        
        `DuplicateName`

            If the there is another group with the same name in the same directory.
        """
        _ext.EnforceVars(Ballchasing.create_group).enforce(
            return_response, "return_response", type_ = bool, filter_ = "x != ..."
        ).enforce(
            [name, player_identification, team_identification], ["name", "player_identification", "team_identification"], type_ = str
        ).enforce(
            parent, "parent", type_ = str, filter_ = "x != ..."
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        data={"name":name,"player_identification":player_identification,"team_identification":team_identification}
        if parent != ...:
            data["parent"]=parent
        URL="https://ballchasing.com/api/groups"
        RESPONSE=requests.post(URL, headers=self.auth_json, data=json.dumps(data, separators=[",",":"]))
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 201: return RESPONSE.json()
            case 400: raise _exceptions.Ballchasing.DuplicateName()
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case 429:
                if self.auto_rate_limit is True:
                    time.sleep(self.patreon_tier.create_group)
                    return self.create_group(
                        name,
                        player_identification,
                        team_identification,
                        parent          = parent,
                        return_response = return_response
                    )
                else:
                    raise _exceptions.Ballchasing.RateLimitExceeded()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)
    
    
    def list_groups(
        self,
        *,
        name            : str                        = ...,
        creator         : Union[Literal["me"], int]  = ...,
        group           : str                        = ...,
        created_before  : str                        = ...,
        created_after   : str                        = ...,
        count           : int                        = ...,
        sort_by         : Literal["created", "name"] = ...,
        sort_dir        : Literal["asc", "desc"]     = ...,
        return_response : bool                       = ...
    ) -> Union[dict, requests.Response]:
        """
        Used to acquire a list of groups given certain criteria.

        Arguments
        ---------
        `name` -> `str`
        
            Filter by group name.
        
        `creator` -> `Union[Literal["me"], int]`
        
            Filter by creator (`"me"` or `SteamID64`).
        
        `group` -> `str`
        
            Only include children of the specified group ID.
        
        `created_before` -> `str`
        
            Only include groups created before a given date in `RFC3339` format.
        
        `created_after` -> `str`
        
            Only include groups created after a given date in `RFC3339` format.
        
        `count` -> `int`
        
            The number of groups to acquire. Must not be less than 1 or greater than 200.
        
        `sort_by` -> `Literal["created", "name"]`
        
            Whether or not to sort by creation date or name.
        
        `sort_dir` -> `Literal["asc", "desc"]`
        
            Direction of sort.
        
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.
        
        Returns
        -------
        `Union[dict, requests.Response]`

        Raises
        ------
        `ValueError`
        
            If `count` is defined and is not between `0` and `200`.
        
        `ValueError`
        
            If none of the arguments are defined.
        
        `MissingAPIKey`
        
            If the API key is missing or invalid.
        
        `APIUnaccessible`
        
            If the API is down.
        """
        _ext.EnforceVars(Ballchasing.list_groups).enforce(
            return_response, "return_response", type_ = bool, filter_ = "x != ..."
        ).enforce(
            [name, creator, group, created_before, created_after, sort_by, sort_dir], ["name", "creator", "group", "created_before", "created_after", "sort_by", "sort_dir"], type_ = str, filter_ = "x != ..."
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        arguments = _ext.format_url_query_parameters([
            (name, "name"),
            (creator, "creator"),
            (group, "group"),
            (created_before, "created-before"),
            (created_after, "created-after"),
            (count, "count"),
            (sort_by, "sort-by"),
            (sort_dir, "sort-dir")
        ])
        if len(arguments) == 0:
            raise ValueError("At least one of \"name\", \"creator\", \"group\", \"created_before\", \"created_after\", \"count\", \"sort_by\", or \"sort_dir\" must be defined.")
        URL=f"https://ballchasing.com/api/groups?{arguments}"
        RESPONSE=requests.get(URL, headers=self.auth)
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 200: return RESPONSE.json()
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case 429:
                if self.auto_rate_limit is True:
                    time.sleep(self.patreon_tier.list_groups)
                    return self.list_groups(
                        name            = name,
                        creator         = creator,
                        group           = group,
                        created_before  = created_before,
                        created_after   = created_after,
                        count           = count,
                        sort_by         = sort_by,
                        sort_dir        = sort_dir,
                        return_response = return_response
                    )
                else:
                    raise _exceptions.Ballchasing.RateLimitExceeded()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)


    def get_group(
        self,
        group_id        : str,
        *,
        return_response : bool = ...
    ) -> Union[dict, requests.Response]:
        """
        Gets detailed information from a group.

        Arguments
        ---------
        `group_id` -> `str`
        
            The id of the group.
        
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.
        
        Returns
        -------
        `Union[dict, requests.Response]`

        Raises
        ------
        `PendingReplay`
        
            If one or more of the replays in the group are still pending.
        
        `FailedReplay`
        
            If one or more of the replays in the group are failed replays.
        
        `MissingAPIKey`
        
            If the API key is missing or invalid.
        
        `APIUnaccessible`
        
            If the API is down.
        """
        _ext.EnforceVars(Ballchasing.get_group).enforce(
            return_response, "return_response", type_ = bool, filter_ = "x != ..."
        ).enforce(
            group_id, "group_id", type_ = str
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        URL="https://ballchasing.com/api/groups/" + group_id
        RESPONSE=requests.get(URL, headers=self.auth)
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 200:
                RESPONSE=RESPONSE.json()
                status = RESPONSE["status"]
                if status == "ok":
                    return RESPONSE
                elif status == "pending_replays":
                    raise _exceptions.Ballchasing.PendingReplay()
                elif status == "failed_replays":
                    raise _exceptions.Ballchasing.FailedReplay
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case 429:
                if self.auto_rate_limit is True:
                    time.sleep(self.patreon_tier.get_group)
                    return self.get_group(
                        group_id,
                        return_response = return_response
                    )
                else:
                    raise _exceptions.Ballchasing.RateLimitExceeded()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)


    def delete_group(
        self,
        group_id           : str,
        *,
        return_response : bool = ...
    ) -> Optional[requests.Response]:
        """
        Deletes the group with the corresponding `group ID` that has been created on Ballchasing by the key-holder.

        Arguments
        ---------
        `group_id` -> `str`
        
            The ID of the group.
        
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.

        Returns
        -------
        `Optional[requests.Response]`

        Raises
        ------
        `MissingAPIKey`
        
            If the API key is missing or invalid.
        
        `APIUnaccessible`
        
            If the API is down.
        """
        _ext.EnforceVars(Ballchasing.delete_group).enforce(
            return_response, "return_response", type_ = bool, filter_ = "x != ..."
        ).enforce(
            group_id, "group_id", type_ = str
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        URL="https://ballchasing.com/api/groups/" + group_id
        RESPONSE=requests.delete(URL, headers=self.auth)
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 204: return
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case 429:
                if self.auto_rate_limit is True:
                    time.sleep(self.patreon_tier.delete_group)
                    return self.delete_group(
                        group_id,
                        return_response = return_response
                    )
                else:
                    raise _exceptions.Ballchasing.RateLimitExceeded()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)


    def patch_group(
        self,
        group_id              : str,
        *,
        player_identification : Literal["by-id", "by-name"]                          = ...,
        team_identification   : Literal["by-distinct-players", "by-player-clusters"] = ...,
        parent                : str                                                  = ...,
        shared                : bool                                                 = ...,
        return_response       : bool                                                 = ...
    ) -> Optional[requests.Response]:
        """
        Used to update certain parameters of a group.

        Arguments
        ---------
        `group_id` -> `str`
        
            The group ID.
        
        `player_identification` -> `Literal["by-id", "by-name"]`
        
            How players are identified across the replays in the group.
        
        `team_identification` -> `Literal["by-distinct-players", "by-player-clusters"]`
        
            How teams are to be identified between replays. `by-distinct-players` means they will be grouped by fixed roster, whereas `by-player-clusters` means they will be grouped less strictly.
        
        `parent` -> `str`
        
            The parent group to assign this group to.
        
        `shared` -> `bool`
        
            Whether or not the group should be marked as shared.
        
        `return_response` -> `bool`
        
            If `True`, the function will simply return the `requests.Response`.

        Returns
        -------
        `Union[Literal[None], requests.Response]`

        Raises
        ------
        `ValueError`
        
            If none of the optional variables are defined.
        
        `MissingAPIKey`
        
            If the API key is missing or invalid.
        
        `APIUnaccessible`
        
            If the API is down.
        """
        _ext.EnforceVars(Ballchasing.patch_group).enforce(
            [return_response, shared], ["return_response", "shared"], type_ = bool, filter_ = "x != ..."
        ).enforce(
            group_id, "group_id", type_ = str
        ).enforce(
            [player_identification, team_identification, parent], ["player_identification", "team_identification", "parent"], type_ = str, filter_ = "x != ..."
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        data = _ext.kwargs_(
            ["player_identification", "team_identification", "parent", "shared"],
            [player_identification, team_identification, parent, shared]
        )
        if len(data) == 0:
            raise ValueError("At least one of \"player_identification\", \"team_identification\", \"parent\" or \"shared\" must be defined.")
        URL="https://ballchasing.com/api/groups/" + group_id
        RESPONSE=requests.patch(URL, headers=self.auth_json, data=json.dumps(data, separators=[",",":"]))
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 204: return
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case 429:
                if self.auto_rate_limit is True:
                    time.sleep(self.patreon_tier.patch_group)
                    return self.patch_group(
                        group_id,
                        player_identification = player_identification,
                        team_identification   = team_identification,
                        parent                = parent,
                        shared                = shared,
                        return_response       = return_response
                    )
                else:
                    raise _exceptions.Ballchasing.RateLimitExceeded()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)
    

    def maps(
        self,
        *,
        return_response : bool = ...
    ) -> Union[dict, requests.Response]:
        """
        Used to acquire a dictionary of current Rocket League maps, with `map id : map name` key-value pairs.

        Arguments
        ---------
        `return_response` -> `bool`
         
            If `True`, the function will simply return the `requests.Response`.

        Returns
        -------
        `Union[dict, requests.Response]`

        Raises
        ------
        `MissingAPIKey`
        
            If the API key is missing or invalid.
        
        `APIUnaccessible`
        
            If the API is down.
        """
        _ext.EnforceVars(Ballchasing.maps).enforce(
            [return_response], ["return_response"], type_ = bool, filter_ = "x != ..."
        )
        [return_response] = _ext.set_defaults(
            [return_response],
            [False]
        )
        URL="https://ballchasing.com/api/maps"
        RESPONSE=requests.get(URL, headers=self.auth)
        if return_response:
            return RESPONSE
        match RESPONSE.status_code:
            case 200: return RESPONSE.json()
            case 401: raise _exceptions.Ballchasing.MissingAPIKey()
            case 500: raise _exceptions.Ballchasing.APIUnaccessible()
            case _: raise _exceptions.Ballchasing.UnknownStatusCode(RESPONSE.status_code)
