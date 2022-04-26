from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup

app = QApplication([])
window = QWidget()
window.setWindowTitle('Мое первое приложение')
window.resize(600, 400)

layout_main = QVBoxLayout()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()
layoutH5 = QHBoxLayout()

btn_answer1 = QRadioButton('1')
btn_answer2 = QRadioButton('2')
btn_answer3 = QRadioButton('3')
button1 = QPushButton('Проверить')
text = QLabel('')

btn_answer1.setChecked(True)

button_group = QButtonGroup()

button_group.addButton(btn_answer1, id = 1)
button_group.addButton(btn_answer2, id = 2)
button_group.addButton(btn_answer3, id = 3)

layoutH1.addWidget(btn_answer1, alignment = Qt.AlignLeft)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignLeft)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignLeft)
layoutH4.addWidget(button1, alignment = Qt.AlignCenter)
layoutH5.addWidget(text, alignment = Qt.AlignCenter)

button_group.checkedId()

layoutH5.setText("Выбрана кнопка под номером " + str(button_group.checkedId()))

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
layout_main.addLayout(layoutH4)
layout_main.addLayout(layoutH5)
window.setLayout(layout_main)
window.show()
app.exec_()