A full-functionality wrapper for the https://ballchasing.com API.

# Install

`$ pip install pychasing`

# The pychasing Client

The `pychasing.Client` class is the main object used to interact with the Ballchasing API.

```py
import pychasing

pychasing_client = pychasing.Client(
    token="your_token",
    auto_rate_limit=True,
    patreon_tier=pychasing.PatreonTier.none # same as "regular"
)
```

Before we get into the methods of `Client`, there are a few things to note about rate limit handling. If `auto_rate_limit` is set to `False`, any request you make will be immediately sent to the ballchasing API. If `auto_rate_limit` is set to `True`, the client will automatically limit the rate of your requests, taking into account both hourly quota and burst limit. This is done through `time.sleep`, so how long it takes to get a response from a given method will depend on how often you are using the API, as well as your Ballchasing Patreon tier. Additionally, there is a `rate_limit_safe_start` option; if this option is set to `True`, the rate limiting will start off as already maxed out on API calls. This prevents any issues from arising if you are reinstantiating the client often (e.g. if you are testing by running a script multiple times). If this option is set to `False`, the rate limiter will assume that you haven't made any API calls in the past hour, and will rate limit accordingly. For long-running programs and use a single client instance, this option isn't necessarily needed, but I would always recommend it be enabled.

The `pychasing.Client` object has the below methods:
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
- `patch_group` - edit the `player-identification`, `team-identification`, `parent`, or `shared` status of a specific replay group, so long as it owned by the token-holder.
- `maps` - list all the maps in the game.
- `get_threejs` - get basic locational data (among other data) of a specific replay. This does not require
    - NOTE: this functionality is highly experimental. It accesses a back-end API used for populating site data (that notably does not require authorization headers). At any time, this API could become restricted or its functionality could change.
- `get_timeline` - get basic timeline data of a specific replay.
    - NOTE: this functionality is highly experimental. It accesses a back-end API used for populating site data (that notably does not require authorization headers). At any time, this API could become restricted or its functionality could change.
- `export_csv` - get group statistics formatted as semi-colon-separated values.

# Enums and other types

Many of the methods in `Client` can use custom enumerations for ease of use. For example, when setting the visibility of a replay through `Client.patch_replay`, you could set `visibility` to `"unlisted"` *or* `Visibility.unlisted`. These Enums are listed below:
- `pychasing.Rank` - used for `min_rank` and `max_rank` in `list_replays`
- `pychasing.Playlist` - used for `playlists` in `list_replays`
- `pychasing.Platform` - used for `platform` in `list_replays`
- `pychasing.Map` - used for `map` in `list_replays`
- `pychasing.Visibility` - used for `visibility` in `patch_replay` and `patch_group`
- `pychasing.PlayerIdentifiercation` - used for `player_identification` in `create_group` and `patch_group`
- `pychasing.TeamIdentification` - used for `team_identification` in `create_group` and `patch_group`
- `pychasing.MatchResult` - used for `match_result` in `list_replays`
- `pychasing.ReplaySortBy` - used for `sort_by` in `list_replays`
- `pychasing.GroupSortBy` - used for `sort_by` in `list_groups`
- `pychasing.SortDirection` - used for `sort_dir` in `list_replays` and `list_groups`
- `pychasing.GroupStats` - used for `stat` in `export_csv`
- `pychasing.PatreonTier` - used in the initialization of `Client`. This is the only exception to the aforementioned "str or enum" rule above; the proper initialization of `Client` **requires** the `PatreonTier` enum.

Additionally, all date parameters (which require an RFC3339 formatted datetime) also accept a `pychasing.Date`. For example:

```py
...list_replays(created_before="2022-11-22T05:00:30Z")
...list_replays(created_before=pychasing.Date(2022, 11, 22, 5, 0, 30)) 
```
