import csv
from Song import Song

#list of songs
song_list = []

# Open the CSV file
with open('playlist.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Skip the first row
    next(reader)
    
    # Iterate over the remaining rows in the CSV file
    for row in reader:
        # Access all the songs
        title = row[0]
        artist = row[4].strip("[]'")
        rank = row[9]
        album_img = row[13]
        
        # Add songs to array of songs
        temp_song = Song(title,artist,rank,album_img)
        song_list.append(temp_song)
        
