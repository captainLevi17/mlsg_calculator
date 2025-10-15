#import modules
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        #App Setting
        self.setWindowTitle("MLSG Calculator")
        self.resize(250, 300)
        self.setStyleSheet("QWidget {background-color: lightblue;}")
        #Objects
        self.textbox = QLineEdit()
        #self.textbox.setFont(QFont("Times New Roman", 30))
        self.textbox.setStyleSheet("QLineEdit {font-size: 30px;}")
        self.grid = QGridLayout()

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        self.clear_button = QPushButton('C')
        self.cut_button = QPushButton('DEL')
        self.clear_button.setStyleSheet("QPushButton {font: 24px Times; padding: 7px}")
        self.cut_button.setStyleSheet("QPushButton {font: 24px Times; padding: 7px}")

        master_layout = QVBoxLayout()
        master_layout.addWidget(self.textbox)
        master_layout.addLayout(self.grid)
        button_row = QHBoxLayout()
        button_row.addWidget(self.clear_button)
        button_row.addWidget(self.cut_button)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25,25,25,25)
        self.clear_button.clicked.connect(self.button_clicked)
        self.cut_button.clicked.connect(self.button_clicked)


        rows = 0
        cols = 0
        for button in self.buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.button_clicked)
            btn.setStyleSheet("QPushButton {font: 24px Times; padding: 7px}")
            self.grid.addWidget(btn, rows, cols)
            cols += 1
            if cols > 3:
                cols = 0
                rows += 1
        self.setLayout(master_layout)

    # Functionality
    def button_clicked(self):
        button = app.sender()
        text = button.text()
        if text == '=':
            try:
                result = str(eval(self.textbox.text()))
                self.textbox.setText(result)
            except Exception:
                self.textbox.setText("Error")
        elif text == 'C':
            self.textbox.clear()
        elif text == 'DEL':
            current_text = self.textbox.text()
            self.textbox.setText(current_text[:-1])
        else:
            current_text = self.textbox.text()
            self.textbox.setText(current_text + text)

    #Design
    
#Show/Run
if __name__ == "__main__":
    app = QApplication([])
    main_window = Calculator()
    main_window.show()
    app.exec_()