def song_decoder(song):

    dub = "WUB"
        
song = "AWUBWUBWUBBWUBWUBWUBC"

def song_decoder(song):
    decode = song.replace("WUB", " ")   
    listdecode = decode.split() 
    newsong = " ".join(listdecode)
    return newsong

midecode = song_decoder(song)
print(midecode)