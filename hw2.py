songTitle= "Moscow"                 # The title of the song 
songArtist= "Autoheart"             # the artist of the song 
songGenre= "Indie Pop"              # the genre of the song
albumTitle= "Punch"                 # the title of the song's album
yearReleased= 2013                  # the year that the album was released
cityOfOrigin= "London"              # the city that the band is from
countryOfOrigin= "England"          # the country that the band is from 
songDurationInMinutes= (3*(55/60))  # the duration of the song, converted to a float variable in minutes
songListens= 4584034                # the amount of listens, according to Spotify
monthlyListeners= 85321             # the band's monthly listeners, according to Spotify
bandMembers= 3                      # the amount of people in the band
bandMales, bandFemales= 3,0         # the distribution of males vs. females in the band (assuming gender binaries for simplicity's sake)
chorusRepeats= 0                    # the amount of times the chorus is played in the song. I listened to the song and added an iteration each time I heard the chorus
chorusRepeats += 1
chorusRepeats += 1
chorusRepeats += 1

def artist():
    print(songArtist)

def year():
    print(yearReleased)

def listens():
    print(songListens)

def memberQuiz(guess):
    if guess == bandMembers:
        check= True
    else:
        check= False
    print(check)
        

   
artist()
year()
listens()
memberQuiz(2)
memberQuiz(3)



