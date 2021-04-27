from tkinter import *
import sqlite3

root = Tk()
lst = []


def draw_root():
    global root, lst

    conn = sqlite3.connect("databases/diary.db")
    cursor = conn.cursor()
    cursor.execute("SELECT *, oid FROM `diary`")
    # cursor.execute("DELETE FROM `diary` WHERE oid = 4 OR oid = 5 OR oid = 6")
    lst = cursor.fetchall()
    # conn.commit()
    conn.close()
    # print(str(lst))
    lst.insert(0, ("", "1 term grade", "2 term grade", "Final grade"))

    grid_slaves = root.grid_slaves()
    for l in grid_slaves:
        l.destroy()

    total_rows = len(lst)
    total_columns = len(lst[0])
    avg = [0, 0, 0]
    for i in range(total_rows):
        if i != 0:
            avg[0] += lst[i][1]
            avg[1] += lst[i][2]
            avg[2] += lst[i][3]
        if i == 0:
            bg = "black"
            fg = "white"
        elif i % 2 == 0:
            bg = "black"
            fg = "lightblue"
        else:
            bg = "white"
            fg = "blue"
        for j in range(total_columns):
            label = Label(
                root,
                width=15,
                fg=fg,
                bg=bg,
                font=("Arial", 16, "bold"),
                text=str(lst[i][j]).title(),
                borderwidth=2,
                relief="groove",
            )
            label.grid(row=i, column=j)

    for i in range(len(avg)):
        avg[i] = round(avg[i] / (total_rows - 1), 2)

    for j in range(total_columns):
        if j == 0:
            text = "Average"
        else:
            text = str(avg[j - 1])
        if total_rows % 2 == 1:
            bg = "white"
            fg = "black"
        else:
            bg = "black"
            fg = "white"

        label = Label(
            root,
            width=15,
            fg=fg,
            bg=bg,
            font=("Arial", 16, "bold"),
            text=text,
            borderwidth=2,
            relief="groove",
        )
        label.grid(row=total_rows, column=j)

    button = Button(
        root,
        command=add_subject,
        text="Click to add new subject",
        width=20,
        height=2,
        fg="black",
        bg="white",
        font=("Arial", 12, "bold"),
        borderwidth=2,
        relief="groove",
    )
    button.grid(row=total_rows + 1, column=0, columnspan=4, padx=20, pady=20)


def add_subject():
    global root, lst

    newWindow = Toplevel(root)
    newWindow.title("Add subject")

    texts = [
        "Subject name: ",
        "First term grade: ",
        "Second term grade: ",
        "Final grade: ",
        "",
    ]
    entries = []
    labels = []
    for x in range(len(texts)):
        label = Label(
            newWindow,
            width=20,
            fg="white",
            bg="black",
            font=("Arial", 16, "bold"),
            borderwidth=2,
            relief="groove",
            text=texts[x],
        )
        if x != len(texts) - 1:
            entries.append(StringVar(root))
            entry = Entry(
                newWindow,
                width=20,
                fg="white",
                bg="black",
                font=("Arial", 16, "bold"),
                borderwidth=2,
                relief="groove",
                text=texts[x],
                textvariable=entries[x],
            )
            entry.grid(row=x, column=1)
            label.grid(row=x, column=0)
        else:
            label.grid(row=x, column=0, columnspan=2)
        labels.append(label)

    def redraw_root():
        global block_popup

        conn = sqlite3.connect("databases/diary.db")
        cursor = conn.cursor()

        for x in range(len(entries)):
            if entries[x].get() == "":
                labels[len(labels) - 1]["text"] = "Give all data!"
                return
            elif x != 0 and entries[x].get().isnumeric() == False:
                labels[len(labels) - 1]["text"] = "Grades are numbers!"
                return

        cursor.execute(
            "INSERT INTO `diary` VALUES (:subject, :first_grade, :second_grade, :final_grade)",
            {
                "subject": entries[0].get(),
                "first_grade": entries[1].get(),
                "second_grade": entries[2].get(),
                "final_grade": entries[3].get(),
            },
        )
        conn.commit()
        conn.close()

        newWindow.destroy()
        draw_root()

    button = Button(
        newWindow,
        command=redraw_root,
        text="Confirm new subject",
        width=20,
        height=2,
        fg="black",
        bg="white",
        font=("Arial", 12, "bold"),
        borderwidth=2,
        relief="groove",
    )
    button.grid(
        row=(len(texts) + 1), column=0, rowspan=2, columnspan=2, padx=20, pady=20
    )


draw_root()
root.mainloop()
