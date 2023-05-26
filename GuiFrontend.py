import tkinter as tk
from PIL import ImageTk, Image
import Backend
import SongReader
import random
from Song import Song

# Create the main window
window = tk.Tk()
window.title("Song Game")

# Load the song data and start the game
Backend.start_game()

# Function to update the song choices and album art
def update_songs():
    song1_name = Backend.return_current_song().get_name()
    song1_artist = Backend.return_current_song().get_artist()
    song2_name = Backend.return_new_song().get_name()
    song2_artist = Backend.return_new_song().get_artist()

    # Update the song labels
    song1_label.config(text="Song 1: {}\nArtist: {}".format(song1_name, song1_artist))
    song2_label.config(text="Song 2: {}\nArtist: {}".format(song2_name, song2_artist))

    # Load and display the album art
    album1_img = Image.open(Backend.return_current_song().get_album_img())
    album1_img = album1_img.resize((150, 150), Image.ANTIALIAS)
    album1_photo = ImageTk.PhotoImage(album1_img)
    album1_label.config(image=album1_photo)
    album1_label.image = album1_photo

    album2_img = Image.open(Backend.return_new_song().get_album_img())
    album2_img = album2_img.resize((150, 150), Image.ANTIALIAS)
    album2_photo = ImageTk.PhotoImage(album2_img)
    album2_label.config(image=album2_photo)
    album2_label.image = album2_photo

# Function to handle song selection
def select_song(choice):
    if choice == 1:
        i = Backend.selected_current()
    elif choice == 2:
        i = Backend.selected_new()
    else:
        print("Sorry, not a valid character.")
        i = 0

    # Check if the game is over
    if i == 0:
        score_label.config(text="Sorry, game over. Your score was {}".format(Backend.get_score()))
        # Clear the window and show a new screen
        clear_window()
        game_over_label.config(text="Game Over\n\nFinal Score: {}".format(Backend.get_score()))
        game_over_label.pack()
    else:
        score_label.config(text="Score: {}".format(Backend.get_score()))
        update_songs()

# Function to clear the window
def clear_window():
    for widget in window.winfo_children():
        widget.pack_forget()

# Create the song labels
song1_label = tk.Label(window, font=("Arial", 12))
song1_label.pack(pady=10)

album1_label = tk.Label(window)
album1_label.pack()

song2_label = tk.Label(window, font=("Arial", 12))
song2_label.pack(pady=10)

album2_label = tk.Label(window)
album2_label.pack()

# Create the score label
score_label = tk.Label(window, font=("Arial", 12))
score_label.pack(pady=10)

# Create the "Game Over" label
game_over_label = tk.Label(window, text="Game Over", font=("Arial", 25))

# Create the button widgets
song1_button = tk.Button(window, text="Select Song 1", command=lambda: select_song(1))
song1_button.pack(side="left", padx=10)

song2_button = tk.Button(window, text="Select Song 2", command=lambda: select_song(2))
song2_button.pack(side="right", padx=10)

# Initial update of the song choices and album art
update_songs()

# Run the main window loop
window.mainloop()
