#!/usr/bin/env python
import sys
from math import sin, cos, tan
from PySide6.QtWidgets import QMainWindow, QApplication 
from MainWindow import Ui_MainWindow
from pylab import *

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Menu")
        
        def onclick_push_btn(b):
            return lambda: onclick_push_btn2(b)
        def get_char_or_empty(string, index):
            try:
                return string[index]
            except IndexError:
                return ""
        def onclick_push_btn2(b):
            stxt = self.screen.text()
            last_char = get_char_or_empty(stxt, -1)
            last2_char = get_char_or_empty(stxt, -2)
            btext = b.text()
            if btext == "." and last_char == ".":  
                 return
            no_doubles = ["+", "*", "/"]
            if btext in no_doubles and (last_char in no_doubles or last_char == "-"):
                 return
            if btext == "-" and last_char == "-" and last2_char == "-":
                return
            self.screen.setText(stxt + btext)
            
        def onclick_special_btn(b):
            return lambda: onclick_special_btn2(b)
        def onclick_special_btn2(b):
            btext = b.text()
            stxt = self.screen.text()
            if stxt == "":
                return 
            def screen_eval(string):
                try:
                   self.screen.setText(str(eval(string)))
                except ZeroDivisionError:
                   self.screen.setText('') 
                except SyntaxError:
                   pass
            if btext == "=":  
                screen_eval(stxt)
            elif btext == "C":
                self.screen.setText("")
            elif btext in ["sin", "cos"]:
                screen_eval(f"{btext}({stxt})")
            elif btext == "tg":
                screen_eval(f"tan({stxt})")
            elif btext == "ctg":
                screen_eval(f"1/tan({stxt})")
                
        def onclick_draw_btn(b):
            return lambda: onclick_draw_btn2(b)
        def onclick_draw_btn2(b):
            btext = b.text()
            x = np.linspace((-2 * np.pi), (2 * np.pi), 256,endpoint=True)
            
            sine = np.sin(x)
            cosine = np.cos(x)
            tangent = np.tan(x)
            cotangent = 1/np.tan(x)
            
            if btext == "Draw sin":
                plot(x, sine, color="red", linewidth=2.5, linestyle="-", label="sin")
            elif btext == "Draw cos":
                plot(x, cosine, color="blue", linewidth=2.5, linestyle="-", label="cos")
            elif btext == "Draw tg":
                plot(x, tangent, color="orange", linewidth=2.5, linestyle="-", label="tan")
            elif btext == "Draw ctg":
                plot(x, cotangent, color="purple", linewidth=2.5, linestyle="-", label="cot")
            
            ax = gca()
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.spines['bottom'].set_position(('data',0))
            ax.yaxis.set_ticks_position('left')
            ax.spines['left'].set_position(('data',0))
            
            xlim(x.min()*1.1, x.max()*1.1)
            xticks([(-2 * np.pi), (-3 * np.pi/2), -np.pi, -np.pi/2, 0, np.pi/2, np.pi, (3 * np.pi/2), (2 * np.pi)], [r'$-2\pi$', r'$-3/2\pi$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$', r'$3/2\pi$', r'$2\pi$'])
            
            ylim(-4, 4)
            yticks([-4, -3, -2, -1, +1, +2, +3, +4], ['-4', '-3', '-2', '-1', '+1', '+2', '+3', '+4'])
            
            for label in ax.get_xticklabels() + ax.get_yticklabels():
              label.set_fontsize(16)
              label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
            
            show()

            

        push_btns = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9, self.b0, self.b_period, self.b_plus, self.b_asterisk, self.b_minus, self.b_divide];
        for b in push_btns:
            b.clicked.connect(onclick_push_btn(b))

        special_btns = [self.b_equal, self.b_c,self.b_sin, self.b_cos, self.b_tg, self.b_ctg]
        for b in special_btns:
            b.clicked.connect(onclick_special_btn(b))

        draw_btns = [self.b_dsin, self.b_dcos, self.b_dtg, self.b_dctg]
        for b in draw_btns:
            b.clicked.connect(onclick_draw_btn(b))


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

