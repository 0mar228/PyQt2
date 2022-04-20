from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle('Button')
window.resize(400, 200)

button = QPushButton('Сгенерировать')

text = QLabel('Секретная надпись')
text.hide()

mainline = QVBoxLayout()
mainline.addWidget(text, alignment=Qt.AlignHCenter)
mainline.addWidget(button, alignment=Qt.AlignHCenter)  

def showtext():
    text.show()

button.clicked.connect(showtext)


window.setLayout(mainline) 
window.show()
app.exec_()
