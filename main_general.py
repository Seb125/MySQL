import PySimpleGUI as sg
import mysql.connector
import process_query
import process_sql_query
import add_data_test
import general_GUI

if __name__ == '__main__':

    sg.theme('dark grey 13')


    layout = [
            [sg.Text("Enter user name:"), sg.Input(key='-U-NAME-', do_not_clear=True, size=(20, 1))],
              [sg.Text("Enter password:"), sg.Input(key='-PASSWORD-', do_not_clear=True, size=(20, 1))],
            [sg.Text("Enter host:"), sg.Input(key='-HOST-', do_not_clear=True, size=(20, 1))],
            [sg.Text("Enter database name:"), sg.Input(key='-DATABASE-', do_not_clear=True, size=(20, 1))],
              [sg.Button('Connect'), sg.Exit()]]


    window = sg.Window("Connect to MySQL DataBase", layout)

 
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Connect':
            
            user = values['-U-NAME-']
            password = values['-PASSWORD-']
            host = values['-HOST-']
            database = values['-DATABASE-']

            cnx = mysql.connector.connect(user=user, password=password,
                              host=host,
                              database=database)
                
            general_GUI.query_window(cnx)
                
            #except:
                #print("Make sure to enter the correct access data")
                

        
    
