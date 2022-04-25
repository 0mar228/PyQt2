from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle('Языки программирования')
window.resize(400, 500)

text1 = QLabel('PHP')
text2 = QLabel('JavaScript')
text3 = QLabel('Python')
text4 = QLabel('Pascal')
text5 = QLabel('SQL')
text6 = QLabel('C++')

layout_main = QVBoxLayout()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(text1, alignment = Qt.AlignCenter)
layoutH1.addWidget(text2, alignment = Qt.AlignCenter)
layoutH2.addWidget(text3, alignment = Qt.AlignCenter)
layoutH2.addWidget(text4, alignment = Qt.AlignCenter)
layoutH3.addWidget(text5, alignment = Qt.AlignCenter)
layoutH3.addWidget(text6, alignment = Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
window.setLayout(layout_main)
window.setLayout(layoutH1)
window.setLayout(layoutH2)
window.setLayout(layoutH3)
window.show()
app.exec_() 