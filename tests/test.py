import sys
sys.path.append(".")
from src import pychasing


TOKEN              = ""
STEAM_ID           = ""
REPLAY_PATH        = "tests/test_replay.replay"
GROUP_NAME         = "__pychasing_test_group__"
REPLAY_NAME        = "__pychasing_test_replay__"
UPLOADED_REPLAY_ID = ""


pychasing_client = pychasing.Client(
    TOKEN,
    True,
    pychasing.PatreonTier.none,
    True
)


def test_ping() -> None:
    """Test the `pychasing.client.Client.ping` method."""
    res0 = pychasing_client.ping()
    print(res0.json())
    assert res0.json()["chaser"] is True
    print("\033[96mpychasing.client.Client.ping \033[90m: \033[92mGOOD\033[0m")


def test_list_replays() -> None:
    res0 = pychasing_client.list_replays(count=5, pro=True, playlists=[pychasing.Playlist.ranked_doubles])
    print(res0.json())
    assert len(res0.json()["list"]) == 5
    res1 = pychasing_client.list_replays(next = res0.json()["next"])
    print(res1.json())
    assert len(res1.json()["list"]) == 5
    assert res0.json()["list"][0]["id"] != res1.json()["list"][0]["id"]
    print("\033[96mpychasing.client.Client.list_replays \033[90m: \033[92mGOOD\033[0m")


def test_list_groups() -> None:
    res0 = pychasing_client.list_groups(count=5)
    print(res0.json())
    assert len(res0.json()["list"]) == 5
    res1 = pychasing_client.list_groups(next=res0.json()["next"])
    print(res1.json())
    assert len(res1.json()["list"]) == 5
    assert res0.json()["list"][0]["id"] != res1.json()["list"][0]["id"]
    print("\033[96mpychasing.client.Client.list_groups \033[90m: \033[92mGOOD\033[0m")


def test_maps() -> None:
    res0 = pychasing_client.maps()
    print(res0.json())
    assert res0.json()["arc_standard_p"] == "Starbase ARC (Standard)"
    print("\033[96mpychasing.client.Client.maps \033[90m: \033[92mGOOD\033[0m")


def test_create_group() -> None:
    res0 = pychasing_client.create_group(GROUP_NAME, pychasing.PlayerIdentification.by_id, pychasing.TeamIdentification.by_player_clusters)
    print(res0.json())
    assert "https://ballchasing.com/api/groups/" in res0.json()["link"]
    print("\033[96mpychasing.client.Client.create_group \033[90m: \033[92mGOOD\033[0m")


def test_upload_replay() -> None:
    groups = pychasing_client.list_groups(name=GROUP_NAME, creator=STEAM_ID)
    with open(REPLAY_PATH, "rb") as replay_file:
        res0 = pychasing_client.upload_replay(replay_file, pychasing.Visibility.private, group = groups.json()["list"][0]["id"])
        print(res0.json())
        print(f"\033[96mpychasing.client.Client.upload_replay \033[90m: \033[92mGOOD\033[0m\n\nNEW REPLAY ID: {res0.json()['id']}")


def test_get_replay() -> None:
    res0 = pychasing_client.get_replay(UPLOADED_REPLAY_ID)
    print(res0.json())
    assert res0.json()["id"] == UPLOADED_REPLAY_ID
    print("\033[96mpychasing.client.Client.get_replay \033[90m: \033[92mGOOD\033[0m")


def test_get_group() -> None:
    groups = pychasing_client.list_groups(name=GROUP_NAME, creator=STEAM_ID)
    res0 = pychasing_client.get_group(groups.json()["list"][0]["id"])
    print(res0.json())
    assert res0.json()["name"] == GROUP_NAME
    print("\033[96mpychasing.client.Client.get_group \033[90m: \033[92mGOOD\033[0m")


def test_patch_group() -> None:
    groups = pychasing_client.list_groups(name=GROUP_NAME, creator=STEAM_ID)
    res0 = pychasing_client.patch_group(groups.json()["list"][0]["id"], team_identification=pychasing.TeamIdentification.by_distinct_players)
    print(res0.content)
    assert res0.content == b""
    res1 = pychasing_client.get_group(groups.json()["list"][0]["id"])
    print(res1.json())
    assert res1.json()["team_identification"] == pychasing.TeamIdentification.by_distinct_players.value
    print("\033[96mpychasing.client.Client.patch_group \033[90m: \033[92mGOOD\033[0m")


def test_patch_replay() -> None:
    res0 = pychasing_client.patch_replay(UPLOADED_REPLAY_ID, title=REPLAY_NAME, visibility=pychasing.Visibility.public)
    print(res0.content)
    assert res0.content == b""
    res1 = pychasing_client.get_replay(UPLOADED_REPLAY_ID)
    print(res1.json())
    assert res1.json()["title"] == REPLAY_NAME
    print("\033[96mpychasing.client.Client.patch_replay \033[90m: \033[92mGOOD\033[0m")


def test_download_replay() -> None:
    with open(REPLAY_PATH, "rb") as replay_file:
        res0 = pychasing_client.download_replay(UPLOADED_REPLAY_ID)
        for c in res0.iter_content(chunk_size=100):
            chunk = c
            print(chunk)
            break
        print(replay_file.read(100))
        replay_file.seek(0)
        assert chunk == replay_file.read(100)
    print("\033[96mpychasing.client.Client.download_replay \033[90m: \033[92mGOOD\033[0m")


def test_experimentals() -> None:
    res0 = pychasing_client.get_threejs(UPLOADED_REPLAY_ID)
    print(res0.content[:100])
    input("\033[92mPress any key to continue...\033[0m")
    res1 = pychasing_client.get_timeline(UPLOADED_REPLAY_ID)
    print(res1.content[:100])
    input("\033[92mPress any key to continue...\033[0m")
    groups = pychasing_client.list_groups(name=GROUP_NAME, creator=STEAM_ID)
    res2 = pychasing_client.export_csv(groups.json()["list"][0]["id"], pychasing.GroupStats.players)
    print(res2.content[:100])


def test_delete_replay() -> None:
    res0 = pychasing_client.delete_replay(UPLOADED_REPLAY_ID)
    print(res0.content)
    assert res0.content == b""
    print("\033[96mpychasing.client.Client.delete_replay \033[90m: \033[92mGOOD\033[0m")


def test_delete_group() -> None:
    groups = pychasing_client.list_groups(name=GROUP_NAME, creator=STEAM_ID)
    res0 = pychasing_client.delete_group(groups.json()["list"][0]["id"])
    print(res0.content)
    assert res0.content == b""
    print("\033[96mpychasing.client.Client.delete_group \033[90m: \033[92mGOOD\033[0m")


if __name__ == "__main__":
    step = 0
    match step:
        case 0: test_ping()
        case 1: test_list_replays()
        case 2: test_list_groups()
        case 3: test_maps()
        case 4: test_create_group()
        case 5: test_upload_replay()
        case 6: test_get_replay()
        case 7: test_get_group()
        case 8: test_patch_group()
        case 9: test_patch_replay()
        case 10: test_download_replay()
        case 11: test_experimentals()
        case 12: test_delete_replay()
        case 13: test_delete_group()
        case 14: print("DONE!")
