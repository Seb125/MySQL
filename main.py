import PySimpleGUI as sg
import mysql.connector
import process_query
import process_sql_query
import add_data_test


if __name__ == '__main__':

    sg.theme('dark grey 13')
    layout_query = [[sg.Text("Query your database:")],
            [sg.Text("Enter table name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
                    [sg.Button('Show Table')],
              [sg.Text("SQL Query:")],
              [sg.Multiline(size=(30, 5), key='textbox')],
              [sg.Button('SQL Query -> Output'), sg.Button('SQL Query -> Table'), sg.Exit()]]


    layout_update =[[sg.Text("Add new entry to the database:")],
        [sg.Text("Enter album name:"), sg.Input(key='-ALBUM_NAME-', do_not_clear=True, size=(20, 1))],
               [sg.Text("Enter record year:"), sg.Input(key='-RECORD-YEAR-', do_not_clear=True, size=(20, 1))],
          [sg.Text("Enter band name:"), sg.Input(key='-BAND_NAME-', do_not_clear=True, size=(20, 1))],
                [sg.Text("Enter song names:"), sg.Multiline(size=(30, 5), key='song_names')],
              [sg.Text("Enter musician names (Charlie Parker, Bill Evans):"), sg.Multiline(size=(30, 5), key='musician_names')],
        [sg.Text("Enter musicians instruments:"), sg.Multiline(size=(30, 5), key='instruments')],
                  [sg.Button('Add data to database')]]

    layout_error = [[sg.Text("Error messages:")],
        [sg.Multiline("", size=(100, 10), key='OUTPUT')],
        [sg.Text("Output:")],
        [sg.Multiline("", size=(100, 10), key='OUTPUT_GENERAL')]]

    layout = [
            [sg.Column(layout_query),
             sg.VSeperator(),
             sg.Column(layout_update),
             sg.VSeperator(),
             sg.Column(layout_error)]           ]


    window = sg.Window("Jazz Database", layout, resizable=True).Finalize()
    window.Maximize()

    cnx = mysql.connector.connect(user='root', password='Dhwoiue832749823',
                              host='127.0.0.1',
                              database='Jazz')

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        try:
            if event == 'SQL Query -> Table':
                query = values['textbox']
                process_sql_query.create(query, cnx)
                window['OUTPUT_GENERAL'].update(value="Query was successful")

            elif event == 'SQL Query -> Output':
                cnx = mysql.connector.connect(user='root', password='Dhwoiue832749823',
                              host='127.0.0.1',
                              database='Jazz')


                cursor = cnx.cursor()

                query = values['textbox']
                cursor.execute(query)
                rows  = cursor.fetchall()
                window['OUTPUT_GENERAL'].update(value=rows)

                cnx.commit()
                
            elif event == 'Show Table':
                table_name = values['-NAME-']     
                process_query.create(table_name, cnx)

                window['OUTPUT_GENERAL'].update(value="Query was successful")
                               
            elif event == 'Add data to database':
                new_entry = [values['-ALBUM_NAME-'], values['-BAND_NAME-'], values['song_names'], values['musician_names'], values['-RECORD-YEAR-'], values['instruments']]
                add_data_test.create(new_entry, cnx)

                window['OUTPUT_GENERAL'].update(value="Data was added successfully to your database")
                

        except Exception as err:
            window['OUTPUT'].update(value="Error: " + str(err))

    cursor.close()
    cnx.close()
