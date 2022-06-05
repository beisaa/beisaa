from tkinter import *
import pyperclip as pc

#FRAME

master = Tk()

cc = '#d32710'

canvas = Canvas(master, height=650, width=750)
canvas.pack()

frame_ust = Frame(master, bg=cc)
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.80, relheight=0.13)

frame_sol = Frame(master, bg=cc)
frame_sol.place(relx=0.1, rely=0.26, relwidth=0.23, relheight=0.5)

frame_sag = Frame(master, bg=cc)
frame_sag.place(relx=0.34, rely=0.26, relwidth=0.56, relheight=0.5)

top_text = Label(frame_ust, bg=cc, text="LaTeX Table Generator", font='Verdana 12 bold')
top_text.pack(padx=10, pady=10, side=LEFT)

top_text_right = Label(frame_ust, bg=cc, text="Version 0.1.1", font='Verdana 12 bold')
top_text_right.pack(padx=10, pady=10, side=RIGHT)

#FUNC


def open_text_file():
    # file type
    fdd = open("myfile.txt")
    # show the open file dialog
    # read the text file and show its content on the Text
    data_txt.insert('1.0', fdd.read())


columns_var = StringVar()
row_var = StringVar()


def empty():
    data_txt.delete('1.0', END)


def set1():

    empty()

    colums=columns_var.get()
    rows=row_var.get()

    i = 0
    model = '{' + ('|c' * int(float(colums))) + '|}'

    tabular = "{tabular}"
    mode = f"{model}"
    blank = "&" * (int(colums) - 1)
    row = f"{blank}" + r"\\ \hline"

    with open("myfile.txt", "w") as file:
        file.write("\n"r"\begin{table}""\n")
        file.write(r"\centering""\n")
        file.write(fr"\begin{tabular}{mode}""\n")
        file.write(r"\hline""\n")

        while i < int(rows):
            file.write(f"{row}""\n")
            i += 1

        file.write(fr"\end{tabular}""\n")
        file.write(r"\end{table}")


def copy():
    cpy = open('myfile.txt', 'r').read()
    pc.copy(cpy)
    pc.paste()
#PartB


Label(frame_sol, bg=cc, text='Variable', font='Verdana 12 bold').pack(pady=10, padx=10, anchor=NW)

Label(frame_sol, bg=cc, text='Colums', font='Verdana 8 bold').pack(pady=10, padx=10, anchor=NW)

B2 =Entry(frame_sol, textvariable=columns_var, bg='#fff', font='Verdana 8 ')
B2.pack(padx=15, pady=3, anchor=NW)

Label(frame_sol, bg=cc, text='Rows', font='Verdana 8 bold').pack(pady=10, padx=10, anchor=NW)

B2 =Entry(frame_sol, textvariable=row_var, bg='#fff', font='Verdana 8 ')
B2.pack(padx=15, pady=3, anchor=NW)

set_button = Button(frame_sol, text="Set",command=set1, width=20, bg="#5f5e5e", fg="black")
set_button.pack(padx=15, pady=10, anchor=SW)

print_button = Button(frame_sol, text="Print",command=open_text_file, width=20, bg="#5f5e5e", fg="black")
print_button.pack(padx=15, pady=10, anchor=SW)


#part c


Label(frame_sag, text="Give Data", bg=cc, font="Verdana 10 bold").pack(padx=10, pady=10, anchor=NW)

data_txt = Text(frame_sag, height=15, width=50)
data_txt.tag_configure('style', foreground='#bfbfbf', font=('Verdana', '7', 'bold'))
data_txt.pack()


data_send_txt = Button(frame_sag, text="Copy", command=copy, bg="#5f5e5e", fg="white")
data_send_txt.pack(pady=5, padx=10, anchor=SE)


master.mainloop()

