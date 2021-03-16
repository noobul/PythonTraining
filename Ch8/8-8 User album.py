def make_album(artis_name, album_name, number_of_songs = None):
    album_dictionary = {
        'name' : artis_name,
        'album' : album_name,
        }
    if number_of_songs:
        album_dictionary['nr_songs'] = number_of_songs
    print(album_dictionary)

loop = True
quit_message = "Type 'q' to quit or press 'Enter' to continue"
album_message = "What is your favourite album? "
artist_message = "By whom? "
song_nr_meesage = "Do you know how many songs does it have? (press 'Enter' to skip) "


while loop:
    album_name_prompt = input(album_message)
    artist_name_prompt = input(artist_message)
    song_nr_prompt = input(song_nr_meesage)
    quit_promt = input(quit_message)

    if quit_promt == 'q':
        break
    else:
        make_album(artist_name_prompt, album_name_prompt, song_nr_prompt)

