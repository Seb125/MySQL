import PySimpleGUI as sg
import process_query
import process_sql_query


if __name__ == '__main__':


    layout = [[sg.Text("Enter table name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
              [sg.Text("SQL Query:")],
              [sg.Multiline(size=(30, 5), key='textbox')],
              [sg.Button('Start SQL Query'), sg.Button('Show Table'), sg.Exit()]]


    window = sg.Window("Jazz Database", layout, resizable=True).Finalize()
    window.Maximize()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Start SQL Query':
            query = values['textbox']
            process_sql_query.create(query)
        elif event == 'Show Table':
            table_name = values['-NAME-']     
            process_query.create(table_name)
