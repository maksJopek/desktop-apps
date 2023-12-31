from tkinter import *
from mysql.connector import connect

root = Tk()
root.geometry("800x800")

db = connect(host="localhost", user="admin", password="qwerty", database="mjopek")

cursor = db.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS toDo(
                    id INT AUTO_INCREMENT,
                    task VARCHAR(250),
                    expire_date VARCHAR(10),
                    done BOOLEAN,
                    PRIMARY KEY(id)
                )"""
)


def set_task_done(id):
    cursor.execute("UPDATE `toDo` SET `done` = !`done` WHERE `id` = %s", (id,))
    db.commit()
    make_ui()


def remove_done_tasks():
    cursor.execute("DELETE FROM `toDo` WHERE `done` = 1")
    db.commit()
    make_ui()


def remove_task(id):
    cursor.execute("DELETE FROM `toDo` WHERE `id` = %s", (id,))
    db.commit()
    make_ui()


def add_task(entry, date):
    task = entry.get()

    if task == "" or task is None:
        return

    cursor.execute(
        "INSERT INTO `toDo` (`task`, `expire_date`, `done`) VALUES(%s, %s, %s)",
        (str(task), str(date.get()), "0"),
    )

    db.commit()

    entry.delete(0, END)
    date.delete(0, END)

    make_ui()


def change_task_in_db(id, new_task, new_date):
    if new_task == "" or new_task is None:
        return

    if new_date == "" or new_date is None:
        cursor.execute(
            "UPDATE `toDo` SET `task` = %s WHERE `id` = %s", (str(new_task), id)
        )
    else:
        cursor.execute(
            "UPDATE `toDo` SET `task` = %s, `expire_date` = %s WHERE `id` = %s",
            (str(new_task), new_date, id),
        )

    db.commit()
    make_ui()


def make_window_change_task(id):
    modify_window = Toplevel(root)

    cursor.execute("SELECT * FROM `toDo` WHERE `id` = %s", (id,))
    task = cursor.fetchall()[0]

    task_entry = Entry(modify_window)
    task_entry.insert(END, task[1])
    date_entry = Entry(modify_window)
    date_entry.insert(END, task[2])
    task_label = Label(modify_window, text="Task: ")
    date_label = Label(modify_window, text="Date: ")

    def close_task_window(id, task_entry_get, date_entry_get):
        change_task_in_db(id, task_entry_get, date_entry_get)
        modify_window.destroy()

    submit_modification = Button(
        modify_window,
        text="Submit",
        command=lambda: close_task_window(id, task_entry.get(), date_entry.get()),
    )

    task_label.pack(side=TOP)
    task_entry.pack(side=TOP)
    date_label.pack(side=TOP)
    date_entry.pack(side=TOP)
    submit_modification.pack(side=TOP)


def make_ui():
    for slave in root.pack_slaves():
        slave.destroy()

    cursor.execute("SELECT * FROM `toDo`")
    tasks = cursor.fetchall()

    for task in tasks:
        frame = Frame(root)
        label = Label(frame, text=f"Till: {task[2]}; Task: {task[1]}     ")

        done_button = Button(frame, command=lambda id=task[0]: set_task_done(id))
        if task[3] == 1:
            label["fg"] = "gray"
            done_button["text"] = "Undone"
        else:
            label["fg"] = "blue"
            done_button["text"] = "Done"

        delete_button = Button(
            frame, text="Remove", command=lambda id=task[0]: remove_task(id)
        )
        modify_button = Button(
            frame, text="Edit", command=lambda id=task[0]: make_window_change_task(id)
        )

        label.pack(side=LEFT)
        done_button.pack(side=LEFT)
        delete_button.pack(side=LEFT)
        modify_button.pack(side=LEFT)
        frame.pack(side=TOP)

    frame = Frame(root)
    task_label = Label(frame, text="Task: ").pack(side=LEFT)
    entry = Entry(frame)
    entry.pack(side=LEFT)
    date_label = Label(frame, text="Date: ").pack(side=LEFT)
    date_entry = Entry(frame)
    add_button = Button(
        frame,
        text="Add task",
        command=lambda: add_task(entry, date_entry),
    )
    date_entry.pack(side=LEFT)
    add_button.pack(side=LEFT)
    frame.pack(side=BOTTOM)

    remove_done_button = Button(root, text="Remove done")
    remove_done_button["command"] = remove_done_tasks
    remove_done_button.pack(side=BOTTOM)


make_ui()

root.mainloop()
