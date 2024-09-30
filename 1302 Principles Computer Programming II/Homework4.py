# GUI builder that logs and presents student information using technologies like tkiner, csv, and sql, and uses comments to make long and deep code more readable and recreatable

from tkinter import Tk, Entry, Text, END, font, Label, Button, BOTH
import sqlite3
from tkinter.messagebox import showinfo
from datetime import datetime
import csv

# Create the main application window
app = Tk()
app.title('Student Records')
app.geometry('600x600')

# Create a custom font with your desired size and other attributes
custom_font = font.nametofont("TkDefaultFont")  # Start with the default font
custom_font.configure(size=18)  # Set the desired font size

# Set the custom font as the default font for the application
app.option_add("*Font", custom_font)

# Connect to the SQLite database and create a cursor
conn = sqlite3.connect('records.db')
cursor = conn.cursor()

# Create a 'students' table in the database if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS students (pantherid INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
conn.commit()

# Create and place labels for PantherID, Name, and Email
pantherid_label = Label(master=app, text='PantherID')
pantherid_label.grid(row=0, column=0)
name_label = Label(master=app, text='Name')
name_label.grid(row=1, column=0)
email_label = Label(master=app, text='Email')
email_label.grid(row=2, column=0)

# Create and place entry widgets for PantherID, Name, and Email
pantherid_entry = Entry(master=app)
pantherid_entry.grid(row=0, column=1)
name_entry = Entry(master=app)
name_entry.grid(row=1, column=1)
email_entry = Entry(master=app)
email_entry.grid(row=2, column=1)

# Define a function to handle adding a student record
def on_add_student_button_clicked():
    # Step-1: Obtain info from entry widgets
    pantherid = int(pantherid_entry.get())
    name = name_entry.get()
    email = email_entry.get()

    # Step-2: Insert these info into the database
    cursor.execute('INSERT INTO Students (PantherID, Name, Email) VALUES (?,?,?)', (pantherid, name, email))
    conn.commit()

    # Clear the entry fields
    pantherid_entry.delete(0, END)
    name_entry.delete(0, END)
    email_entry.delete(0, END)

    # Show an information message
    showinfo(message='Student record added to the database...')

# Define a function to list student records
def on_list_student_button_clicked():
    cursor.execute('SELECT * from Students')
    records = cursor.fetchall()
    txt.delete(0.0, END)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    txt.insert(END, f'--- Student list as of {timestamp} ---\n')
    for record in records:
        txt.insert(END, f"PantherID: {record[0]}   Name:{record[1]}   Email:{record[2]}\n")


# Define a function to search records
def on_search_rec():
    # Gets the input panther ID
    pantherid = pantherid_entry.get()

    # Test if the pantherID was entered
    if pantherid:
        # Gets the records of the specific PantherID
        cursor.execute('SELECT * FROM STUDENTS WHERE PantherID=' + pantherid)
        records = cursor.fetchall()
        # Test to see if the panther ID had any records
        try:
            if records[0]:
                # Shows the record
                txt.delete(0.0, END)
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                txt.insert(END, f'--- Student list as of {timestamp} ---\n')

                for record in records:
                    txt.insert(END, f"PantherID: {record[0]}   Name:{record[1]}   Email:{record[2]}\n")

            else:
                showinfo(message='No record was found for ' + str(pantherid))

        except IndexError:
            showinfo(message='No record was found for ' + str(pantherid))

    else:
        showinfo(message='Please enter a PantherID to search for a record')

# Define a function to delete records
def del_rec():
    # Gets panther ID
    pantherid = pantherid_entry.get()

    # Test if panther ID was entered
    if pantherid:
        # Gets the record for the panther ID
        cursor.execute('SELECT * FROM STUDENTS WHERE PantherID=' + pantherid)
        records = cursor.fetchall()
        # Test if the records are there
        try:
            if records[0]:
                # Deletes the records of that panther ID
                cursor.execute('DELETE FROM STUDENTS WHERE PantherID=' + pantherid)

            else:
                showinfo(message='‘No record was found for ' + pantherid)

        except IndexError:
            showinfo(message='‘No record was found for ' + pantherid)

    else:
        showinfo(message='Please enter a PantherID to delete a record')


# Define a function to update records
def update_rec():
    # Gets info
    pantherid = pantherid_entry.get()
    name = name_entry.get()
    email = email_entry.get()

    # Test if info was entered
    if pantherid and name and email:
        # Finds the record
        cursor.execute('SELECT * FROM STUDENTS WHERE PantherID=' + pantherid)
        records = cursor.fetchall()
        # Test if there is a record
        try:
            if records[0]:
                # Updates the record
                cursor.execute('UPDATE STUDENTS SET name=' + name + ' where PantherID=' + pantherid)
                cursor.execute('UPDATE STUDENTS SET email=' + email + ' where PantherID=' + pantherid)
            else:
                showinfo(message='No record was found for' + pantherid)
        except IndexError:
            showinfo(message='No record was found for' + pantherid)
    else:
        showinfo(message='Please enter PantherID, Name and Email to update a record.')


# Define a function to export a file to csv
def csv_ep():
    # Gets the file database
    cursor.execute("select * from STUDENTS;")

    # Makes the database into a csv file
    with open("students.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)


# Create buttons for adding and listing student records
button_add = Button(master=app, text='Add Student', command=on_add_student_button_clicked)
button_add.grid(row=3, column=0, columnspan=1)

button_list = Button(master=app, text='List Students', command=on_list_student_button_clicked)
button_list.grid(row=4, column=0, columnspan=1)

# Create buttons for searching
button_search = Button(master=app, text='Search Record', command=on_search_rec)
button_search.grid(row=3, column=1, columnspan=1)

# Create button for deleting
button_del = Button(master=app, text='Delete Record', command=del_rec)
button_del.grid(row=4, column=1, columnspan=1)

# Create button for updating
button_upd = Button(master=app, text='Update Record', command=update_rec)
button_upd.grid(row=3, column=2, columnspan=1)

# Create button for exporting to csv
button_csv = Button(master=app, text='Export to CSV', command=csv_ep)
button_csv.grid(row=4, column=2, columnspan=1)

# Create a Text widget to display student records
txt = Text(master=app, height=10, width=50)
txt.grid(row=5, column=0, columnspan=3)

# Start the main application loop
app.mainloop()

# An GUI that logs student information into a sql .db file and presents it on demand
