import argparse
import os
import pygame
from threading import Thread
from time import sleep, perf_counter

class Metronome(Thread):
    def __init__(self, bpm, sound_file):
        super().__init__()
        self.bpm = bpm  # beats per minute
        self.sound_file = sound_file  # path to sound file
        self.running = True  # flag to control when the metronome should stop

    def run(self):
        # initialize pygame mixer
        pygame.mixer.init()
        # load sound file
        sound = pygame.mixer.Sound(self.sound_file)
        # calculate delay between ticks based on bpm
        delay = 60 / self.bpm
        print(self.bpm, 'bpm')
        prev = perf_counter()
        while self.running:
            # play sound
            sound.play()
            # sleep for delay seconds
            sleep(delay)
            t = perf_counter()
            delta = t - prev - delay
            # recalculate delay based on current bpm
            delay = 60 / self.bpm
            prev = t

    def stop(self):
        # set running flag to False to stop the metronome
        self.running = False

def main():
    # parse command-line arguments
    parser = argparse.ArgumentParser(description='A simple command-line metronome.')
    parser.add_argument('bpm', type=int, help='beats per minute')
    parser.add_argument('--sound-file', type=str, default='click.wav', help='path to sound file')
    args = parser.parse_args()

    # construct absolute path to sound file
    sound_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.sound_file)

    # create and start metronome thread
    metronome = Metronome(args.bpm, sound_file_path)
    metronome.start()

    while True:
        # read command from user input
        command = input('Enter command (q to quit, c to change bpm): ')
        if command == 'q':
            # stop metronome and exit program
            metronome.stop()
            break
        elif command == 'c':
            # read new bpm from user input and update metronome bpm
            bpm = int(input('Enter new bpm: '))
            metronome.bpm = bpm

if __name__ == '__main__':
    main()