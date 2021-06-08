import tkinter
import tkinter.ttk
import os

program_dir = os.getenv('LOCALAPPDATA') + "\\PythonReminders"


def save_reminder(text):

    print(text)


def draw_screen():
    top = tkinter.Tk()
    top.title("Reminders")

    # box dimensions:
    default_width = 450
    default_height = 350

    # get screen dimensions to center form
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()

    top.geometry(str(default_width) + "x" + str(default_height) + "+"
                 + str(int(screen_width / 2 - default_width / 2)) + "+"
                 + str(int(screen_height / 2 - default_height / 2)))

    top.resizable(False, False)
    # Code to add widgets will go here...
    textbox = tkinter.Text(top, width=50, height=10)
    textbox.pack()
    save_button = tkinter.Button(top, text="Save", command=lambda: save_reminder(textbox.get("1.0", 'end-1c')))
    save_button.pack()
    top.mainloop()


def output(text):
    print(text)


def main():
    my_string = "test"
    output(my_string)
    draw_screen()


if __name__ == "__main__":
    main()
