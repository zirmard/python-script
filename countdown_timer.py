
import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

seconds = int(input("Enter the time in seconds: "))
countdown_timer(seconds)
    