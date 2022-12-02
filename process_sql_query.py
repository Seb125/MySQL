import PySimpleGUI as sg
import mysql.connector
import numpy as np


def create(sql_query):

    cnx = mysql.connector.connect(user='root', password='Dhwoiue832749823',
                              host='127.0.0.1',
                              database='Jazz')


    cursor = cnx.cursor()

    query = (sql_query)

    cursor.execute(query)

    rows  = cursor.fetchall()

    list_of_lists = [list(elem) for elem in rows]


  # geth columns names

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

    window = sg.Window("Contact Information Window", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
            
    window.close()
    cursor.close()
    cnx.close()
