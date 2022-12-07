import PySimpleGUI as sg
import mysql.connector
import numpy as np


def create(sql_query, cnx):

    cursor = cnx.cursor()

 

    cursor.execute(sql_query)

    rows  = cursor.fetchall()

    list_of_lists = [list(elem) for elem in rows]


    # get columns names

    headings = [i[0] for i in cursor.description]



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

    window = sg.Window(sql_query, layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()
    



    
