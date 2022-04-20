from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle('HELLO,WORLD!')
window.resize(400, 200)
winner = QLabel('Победитель:')

text = QLabel('Hello, world!')

mainline = QVBoxLayout()
mainline.addWidget(text, alignment=Qt.AlignHCenter) #добавляем виджет на линию в центре

window.setLayout(mainline) #устанавливаем виджет на окно
button = QPushButton('Сгенерировать')

window.show()
app.exec_()
