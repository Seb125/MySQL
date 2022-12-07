import mysql.connector
import numpy as np



def create(table_name, cnx):


    cursor = cnx.cursor()

    add_band = ("INSERT INTO band "
                   "(band_name) "
                   "VALUES (%s)")

    add_album = ("INSERT INTO album "
                   "(album_name, band_id) "
                   "VALUES (%s, %s)")


    data_band = (table_name[1], )

 
    

    # Insert new band
    try:
        cursor.execute(add_band, data_band)
        band_id = cursor.lastrowid

    except:
        # If band already exists in the database
        # search for band_id
        band_id_query = "SELECT band_id FROM band WHERE band_name = '{name}'".format(name = table_name[1])
        cursor.execute(band_id_query)

        rows = cursor.fetchall()
        band_id = rows[0][0]

    
    # Insert new album
    data_album = (table_name[0], band_id)

    try:
        cursor.execute(add_album, data_album)
        album_id = cursor.lastrowid
    except:
        album_id_query = "SELECT album_id FROM album WHERE album_name = '{name}'".format(name = table_name[0])
        cursor.execute(album_id_query)
        rows = cursor.fetchall()
        album_id = rows[0][0]
    

    # Insert song names
    data_songs = table_name[2]
    song_list = data_songs.split(",")

    for song in song_list:
        try:
            song_query = "INSERT INTO song (song_name) VALUES ('{name}')".format(name = song)
            cursor.execute(song_query)
            song_id = cursor.lastrowid
        except:
            song_id_query = "SELECT song_id FROM song WHERE song_name = '{name}'".format(name = song)
            cursor.execute(song_id_query)

            rows = cursor.fetchall()
            song_id = rows[0][0]
        
        # Insert record
        record_query = "INSERT INTO record (song_id, album_id, record_year) VALUES ({song}, {album} ,{year})".format(song = song_id, album = album_id, year = table_name[4])
        cursor.execute(record_query)

        
    # Insert musicians
    data_musicians = table_name[3]
    musicians_list = data_musicians.split(",")

    data_instruments = table_name[5]
    instrument_list = data_instruments.split(",")

    for i, musician in enumerate(musicians_list):
        m_names = musician.split()

        try:
            musician_query = "INSERT INTO musician (musician_first_name, musician_last_name, musician_instrument) VALUES ('{first_name}', '{last_name}', '{instrument}')".format(first_name = m_names[0], last_name = m_names[1], instrument = instrument_list[i])
            cursor.execute(musician_query)
            musician_id = cursor.lastrowid
        except:
            musician_id_query = "SELECT musician_id FROM musician WHERE musician_first_name = '{first_name}' AND musician_last_name = '{last_name}'".format(first_name = m_names[0], last_name = m_names[1])
            cursor.execute(musician_id_query)

            rows = cursor.fetchall()
            musician_id = rows[0][0]

            
        # Insert band members

        member_query = "INSERT INTO members (member_musician_id, member_band_id) VALUES ({musician}, {band})".format(musician = musician_id, band = band_id)
        cursor.execute(member_query)
        
 
     

    # Make sure data is committed to the database
    cnx.commit()

 
