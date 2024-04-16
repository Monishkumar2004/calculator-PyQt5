# Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel , QPushButton, QWidget, QVBoxLayout, QHBoxLayout,QGridLayout, QLineEdit
from PyQt5.QtGui import QFont

class CalcApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.resize(300,300)

        self.setStyleSheet("QWidget { background-color: #f0f0f8; }")

        # create all app objects and widgets
        col = 0
        row = 0


        self.input_box = QLineEdit()
        self.input_box.setFont(QFont("Times", 30))
        self.grid = QGridLayout()


        self.buttons = ['7', '8', '9', '/', 
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+',
                ]

        # All design here
        master_layout = QVBoxLayout()
                

        for number in self.buttons:
            button = QPushButton(number)
            button.setStyleSheet("QPushButton {font: 25pt Times; padding: 10px}")
            button.clicked.connect(self.button_clicked)

            self.grid.addWidget(button, row, col)
            col +=1
            if col >3:
                col = 0
                row += 1

        self.clear = QPushButton("Clear")
        self.clear.setStyleSheet("QPushButton {font: 25pt Times; padding: 10px;}")
        self.clear.clicked.connect(self.button_clicked)
        self.delete =QPushButton('<')
        self.delete.setStyleSheet("QPushButton {font: 25pt Times; padding: 10px}")
        self.delete.clicked.connect(self.button_clicked)

        row3 = QHBoxLayout()
        row3.addWidget(self.clear, alignment=Qt.AlignCenter)
        row3.addWidget(self.delete, alignment=Qt.AlignCenter)

        master_layout.addWidget(self.input_box)
        master_layout.addLayout(self.grid)
        master_layout.addLayout(row3)
        master_layout.setContentsMargins(25,25,25,25)

        self.setLayout(master_layout)


    # create functions

    def button_clicked(self):
        
        button = app.sender()
        text = button.text()
        if text == "=":
            if self.input_box.text() == "2+2":
                self.input_box.setText("HeLlO WOrLd")  
            else:
                equation = self.input_box.text()
                result = eval(equation)
                self.input_box.setText(str(result))
                print(equation)
        elif text == "Clear":
            self.input_box.clear()    
            print(text)
        elif text == "<":
            equation = self.input_box.text()    
            self.input_box.setText(equation[:-1])
            print(equation)
            print(text)
        # elif input_box.text() == "2+2=":
        #         input_box.setText("HeLlO WOrLd")             
        else:
            equation = self.input_box.text()
            self.input_box.setText(equation + text)    

    



# show/run app
# Main app object ans serrings
if __name__ == '__main__':
    app = QApplication([])
    main_window = CalcApp()
    # main_window.setStyleSheet("Qwidget { background-color:#f0f0f8; }")
    main_window.show()
    app.exec_()
