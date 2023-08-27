#!/usr/bin/env python3

import os
import sys
import time
import threading

minutes = float(sys.argv[1])

def sound(t, freq):
    os.system(f'play -nq -t alsa synth {t} sine {freq} norm -1 gain -20')

def timer_thread(minutes):
    time.sleep(minutes * 60)  # Convert minutes to seconds and wait
    sound(1, 440)  # Play the sound for notification
    os._exit(0)  # Terminate the process

def main():
    timer = threading.Thread(target=timer_thread, args=(minutes,))
    timer.start()
    return

if __name__ == "__main__":
    main()
