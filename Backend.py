import SongReader
import random
from Song import Song

playlist = SongReader.song_list
score = 0
current_song = Song
new_song = Song

def start_game():
    global current_song
    current_song = random.choice(playlist)
    select_random_song()

def return_current_song():
    return current_song

def return_new_song():
    return new_song

def score_point():
    global score
    score += 1

def get_score():
    return score

def select_random_song():
    if len(playlist) == 0:
        return None
    global new_song
    new_song = random.choice(playlist)

def selected_current():
    global current_song
    global new_song
    if current_song.get_rank() <= new_song.get_rank():
        score_point()
        select_random_song()
        return 1
    
    else:
        return 0

def selected_new():
    global current_song
    global new_song
    if current_song.get_rank() >= new_song.get_rank():
        score_point()
        current_song = new_song
        select_random_song()
        return 1
    
    else:
        return 0
    
def reset_game():
    global score
    score = 0
    start_game()
    