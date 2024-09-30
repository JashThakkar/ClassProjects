# This program recognizes and tells you what the key you pressed is. It is done in a TKINTER GUI

from tkinter import Tk, Entry, Text, END


def record(event):
    inp = ('Key = {}'.format(event.keysym))

    if len(inp) == 7:
        char = [chars for chars in inp]

        if char[6].isalpha():

            if char[6].isupper():
                text.insert(END, 'It is an uppercase letter.\n')

            else:
                text.insert(END, 'It is a lowercase letter.\n')

        elif char[6].isdigit():
            text.insert(END, 'It is a number.\n')

        else:
            text.insert(END, 'It is a non-alphanumeric key.\n')

    else:
        text.insert(END, 'It is a non-alphanumeric key.\n')


root = Tk()

entry = Entry(root)
entry.grid(row=0, column=1)
entry.bind('<KeyPress>', record)
entry.pack()

text = Text(root)
text.pack()

root.mainloop()

# You can type in the text box and the program will record what each keystroke is
