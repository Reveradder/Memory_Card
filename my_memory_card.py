from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QButtonGroup, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()

question_label = QLabel('Кто?')
button = QPushButton("Ответить")
RGB = QGroupBox("Вариаты ответов:")
r_button1 = QRadioButton(" 11")
r_button2 = QRadioButton(" 22")
r_button3 = QRadioButton(" 33")
r_button4 = QRadioButton(" 44")

layout_ans1 = QVBoxLayout()

layout_ans1.addWidget(r_button1)
layout_ans1.addWidget(r_button2)
layout_ans1.addWidget(r_button3)
layout_ans1.addWidget(r_button4)
RGB.setLayout(layout_ans1)

#answers = [r_button1, r_button2, r_button3, r_button4]
#shuffle(answers)

layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

RGB_ = QGroupBox("Результат:")
result_label = QLabel("верно нет")
right_answer = QLabel("Зеленый")
layout_ans2.addWidget(result_label)
layout_ans2.addWidget(right_answer)
RGB_.setLayout(layout_ans2)
RGB_.hide()

def show_result():
    RGB.hide()
    RGB_.show()
    button.setText("Следущий вопрос")

def show_question():
    RGB.show()
    RGB_.hide()
    button.setText("Ответить")
    RadioGroup.setExclusive(False)
    r_button1.setChecked(False)
    r_button2.setChecked(False)
    r_button3.setChecked(False)
    r_button4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [r_button1, r_button2, r_button3, r_button4]

def start():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def ask(q:Question):
    question_label.setText(q.question)

    shuffle(answers)

    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    right_answer.setText(q.right_answer)
    show_question()
       
def check_answer():
    if answers[0].isChecked():
        result_label.setText("Правильно!")
    else:
        result_label.setText("Неверно!")
    show_result()

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)

RadioGroup = QButtonGroup()
RadioGroup.addButton(r_button1)
RadioGroup.addButton(r_button2)
RadioGroup.addButton(r_button3)
RadioGroup.addButton(r_button4)

main_layout=QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(RGB)
main_layout.addWidget(RGB_)
main_layout.addWidget(button)
main_win.setLayout(main_layout)
main_win.setWindowTitle('Memo Card')

button.clicked.connect(start)
main_win.setLayout(main_layout)

q = Question('Какая Windows была выпущена в 2001 году?', 'Windows XP', 'Windows 2001', 'Windows Vista', 'Windows 1')
question_list = []
question_list.append(q)
# question_list.append(Question('Какая Windows была выпущена в 2001 году?', 'Windows XP', 'Windows 2001', 'Windows Vista', 'Windows 1'))
question_list.append(Question('В каком году был основан сайт YouTube?', '2005', '2006', '2004', '2007'))
question_list.append(Question('Когда была выпущена первая версия Adobe Photoshop?', '19 февраля 1990', '25 марта 1994', '6 июля 1997', '13 января 1992'))
question_list.append(Question('Какая самая продоваемая видеоигра в истории?', 'Minecraft', 'Tetris', 'GTA V', 'Cyberpunk 2077'))

main_win.cur_question = -1

main_win.setLayout(main_layout)
main_win.show()
next_question()
app.exec_()