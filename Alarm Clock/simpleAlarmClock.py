from time import strftime
from time import sleep
import time
import os
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('fire alarm sound.mp3')





def set_alarm(alarm,now):



    print("Alarm set: ",alarm)

    while alarm != now:
        time.sleep(1)
        now = time.strftime('%H:%M')

    if alarm == now:
        print("Its time",alarm)
        pygame.mixer.music.play(loops=10, start=0.0)
        time.sleep(10)
        pygame.mixer.music.set_volume(10)


now = time.strftime('%H:%M')
print('now: ',now," o'clock")

#alarm = input('Set Alarm :e.g (21:30)')
alarm = '00:29'
set_alarm(alarm,now)
