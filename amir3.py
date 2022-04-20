from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle('Испытай удачу, друг')
window.resize(400, 600)

button = QPushButton('1')
ton = QPushButton('2')
tni = QPushButton('3')
uto = QPushButton('4')
bu = QPushButton('5')

mainline = QHBoxLayout()
mainlne = QHBoxLayout()
tno = QHBoxLayout()
ne = QHBoxLayout()
l =QHBoxLayout()

window.setLayout(mainline)
window.setLayout(mainlne)
window.setLayout(tno)
window.setLayout(ne)
window.setLayout(l)

window.show()
app.exec_()