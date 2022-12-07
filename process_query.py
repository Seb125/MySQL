import PySimpleGUI as sg
import mysql.connector
import numpy as np


def create(table_name, cnx):


    cursor = cnx.cursor()

    query = ("SELECT * FROM " + table_name)

    cursor.execute(query)

    rows  = cursor.fetchall()

    list_of_lists = [list(elem) for elem in rows]


    culumn_names = ("SHOW COLUMNS FROM " + table_name)

    cursor.execute(culumn_names)

    rows2  = cursor.fetchall()



    headings = [name[0] for name in rows2]


    layout = [
            [sg.Table(values=list_of_lists, 
            headings=headings, 
            max_col_width=35,
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='right',
                        num_rows=10,
                        key='-TABLE-',
                        row_height=35)]
        ]

    window = sg.Window("Contact Information Window", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
            
    window.close()
 
