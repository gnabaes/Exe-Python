

from pygame import mixer

mixer.init()
mixer.music.load('rock.mp3')

mixer.music.play()

parar = input('Digite algo para parar...')

