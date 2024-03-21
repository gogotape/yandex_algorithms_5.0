def find_common_tracks(playlists):
    if not playlists:
        return []

    common = {elem for elem in playlists[0]}
    for current_playlist in playlists:
        common = common.intersection(set(current_playlist))

    common_tracks = list(common)
    common_tracks.sort()
    return common_tracks


if __name__ == "__main__":
    n = int(input())
    playlists = []
    for _ in range(n):
        _ = input()
        playlists.append(input().split())
    res = find_common_tracks(playlists)
    print(len(res))
    print(*res)
