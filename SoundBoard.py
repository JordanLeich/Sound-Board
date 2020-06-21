# Made by Jordan Leich on 6/21/2020

# imports
import time
import end
import restart
import os


def help():
    os.system('color B')
    print("""
        Sound List:
        1. Super Mario Sound
        2. Star Wars Sound
        Song List:
        3. SMLE - Halo (feat. Helen Tess) Song\n
        """)
    time.sleep(2)
    start()


def start():
    user_music_choice = input("Enter a number (1, 2, or 3) to play a sound or song or type help: ")
    print()
    time.sleep(2)

    if user_music_choice == '1':
        print('Playing sound...\n')
        time.sleep(2)
        import winsound
        winsound.PlaySound('mario.wav', winsound.SND_ASYNC)
        time.sleep(2)
        restart.restart()

    elif user_music_choice == '2':
        print('Playing sound...\n')
        time.sleep(2)
        import winsound
        winsound.PlaySound('starwars.wav', winsound.SND_ASYNC)
        time.sleep(2)
        restart.restart()

    elif user_music_choice == '3':
        from pygame import mixer
        mixer.init()
        mixer.music.load('halo.mp3')
        print('Playing song...\n')
        time.sleep(2)
        mixer.music.play()
        time.sleep(2)

        user_stop_choice = str(input('Type end if you wish you to end the song or type restart to play a different '
                                     'sound or song: '))
        print()
        time.sleep(2)

        if user_stop_choice.lower() == 'end' or user_stop_choice.lower() == 'e':
            print('Ending song...\n')
            time.sleep(2)
            mixer.music.load('halo.mp3')
            mixer.music.stop()
            end.end()

        elif user_stop_choice.lower() == 'restart' or user_stop_choice.lower() == 'r':
            mixer.music.load('halo.mp3')
            mixer.music.stop()
            restart.restart()

    elif user_music_choice.lower() == 'help' or user_music_choice.lower() == 'h':
        help()

    else:
        print("Error found...\n")
        time.sleep(1)
        restart.restart()


start()
