A full-functionality wrapper for the https://ballchasing.com API.
# Install
`pip install pychasing`
# pychasing.Client
The main object used to interact with the API. Has the below methods:
- `ping` - pings the ballchasing servers.
- `upload_replay` - uploads a replay to the token-holder's account.
    - NOTE: this takes a `BinaryIO` object. For example:
    ```py
    with open("my_replay.replay", "rb") as replay_file:
        ...upload_replay(replay_file, ...)
    ```
- `list_replays` - list replays (basic information only) filtered on various criteria.
- `get_replay` - get the in-depth information of a specific replay.
- `delete_replay` - delete a specific replay, so long as it is owned by the token-holder.
    - NOTE: this operation is **permenant** and cannot be undone.
- `patch_replay` - edit the `title`, `visibility` or parent `group` of a specific replay.
- `download_replay` - download the raw bytes of a specific replay, so long as it is not private (unless it is owned by the token-holder).
    - NOTE: since replays are relatively large, they should be downloaded in chunks. For example:
    ```py
    with ...download_replay(...) as data_stream:
        with open("my_replay.replay", "wb") as replay_file:
            for chunk in data_stream.iter_content(chunk_size=4096):
                replay_file.write(chunk)
    ```
- `create_group` - create a replay group.
- `list_groups` - list groups (basic information only) filtered on various criteria.
- `get_group` - get in-depth information of a specific replay group.
- `delete_group` - delete a specific group, so long as it is owned by the token-holder.
    - NOTE: this operation is **permenant** and cannot be undone.
- `patch_group`edit the `player-identification`, `team-identification`, `parent`, or `shared` status of a specific replay group, so long as it owned by the token-holder.
- `maps` - list all the maps in the game.
- `get_threejs` - get basic locational data (among other data) of a specific replay.
    - NOTE: this functionality is highly experimental. It accesses a back-end API used for populating site data (that notably does not require authorization headers). At any time, this API could become restricted or its functionality could change.
- `get_timeline` - get basic timeline data of a specific replay.
    - NOTE: this functionality is highly experimental. It accesses a back-end API used for populating site data (that notably does not require authorization headers). At any time, this API could become restricted or its functionality could change.
- `export_csv` - get group statistics formatted as semi-colon-separated values.
# Helper types
## pychasing.types.Rank
Represents an in-game rank (`Unranked` to `SSL`).
## pychasing.types.Playlist
Represents an in-game playlist, e.g. `Hoops`, `Rumble`, `Ranked Duels`.
## pychasing.types.Platform
Represents the current playable platforms (`Steam`, `Epic`, `XBox`, `PlayStation`, `Switch`).
## pychasing.types.Map
Represents an in-game map, e.g. `Starbase Arc`, `arc_p`.
## pychasing.types.PatreonTier
Represents a patreon tier for `ballchasing`'s patreon. Tiers include `GrandChampion`, `Champion`, `Diamond`, `Gold`, and ``Regular` (no patreon tier).
## pychasing.types.Visibility
Represents the visibility of a replay or group, i.e. `public`, `unlisted`, and `private`.
## pychasing.types.PlayerIdentification
Represents a type of player identification for groups, i.e. `by id` and `by name`.
## pychasing.types.TeamIdentification
Represents a type of team identification for groups, i.e. `by distinct players` and `by player clusters`.
## pychasing.types.MatchResult
Represents a result of a match, i.e. `win` or `loss`
## pychasing.types.SortBy
Represents a sorting method, e.g. `replay date`, `group creation date`, `group name`.
## pychasing.types.SortDir
Represents a sort direction, i.e. `ascending` and `descending`.
## pychasing.types.GroupStats
Represents a stat group when exporting CSV, e.g. `players`, `teams`.
