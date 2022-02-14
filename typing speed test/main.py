# Import tkinter library
from tkinter import *
from datetime import datetime

# Create an instance of tkinter frame
win = Tk()
win.geometry("1000x800")
current_pos = 1
word_typed = 0
error_words = 0
first_type = True
time_start = None

type_text = "Python is an interpreted high-level general-purpose programming language. Its design philosophy " \
            "emphasizes code readability with its use of significant indentation. Its language constructs as well as " \
            "its object-oriented approach aim to help programmers write clear, logical code for small and large-scale "\
            "projects.\n\n "


# Define a function to highlight the text
def add_highlighter(is_true):
    if is_true:
        text.tag_add(f"{current_pos}", f"1.{current_pos - 1}", f"1.{current_pos}")
        text.tag_config(f"{current_pos}", background="#57fdbc", foreground="white")
    else:
        text.tag_add(f"{current_pos}", f"1.{current_pos - 1}", f"1.{current_pos}")
        text.tag_config(f"{current_pos}", background="#ffbebc", foreground="white")


def checker(event):
    global current_pos
    global error_words
    global word_typed
    global first_type
    global time_start
    if first_type:
        first_type = False
        time_start = datetime.now()
    elif current_pos + 3 == len(type_text):
        if type_text[current_pos - 1] == event.char:
            add_highlighter(True)
        else:
            add_highlighter(False)
        end_speed = Text(font=("Helvetica", 20, "bold"))
        end_speed.insert(INSERT, f"your speed is {round(word_typed/(datetime.now() - time_start).seconds * 60)}wpm")
        end_speed.pack()
    elif type_text[current_pos - 1] == event.char:
        add_highlighter(True)
        if event.char == ' ':
            if error_words <= 0:
                word_typed += 1
            else:
                error_words = 0
        current_pos += 1
    elif event.char == '':
        pass
    elif event.char == '\x08':
        current_pos -= 1
        backspace()
    else:
        add_highlighter(False)
        error_words += 1
        current_pos += 1


def backspace():
    global error_words
    error_words -= 1
    text.tag_add(f"{current_pos}", f"1.{current_pos - 1}", f"1.{current_pos}")
    text.tag_config(f"{current_pos}", background="#dcfa93", foreground="white")


# Create a Tex Field
text = Text(font=("Helvetica", 20, "bold"))
text.insert(INSERT, type_text)
text.pack()
win.bind('<KeyPress>', checker)


win.mainloop()
