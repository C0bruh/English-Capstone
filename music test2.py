from pygame import mixer
music = 'e:/Users/TNat\Desktop/,/music/After Dark.mp3'
mixer.init()
mixer.music.load(music)
mixer.music.play()