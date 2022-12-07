import PySimpleGUI as sg
import process_query
import process_sql_query

def query_window(cnx):

    layout_query = [[sg.Text("Query your database:")],
            [sg.Text("Enter table name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
                    [sg.Button('Show Table')],
              [sg.Text("SQL Query:")],
              [sg.Multiline(size=(30, 5), key='textbox')],
              [sg.Button('SQL Query -> Output'), sg.Button('SQL Query -> Table'), sg.Exit()]]



    layout_error = [[sg.Text("Error messages:")],
        [sg.Multiline("", size=(100, 10), key='OUTPUT')],
        [sg.Text("Output:")],
        [sg.Multiline("", size=(100, 10), key='OUTPUT_GENERAL')]]

    layout = [
            [sg.Column(layout_query),
             sg.VSeperator(),
             sg.Column(layout_error)]           ]


    window = sg.Window("Jazz Database", layout, resizable=True).Finalize()
    window.Maximize()

    

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
        try:
            if event == 'SQL Query -> Table':
                query = values['textbox']
                process_sql_query.create(query, cnx)
                window['OUTPUT_GENERAL'].update(value="Query was successful")

            elif event == 'SQL Query -> Output':

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
                               
        except Exception as err:
            window['OUTPUT'].update(value="Error: " + str(err))

    cursor.close()
    cnx.close()

