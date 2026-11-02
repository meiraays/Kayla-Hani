def make_album(artist, title, tracks=None):
    album = {
        "artist": artist,
        "title": title
    }

    if tracks is not None:
        album["tracks"] = tracks

    return album

while True:
    print("\nEnter 'q' at any time to quit.")
    artist = input("Enter the artist's name: ")
    if artist.lower() == 'q':
        break

    title = input("Enter the album title: ")
    if title.lower() == 'q':
        break

    tracks_input = input("Enter the number of tracks (or leave blank): ")
    if tracks_input.lower() == 'q':
        break

    tracks = int(tracks_input) if tracks_input else None

    album_info = make_album(artist, title, tracks)
    print(f"\nAlbum Info: {album_info}")