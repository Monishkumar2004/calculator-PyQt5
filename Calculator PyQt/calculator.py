# Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel , QPushButton, QWidget, QVBoxLayout, QHBoxLayout,QGridLayout, QLineEdit


# Main app object ans serrings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Calculator')
main_window.resize(300,300)


# create all app objects and widgets
col = 0
row = 0


input_box = QLineEdit()
grid = QGridLayout()


buttons = ['7', '8', '9', '/', 
           '4', '5', '6', '*',
           '1', '2', '3', '-',
           '0', '.', '=', '+',
           ]



# create functions

def button_clicked():
    
    button = app.sender()
    text = button.text()
    
    if text == "=":
        if input_box.text() == "2+2":
            input_box.setText("HeLlO WOrLd")  
        else:
            equation = input_box.text()
            result = eval(equation)
            input_box.setText(str(result))
            print(equation)
    elif text == "Clear":
        input_box.clear()    
        print(text)
    elif text == "<":
        equation = input_box.text()    
        input_box.setText(equation[:-1])
        print(equation)
        print(text)
    # elif input_box.text() == "2+2=":
    #         input_box.setText("HeLlO WOrLd")             
    else:
        equation = input_box.text()
        input_box.setText(equation + text)    

# All design here
master_layout = QVBoxLayout()
        

for number in buttons:
    button = QPushButton(number)
    button.clicked.connect(button_clicked)

    grid.addWidget(button, row, col)
    col +=1
    if col >3:
        col = 0
        row += 1

clear = QPushButton("Clear")
clear.clicked.connect(button_clicked)
delete =QPushButton('<')
delete.clicked.connect(button_clicked)

row3 = QHBoxLayout()
row3.addWidget(clear, alignment=Qt.AlignCenter)
row3.addWidget(delete, alignment=Qt.AlignCenter)

master_layout.addWidget(input_box)
master_layout.addLayout(grid)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)



# show/run app
main_window.show()
app.exec_()