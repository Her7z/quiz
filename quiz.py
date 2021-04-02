import time
import turtle
# tela
wn = turtle.Screen()
wn.setup(1000,600)
wn.colormode(255)
wn.bgcolor(0, 0, 70)
wn.title("Cyber Quiz")

#setup da caixas
#C
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-450, -250)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.color("white")
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()

#D
turtle.penup()
turtle.goto(25, -250)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()

#A
turtle.penup()
turtle.goto(-450, -75)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()

#B
turtle.penup()
turtle.goto(25, -75)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()

#questão
turtle.penup()
turtle.goto(-450, 100)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(625)
    turtle.left(90)
    turtle.fd(150)
    turtle.left(90)
turtle.end_fill()

#score
turtle.penup()
turtle.goto(225, 100)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(225)
    turtle.left(90)
    turtle.fd(150)
    turtle.left(90)
turtle.end_fill()

#texto Questão
quest = turtle.Turtle()
quest.speed(0)
quest.hideturtle()
quest.penup()
quest.goto(-425, 150)

#texto Score
scorel = turtle.Turtle()
scorel.speed(0)
scorel.hideturtle()
scorel.penup()
scorel.goto(250, 125)

#texto Respostas
#A
A = turtle.Turtle()
A.speed(0)
A.hideturtle()
A.penup()
A.goto(-425, -50)

#B
B = turtle.Turtle()
B.speed(0)
B.hideturtle()
B.penup()
B.goto(50, -50)

#C
C = turtle.Turtle()
C.speed(0)
C.hideturtle()
C.penup()
C.goto(-425, -225)

#D
D = turtle.Turtle()
D.speed(0)
D.hideturtle()
D.penup()
D.goto(50, -225)

#Menu
quest.write("Bem-Vindo ao quiz!", font=("Verdana", 23, "bold"))
time.sleep(2)
quest.clear()

quest.write("Aperte a, b, c, d para Responder!", font=("Verdana", 23, "bold"))
time.sleep(2)
quest.clear()

quest.write("Boa sorte!", font=("Verdana", 23, "bold"))
time.sleep(2)
quest.clear()

# Numero de acertos
correctNow = 0

scorel.write("{}".format(correctNow), font=("Verdana", 45, "bold"))

# Variaveis
CurrentQ = 1

# Teclas Funcionais
def chooseAnswerA():
    global select
    select = 'A'
    evaluate()

def chooseAnswerB():
    global select
    select = 'B'
    evaluate()

def chooseAnswerC():
    global select
    select = 'C'
    evaluate()

def chooseAnswerD():
    global select
    select = 'D'
    evaluate()

def evaluate():
    global correctNow
    global CurrentQ
    if correct == select:
        quest.clear()
        quest.write("CORRETO!!!", font=("Verdana", 23, "bold"))
        time.sleep(1.2)
        score1.clear()
        correctNow += 1
        score1.write("{}".format(correctNow), font=("Verdana", 45, "bold"))
    else:
        quest.clear()
        quest.write("ERRRRRROUUU! {}".format(correct), font=("Verdana", 23, "bold"))
        time.sleep(1.2)
        quest.clear()
    CurrentQ += 1
    clearBoard()
    GetQuestionNum()

def GetQuestionNum():
    if CurrentQ == 2:
        question2()
    
def clearBoard():
    quest.clear()
    A.clear()
    B.clear()
    C.clear()
    D.clear()

def question1():
    quest.write("Qual a linguagem usada no projeto?", font=("Verdana", 23, "bold"))
    A.write("A. Python", font=("Verdana", 23, "bold"))
    B.write("B. Java", font=("Verdana", 23, "bold"))
    C.write("C. HTML", font=("Verdana", 23, "bold"))
    D.write("D. CSS", font=("Verdana", 23, "bold"))
    global correct
    correct = 'A'
        
def question2():
    quest.write("Questão 2?", font=("Verdana", 23, "bold"))
    A.write("A. Opção A", font=("Verdana", 23, "bold"))
    B.write("B. Opção B", font=("Verdana", 23, "bold"))
    C.write("C. Opção C", font=("Verdana", 23, "bold"))
    D.write("D. Opção D", font=("Verdana", 23, "bold"))
    global correct
    correct = 'A'
    
# Teclas
wn.listen()
wn.onkeypress(chooseAnswerA, "a")
wn.onkeypress(chooseAnswerB, "b")
wn.onkeypress(chooseAnswerC, "c")
wn.onkeypress(chooseAnswerD, "d")

# Iniciar o quiz
question1()
