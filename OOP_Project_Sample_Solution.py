# Create Song object
class Song:
    def __init__(self,name,artist,album):
        self.name = name
        self.artist = artist
        self.album = album
    def __repr__(self):
        return '\t%-30s %-30s %-30s'%(self.name,self.artist,self.album)

def find_song(requested_name,playlist_name):
    for song in playlists[playlist_name]:
            if song.name == requested_name:
                return True,song
    print(requested_name,'not found in',playlist_name)
    return False,None

def print_playlist(playlist_name):
    try: songList = playlists[playlist_name]
    except:
        print('Could not find',playlist_name)
        return 
    print('Playlist:',playlist_name)
    print('\t%-30s %-30s %-30s'%('Name','Artist','Album'))
    for song in songList: print(song)
    return 


# Construct playlists from .csv files in Playlists folder
playlists = {} # Dictionary of {'PlaylistName':[Songs in playlist]}
for playlist_name in ['All_Songs']: # Add names of playlists you want to import to the list
    playlists[playlist_name] = []
    for line in open('Playlists/%s.csv'%(playlist_name),'r'):
        name,artist,album = line.replace('\n','').split(',')
        playlists[playlist_name].append(Song(name,artist,album))

# Display Menu
i = 1
while i in range(1,8):
    print('''
            1. Print all Songs
            2. Create a Playlist
            3. Delete a Playlist
            4. Print all songs in a playlist
            5. Create a song
            6. Add a song to a playlist
            7. Print all playlists
            8. Exit
            ''')
    # Get user input
    try: i = int(input("\t\tOption: "))
    except:
        i = 1
        print("\tPlease input a number 1-8")
        continue
    # Preform menu action
    if i==1: # 1. Print All Songs
        print_playlist('All_Songs') 
    elif i==2: # Create a Playlist
        requested_playlist = input("Playlist to Create: ")
        playlists[requested_playlist] = []
        print('Type a song name to be added to',requested_playlist,'then press enter')
        print('When done, type quit then press enter')
        while True:
            requested_song = input(': ')
            if requested_song == 'quit': break
            found,songObj = find_song(requested_song,'All_Songs')
            if found: playlists[requested_playlist].append(songObj)
            else: print('Song not found')
    elif i==3: # Delete a playlist 
        # will not delete playlist's .csv file
        requested_playlist = input("Playlist to Deleted: ")
        try: del playlists[requested_playlist]
        except: print('Could not find',requested_playlist)
    elif i==4: # Print all songs in a playlist
        requested_playlist = input("Playlist: ")
        print_playlist(requested_playlist)
    elif i==5: # Create a Song
        songName = input('Song Name: ')
        songArtist = input('Song Artist: ')
        songAlbum = input('Song Album: ')
        playlists['All_Songs'].append(Song(songName,songArtist,songAlbum))
    elif i==6: # Add a song to a playlist
        requested_song = input('Song: ')
        found,songObj = find_song(requested_song,'All_Songs')
        if not found: continue
        requested_playlist = input('Playlist: ')
        try: playlists[requested_playlist].append(songObj)
        except: print('Could not find',requested_playlist)
    elif i==7: # Print all playlists
        for playlist_name,song_list in playlists.items():
            print(playlist_name)
    elif i==8: # Exit Application
        for playlist_name,song_list in playlists.items():
            f = open('Playlists/%s.csv'%(playlist_name),'w')
            for song in song_list: f.write('%s,%s,%s\n'%(song.name,song.artist,song.album))
            f.close()
    else:
        print(i,'is not a valid menu item. Please input a number 1-7')
        i=1

