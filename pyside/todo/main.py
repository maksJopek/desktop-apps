#!/usr/bin/env python
import sys
import os
import sqlite3
from datetime import datetime, timedelta
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QDateTimeEdit, QLineEdit, QMainWindow, QScrollArea, QSizePolicy, QStatusBar, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QCheckBox, QFormLayout, QGroupBox, QToolBar
from PySide6.QtCore import QDate, Qt, QDateTime

def create_title():
    lh = QLabel("Todo tasks tracker")
    lh.setAlignment(Qt.AlignHCenter) # type: ignore
    lhf = lh.font()
    lhf.setPointSize(50)
    lhf.setBold(True)
    lh.setFont(lhf)
    return lh

db = None
cur = None
def conn_to_db():
    global db, cur
    if db is not None:
        return
    data_path = './'
    filename = 'todo'
    os.makedirs(data_path, exist_ok=True)
    db = sqlite3.connect(data_path + filename + '.db')
    cur = db.cursor()
    db.execute('CREATE TABLE IF NOT EXISTS todo ( text TEXT, till VARCHAR(30), done BOOLEAN )')
    # cur.execute("INSERT INTO `todo` VALUES (:text, :till, :done)",
    #     {
    #         "text": f"{datetime.now()}",
    #         "till": datetime.now().strftime('%Y-%m-%d %H:%M'),
    #         "done": False,
    #     })
    db.commit()

    # db.close()

def get_todos():
    global cur 
    conn_to_db()
    cur.execute("SELECT *, oid FROM `todo`")
    todos = []
    for t in cur.fetchall():
        todos.append({
            "text": t[0],
            "till": datetime.strptime(t[1], '%Y-%m-%d %H:%M'),
            "done": t[2],
            "id": t[3],
    })
    # print(todos)
    return todos

get_todos()

class ScrollLabel(QScrollArea):
 
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setWidget(content)
        lay = QVBoxLayout(content)
        self.label = QLabel(content)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop) #type: ignore
        self.label.setWordWrap(True)
        lay.addWidget(self.label)
 
    def setText(self, text):
        self.label.setText(text)

    def text(self):
        return self.label.text()

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.tasks = get_todos()

        self.setWindowTitle("Todo app")
        self.edit_window = EditWindow(self.tasks, self)
        self.edit_window.hide()
        widget = QWidget()
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)

        main_layout = QFormLayout()
        widget.setLayout(main_layout)
        scroll = QScrollArea()
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)

        real_main = QVBoxLayout()
        real_main.addWidget(create_title())
        real_main.addWidget(scroll)
        real_widget = QWidget()
        real_widget.setLayout(real_main)
        self.setCentralWidget(real_widget)

        main_layout.setContentsMargins(0, 20, 0, 0)
        main_layout.setSpacing(40)

        toolBar = QToolBar('Menu główne')
        toolBar.setStyleSheet("font-size: 20pt")
        self.addToolBar(toolBar)

        button = QAction('Add', self)
        button.setStatusTip('Add new task')
        button.triggered.connect(self.edit_window.add_task) #type: ignore
        toolBar.addAction(button)

        statusBar = QStatusBar(self)
        statusBar.setStyleSheet("font-size: 20pt;")
        self.setStatusBar(statusBar)

        self.main_layout = main_layout
        self.refresh()

    def refresh(self):
        def clearLayout(layout):
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    clearLayout(child.layout())
        clearLayout(self.main_layout)

        self.tasks = get_todos()
        self.edit_window.tasks = self.tasks

        for i, todo in enumerate(self.tasks):
            row = QHBoxLayout()
            l = ScrollLabel()
            l.setText(f'<font>{i + 1}. {todo["text"]}</font>')
            e = QPushButton("Edit")
            e.clicked.connect(lambda a=todo["id"], b=todo["id"]: self.edit_window.edit_task(a)) # type: ignore
            dl = QLabel("Done: ")
            dl.setAlignment(Qt.AlignRight | Qt.AlignVCenter) # type: ignore
            d = QCheckBox()
            d.setCheckState(Qt.CheckState.Checked if todo["done"] else Qt.CheckState.Unchecked)
            d.setStyleSheet("QCheckBox::indicator { width: 40px; height: 40px;}")
            d.stateChanged.connect(lambda b, a=todo["id"]: self.toggle_done(a, b)) # type: ignore
            t = QLabel(f'Do till: {todo["till"].strftime("%Y-%m-%d %H:%M")}')
            r = QPushButton("Remove")
            # print(f"todo id = {todo['id']}")
            c = todo["id"]
            r.clicked.connect(lambda b=c, z=c: self.remove_task(b, z)) # type: ignore

            if todo["till"] < datetime.now() and todo["done"] != 1:
                l.setText(f'<font color="red">MISSED!!!</font>&nbsp;&nbsp;&nbsp;<s>{l.text()}</s>')
                df = dl.font()
                df.setStrikeOut(True)
                dl.setFont(df)
                d.setEnabled(False)
                e.setEnabled(False)
                tf = t.font()
                tf.setStrikeOut(True)
                t.setFont(tf)

            row.addWidget(l)
            row.addWidget(e)
            row.addWidget(dl)
            row.addWidget(d)
            row.addWidget(t)
            row.addWidget(r)
            self.main_layout.addRow(row)


    def toggle_done(self, id, d):
        global cur, db 
        print(id, d)
        cur.execute("UPDATE `todo` SET done = :done WHERE oid = :id", { "id": id, "done": 1 if d == 2 else 0 })
        db.commit()

    def remove_task(self, id, a):
        global cur, db 
        cur.execute("DELETE FROM `todo` WHERE oid = :id", { "id": id, })
        db.commit()
        self.refresh()       

class EditWindow(QWidget):
    def __init__(self, tasks, parent):
        super().__init__()
        self.tasks = tasks
        self.parent = parent
        font = self.font()
        font.setPointSize(30)
        self.setFont(font)
        form = QFormLayout()

        self.lt = QLabel("What you have to do?")
        self.it = QLineEdit()
        form.addRow(self.lt, self.it)
        self.ld = QLabel("When is the deadline?")
        self.id = QDateTimeEdit(QDate.currentDate())
        # self.id.setDisplayFormat("mm:HH dd.MM.yyyy")
        self.id.setDisplayFormat("HH:mm dd.MM.yyyy")
        self.id.setMinimumDate(QDate.currentDate())
        form.addRow(self.ld, self.id)
        self.cbtn = QPushButton("Confirm")
        self.cbtn.clicked.connect(self.confirm) # type: ignore
        form.addRow(self.cbtn)

        self.setLayout(form)

    def add_task(self):
        self.it.setText("")
        self.id.setDateTime(QDateTime.currentDateTime())
        self.edit_id = None
        self.show()

    def edit_task(self, id):
        print(id)
        t = [x for x in self.tasks if x["id"] == id][0]
        self.it.setText(t["text"])
        self.id.setDateTime(QDateTime(t["till"]))
        self.edit_id = id
        self.show()

    def confirm(self):
        dt = self.id.dateTime().toPython()
        if self.edit_id is None:
            cur.execute("INSERT INTO `todo` VALUES (:text, :till, :done)", {
                "text": self.it.text(),
                "till": dt.strftime('%Y-%m-%d %H:%M'),
                "done": False,
            })
            self.tasks.append({ "text": self.it.text(), "till": dt.strftime('%Y-%m-%d %H:%M'), "done": False, "id": self.edit_id, })
        else:
            t = [x for x in self.tasks if x["id"] == self.edit_id][0]
            cur.execute("UPDATE `todo` SET text = :text, till = :till, done = :done WHERE oid = :id", {
                "text": self.it.text(),
                "till": dt.strftime('%Y-%m-%d %H:%M'),
                "done": t["done"],
                "id": self.edit_id,
            })
        db.commit()
        self.parent.refresh()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    app.exec()
