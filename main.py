# from turtle import Turtle, Screen
import turtle
import pandas

screen = turtle.Screen()
screen.title("Judetele Romaniei")

image = "dist//ghiceste_judetul//romania_judete.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("dist\ghiceste_judetul\judete.csv")
judet_column = data["judet"]
guessed_judete = []
score = 0

while(len(guessed_judete) < 41):

    answer_state = screen.textinput(title=f"{len(guessed_judete)}/41 - Judete Romania", prompt= "Numele unui alt judet:") 

    if answer_state is None:
        break

    correct_answer_line = data[judet_column == answer_state.title()]     
    if correct_answer_line.empty:
        break  

    for judet_din_lista in guessed_judete:
        if judet_din_lista == answer_state.title(): 
            break

    judet = turtle.Turtle()
    judet.hideturtle()
    judet.penup()
    judet.goto(int(correct_answer_line.x), int(correct_answer_line.y))
    judet.write(correct_answer_line.judet.item()) 

    score += 1
    screen.title(str(score) + "/41 - Judetele Romaniei")
    guessed_judete.append(answer_state.title())

judete_de_invatat_lista = [judet_de_invatat for judet_de_invatat in judet_column.to_list() if judet_de_invatat not in guessed_judete]


# for judet_de_invatat in judet_column.to_list():
#     if judet_de_invatat in guessed_judete:
#         pass
#     else:
#         judete_de_invatat_lista.append(judet_de_invatat)

data_to_learn = pandas.DataFrame(judete_de_invatat_lista)     
data_to_learn.to_csv("dist\ghiceste_judetul\judete_de_invatat.csv")