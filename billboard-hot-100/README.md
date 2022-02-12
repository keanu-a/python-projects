# Billboard Hot 100
This program will find the billboard hot 100 songs from a specific date, then make a spotify playlist of those songs.

## Program
1. Prompts user for a date (ex. 2012-08-12)
2. Using the BeautifulSoup module, the program gets each song title and stores it into a list.
3. Using the spotipy library, I authenticate my account and the program searches for each song and adds it into the playlist.

## Python modules used
- requests
- BeautifulSoup
- spotipy
- os
