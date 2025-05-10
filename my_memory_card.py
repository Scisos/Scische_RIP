
#модули
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QRadioButton, QVBoxLayout, QHBoxLayout, QApplication, QLabel, QGroupBox, QPushButton, QButtonGroup

#созд приложения и окна
app = QApplication([])

main_wind = QWidget()
main_wind.resize(400, 200)
main_wind.setWindowTitle('Memory Card')
main_wind.show()

#сбор статистики
main_wind.stat_que = 1
main_wind.stat_ans = 0

#функции
class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

the_most_crucial_question = list()
u = Question('Какой главный вопросо смысле жизни, вселенной и вообще?', '42', '18', 'кошбки', 'лежать в теплой кроватке:))))')
g = Question('У кого самая вкусная еда?', 'у моей мамы', 'у твоей мамы', 'у французов', 'у мексиканцев')
l = Question('Кто жил у бабуси?', 'гуси', 'барашки', 'чертики', 'барабашки')
r = Question('Самое приколдесное слово на англисеке', 'seldom', 'punk', 'onion', 'doubtful')
q = Question('Гос язык бразилии', 'португальский', 'бразильский', 'испанский', 'итальянский')
the_most_crucial_question.extend([u, g, l, r, q])

def show_result():
    box_ans.setLayout(line_box)
    boxs_line.addWidget(box_ans, alignment=Qt.AlignCenter)
    box.hide()  
    box_ans.show()
    but.setText('Следующий вопрос')
    print('-Всего вопросов:', main_wind.stat_que)
    print('-Всего правильных ответов:', main_wind.stat_ans)
    print('Статистика:', main_wind.stat_ans/main_wind.stat_que*100, '%')

def show_question():
    box_ans.hide()
    box.show()
    RadioGroup.setExclusive(False)
    an1.setChecked(False)
    an2.setChecked(False)
    an3.setChecked(False)
    an4.setChecked(False)
    RadioGroup.setExclusive(True)
    but.setText('Ответить')
    
def start_text():
    if but.text() == 'Ответить':
        check_ans()
    else:
        show_question()

def ask_funk(q: Question):
    shuffle(all_asks)
    all_asks[0].setText(q.right_ans)
    all_asks[1].setText(q.wrong1)
    all_asks[2].setText(q.wrong2)
    all_asks[3].setText(q.wrong3)
    ask.setText(q.question)
    ans.setText(q.right_ans)
    show_question()

def check_ans():
    if all_asks[0].isChecked():
        lb_correct.setText('Правильно!')
        main_wind.stat_ans += 1
        show_result()
        print('-Всего вопросов:', main_wind.stat_que)
        print('-Всего правильных ответов:', main_wind.stat_ans)
        print('Статистика:', main_wind.stat_ans/main_wind.stat_que*100, '%')
    if all_asks[1].isChecked() or all_asks[2].isChecked() or all_asks[3].isChecked():
        lb_correct.setText('Неправильно!')
        show_result()

def next_question():
    main_wind.stat_que += 1
    if main_wind.cur_question == len(the_most_crucial_question):
        main_wind.cur_question = 0
        shuffle(the_most_crucial_question)
    else:
        ask_funk(the_most_crucial_question[main_wind.cur_question])
        main_wind.cur_question += 1
        
def click_ok():
    if but.text() == 'Ответить':
        check_ans()
    else:
        next_question()

#виджеты вопросы
shuffle(the_most_crucial_question)
main_wind.cur_question = 1

lb_correct = QLabel()

ask = QLabel('Какой национальности не существует?')

but = QPushButton('Ответить')

RadioGroup = QButtonGroup()

box = QGroupBox('Варианты ответов')
an1 = QRadioButton()
an2 = QRadioButton()
an3 = QRadioButton()
an4 = QRadioButton()

RadioGroup.addButton(an1)
RadioGroup.addButton(an2)
RadioGroup.addButton(an3)
RadioGroup.addButton(an4)

main_line = QVBoxLayout()
boxs_line = QHBoxLayout()
lineH = QHBoxLayout()
line1V = QVBoxLayout()
line2V = QVBoxLayout()

lineH.addStretch(2)
line1V.addStretch(2)
line2V.addStretch(2)

line1V.addWidget(an1)
line1V.setSpacing(10)
line1V.addWidget(an2)
line2V.addWidget(an3)
line2V.setSpacing(10)
line2V.addWidget(an4)
lineH.addLayout(line1V)
lineH.setSpacing(100)
lineH.addLayout(line2V)

box.setLayout(lineH)
boxs_line.addWidget(box, alignment=Qt.AlignCenter)

main_line.addWidget(ask, alignment=Qt.AlignCenter)
main_line.addLayout(boxs_line)
main_line.addWidget(but, stretch=1)

main_wind.setLayout(main_line)

box_ans = QGroupBox()
ans = QLabel('Ответ')
yesno_line = QHBoxLayout()
line_box = QVBoxLayout()
yesno_line.addWidget(lb_correct, alignment=Qt.AlignLeft)
line_box.addLayout(yesno_line)
line_box.addWidget(ans, alignment=Qt.AlignCenter)
box_ans.hide()
box_ans = QGroupBox()

#работа
all_asks = [an1, an2, an3, an4]

ask_funk(the_most_crucial_question[0])
but.clicked.connect(click_ok)



app.exec_()