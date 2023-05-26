import Backend
import SongReader
import random
from Song import Song

print()
print("Select the most popular song out of the two choices!\nUse 1/2 to select the song")
print()

Backend.start_game()

i = 1
while i == 1:
    
    print("Song 1:", Backend.return_current_song().get_name(), "\nArtist:", Backend.return_current_song().get_artist())
    print()
    print("Song 2:", Backend.return_new_song().get_name(), "\nArtist:", Backend.return_new_song().get_artist())
    print()

    songChoice = input("Select the song:")
    print()

    if songChoice == "1":
        i = Backend.selected_current()

    elif songChoice == "2":
        i = Backend.selected_new()

    else:
        print("sorry not a valid caracter")
        i = 0


print()
print("Sorry, game over. Your score was",Backend.get_score())