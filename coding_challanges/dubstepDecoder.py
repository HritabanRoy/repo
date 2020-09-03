def song_decoder(song):
    song = ' '.join(song.split("WUB"))
    song = ' '.join(song.split())
    return song.strip()

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))