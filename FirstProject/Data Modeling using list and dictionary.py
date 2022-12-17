# --------------------------------------- creating spotify playlists -----------------------------------------------
playlists = {
    "title": "Patagonia Bus",
    "author": "colt steele",
    "songs": [
        {
            "title": "song1",
            "artist": ["blue"],
            "duration": 2.5,
        },
        {
            "title": "song2",
            "artist": ["kity", "dj blue"],
            "duration": 5.25,
        },
        {
            "title": "meow meow",
            "artist": ["garfield"],
            "duration": 2.0,
        }
    ]
}

total_length = 0
for song in playlists["songs"]:
    print(song["title"])
    total_length += song["duration"]

print(f"Total Length: {total_length}")
