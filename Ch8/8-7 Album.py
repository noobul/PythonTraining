def make_album(artis_name, album_name, number_of_songs=None):
    album_dictionary = {
        'name' : artis_name,
        'album' : album_name,
        }
    if number_of_songs:
        album_dictionary['nr_songs'] = number_of_songs
    print(album_dictionary)

make_album('Pink Floyd', "Dark side of the Moon")
make_album("Led Zeppelin", "IV")
make_album("Come", "Orizont", "10")
