from PyQt5.QtWidgets import *
import sys
import math
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Калькулятор')
        layout = QGridLayout()
        self.setLayout(layout)
        self.st = QLineEdit('')
        layout.addWidget(self.st, 0, 6)
        button = QPushButton('0')
        button.clicked.connect(lambda: self._clicked(0))
        layout.addWidget(button, 4, 1)
        button = QPushButton('1')
        button.clicked.connect(lambda: self._clicked(1))
        layout.addWidget(button, 3, 0)
        button = QPushButton('2')
        button.clicked.connect(lambda: self._clicked(2))
        layout.addWidget(button, 3, 1)
        button = QPushButton('3')
        button.clicked.connect(lambda: self._clicked(3))
        layout.addWidget(button, 3, 2)
        button = QPushButton('4')
        button.clicked.connect(lambda: self._clicked(4))
        layout.addWidget(button, 2, 0)
        button = QPushButton('5')
        button.clicked.connect(lambda: self._clicked(5))
        layout.addWidget(button, 2, 1)
        button = QPushButton('6')
        button.clicked.connect(lambda: self._clicked(6))
        layout.addWidget(button, 2, 2)
        button = QPushButton('7')
        button.clicked.connect(lambda: self._clicked(7))
        layout.addWidget(button, 1, 0)
        button = QPushButton('8')
        button.clicked.connect(lambda: self._clicked(8))
        layout.addWidget(button, 1, 1)
        button = QPushButton('9')
        button.clicked.connect(lambda: self._clicked(9))
        layout.addWidget(button, 1, 2)
        button = QPushButton(',')
        button.clicked.connect(lambda: self._clicked('.'))
        layout.addWidget(button, 4, 0)
        button = QPushButton('=')
        button.clicked.connect(lambda: self._clicked('='))
        layout.addWidget(button, 4, 2)
        button = QPushButton('+')
        button.clicked.connect(lambda: self._func('+'))
        layout.addWidget(button, 1, 3)
        button = QPushButton('-')
        button.clicked.connect(lambda: self._func('-'))
        layout.addWidget(button, 2, 3)
        button = QPushButton('/')
        button.clicked.connect(lambda: self._func('/'))
        layout.addWidget(button, 3, 3)
        button = QPushButton('*')
        button.clicked.connect(lambda: self._func('*'))
        layout.addWidget(button, 4, 3)
        button = QPushButton('//')
        button.clicked.connect(lambda: self._func('//'))
        layout.addWidget(button, 1, 4)
        button = QPushButton('%')
        button.clicked.connect(lambda: self._func('%'))
        layout.addWidget(button, 2, 4)
        button = QPushButton('^')
        button.clicked.connect(lambda: self._func('^'))
        layout.addWidget(button, 3, 4)
        button = QPushButton('log x(y)')
        button.clicked.connect(lambda: self._func('log x(y)'))
        layout.addWidget(button, 4, 4)
        button = QPushButton('Del')
        button.clicked.connect(lambda: self._clicked('Del'))
        layout.addWidget(button, 0, 0)
        button = QPushButton('<--')
        button.clicked.connect(lambda: self._clicked('<--'))
        layout.addWidget(button, 0, 1)
    def _clicked(self, n):
        if n == '=':
            if self.op == '+':
                self.st.setText(str(self.num1+float(self.st.text())))
            elif self.op == '-':
                self.st.setText(str(self.num1-float(self.st.text())))
            elif self.op == '*':
                self.st.setText(str(self.num1*float(self.st.text())))
            elif self.op == '/':
                self.st.setText(str(self.num1/float(self.st.text())))
            elif self.op == '//':
                self.st.setText(str(self.num1//float(self.st.text())))
            elif self.op == '%':
                self.st.setText(str(self.num1%float(self.st.text())))
            elif self.op == '^':
                self.st.setText(str(self.num1**float(self.st.text())))
            elif self.op == 'log x(y)':
                self.st.setText(str(math.log(self.num1, float(self.st.text()))))
        elif n == 'Del':
            self.num1 = None
            self.st.setText('')
        elif n == '<--':
            self.st.setText(self.st.text()[0:-1])
        elif n == '.':
            if len(self.st.text()) == 0:
                self.st.setText('0.')
            else:
                s =self.st.text()
                self.st.setText(s+str(n))
        else:
            s =self.st.text()
            self.st.setText(s+str(n))
    def _func(self, n):
        if n == '+':
            self.num1 = float(self.st.text())
            self.op = n
            self.st.setText('')
        elif n == '-':
            if len(self.st.text()) == 0:
                self.st.setText('-')
            else:
                self.num1 = float(self.st.text())
                self.op = n
                self.st.setText('')
        elif n == '/':
            self.num1 = float(self.st.text())
            self.op = n
            self.st.setText('')
        elif n == '*':
            self.num1 = float(self.st.text())
            self.op = n
            self.st.setText('')
        elif n == '//':
            self.num1 = float(self.st.text())
            self.op = n
            self.st.setText('')
        elif n == '%':
            self.num1 = float(self.st.text())
            self.op = n
            self.st.setText('')
        elif n == '^':
            self.num1 = float(self.st.text())
            self.op = n
            self.st.setText('')
        elif n == 'log x(y)':
            self.num1 = float(self.st.text())
            self.op = n
            self.st.setText('')
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())