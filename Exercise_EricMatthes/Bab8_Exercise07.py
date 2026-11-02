def make_album(artist, title, tracks=None):
    album = {
        "artist": artist,
        "title": title
    }
    if tracks is not None:
        album["tracks"] = tracks
    return album