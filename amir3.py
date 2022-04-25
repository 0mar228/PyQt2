from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle('Испытай удачу, друг')
window.resize(400, 500)

button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')

layout_main = QVBoxLayout()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(button1, alignment = Qt.AlignCenter)
layoutH1.addWidget(button2, alignment = Qt.AlignCenter)
layoutH2.addWidget(button3, alignment = Qt.AlignCenter)
layoutH3.addWidget(button4, alignment = Qt.AlignCenter)
layoutH3.addWidget(button5, alignment = Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
window.setLayout(layout_main)
window.setLayout(layoutH1)
window.setLayout(layoutH2)
window.setLayout(layoutH3)
window.show()
app.exec_() 