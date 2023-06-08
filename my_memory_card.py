from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QPushButton, QLabel, QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Kako se zove najveca planina?', 'Himalaji', 'Alpi', 'Majevica', 'Jahorina'))
question_list.append(Question('Ko ce pobediti u trecem svjetskom ratu', 'Rusija', 'Ukraina', 'Belgija', 'Njemacka'))
question_list.append(Question('Kako se zove program koji sad radite?', 'Pyton', 'Mars_academy', 'Roblox', 'Cat'))
question_list.append(Question('Kako se zove Branko Kockica kad legne u krevet?', 'Lego Kockica', 'Milos', 'Maja', 'Petar'))
question_list.append(Question('Kako se zove najbolja igrica?', 'Minecraft', 'CSG', 'GTA 5', 'FIFA 2022'))
question_list.append(Question('Sta je palo sa jabuke?', 'Veljko', 'Kruska', 'Zvake', 'Voda'))
question_list.append(Question('Sta sam ja?', 'Covjek', 'Demon', 'Prase', 'Krembil'))
question_list.append(Question('Sta sve moj drug prica?', 'Ko ce ga znati', 'Sve sto postoji', 'Sve sto nepostoji', 'Sve sto je u vezi sa skolom'))
question_list.append(Question('Koliko ja imam godina?', '12', '11', '20', '2'))
question_list.append(Question('Sta kaze macka?', 'mjau mjau niga niga', 'mijauuuu', 'av av av', 'newer gona give you up'))

app = QApplication([])
my_win = QWidget()

question = QLabel('Which nationality does not exist?')
ans_button = QPushButton('Answer')
group_box = QGroupBox('Answer options')

rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Smurfs')
rbtn_3 = QRadioButton('Chulyms')
rbtn_4 = QRadioButton('Aleuts')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()

layout_2.addWidget(rbtn_1)
layout_2.addWidget(rbtn_2)
layout_3.addWidget(rbtn_3)
layout_3.addWidget(rbtn_4)

layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)

group_box.setLayout(layout_1)

AnsGroupBox = QGroupBox('Test result')
lb_Result = QLabel('True/False')
lb_Correct = QLabel('Tacan odgovor ce biti ovdje!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)

AnsGroupBox.setLayout(layout_res)

layout_line_1 = QHBoxLayout()
layout_line_2 = QHBoxLayout()
layout_line_3 = QHBoxLayout()
layout_line_4 = QVBoxLayout()

layout_line_1.addWidget(question, alignment = (Qt.AlignHCenter|Qt.AlignVCenter))
layout_line_2.addWidget(group_box)
layout_line_2.addWidget(AnsGroupBox)

AnsGroupBox.hide()

layout_line_3.addStretch(3)
layout_line_3.addWidget(ans_button, stretch = 2)
layout_line_3.addStretch(3)

layout_line_4.addLayout(layout_line_1)
layout_line_4.addLayout(layout_line_2)
layout_line_4.addLayout(layout_line_3)

def show_result():
    group_box.hide()
    AnsGroupBox.show()
    ans_button.setText('Next question')

def show_question():
    AnsGroupBox.hide()
    group_box.show()
    ans_button.setText('Answer')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q:question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Tacno')
        my_win.score += 1
        print('Statistika \n - Ukupno pitanja: ', my_win.total,'\n - Tacnih odgovora:', my_win.score)
        print('Postotak: ', (my_win.score/my_win.total)*100, '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Netacno!')
            print('Postotak: ', (my_win.score/my_win.total)*100, '%')

def next_question():
    my_win.total += 1
    print('Statistika \n - Ukupno pitanja: ', my_win.total,'\n - Tacnih odgovora:', my_win.score)
    cur_question = randint( 0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if ans_button.text() == 'Answer':
        check_answer()
    else:
        next_question()

my_win.setLayout(layout_line_4)
ans_button.clicked.connect(click_OK)
my_win.total = 0
my_win.score = 0
next_question()

my_win.show()
app.exec_()