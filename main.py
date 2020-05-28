from ufo import *
import turtle as tr
import random


tr.tracer(0)
tr.hideturtle()
tr.bgcolor('blue')

colors = ['green', 'blue', 'pink', 'orange', 'red', 'black', 'brown', 'yellow']
lst_ufo = []
tr.showturtle()
response = tr.numinput('Ответ', 'Введите желаемое кол-во тарелок:')
if response == None:
    pass
else:
    for i in range(int(response)):
        lst_ufo.append(Ufo('Пришелец-'+str(i),random.randint(-600,600),
                           random.randint(-600, 600),random.randint(30,300),
                           colors[random.randint(0,7)],random.randint(3,10),
                           random.randint(2,8)))

while True:
    for i in range(len(lst_ufo)):
        lst_ufo[i].show()
        lst_ufo[i].move()
    tr.update()
    tr.clear()

    tr.listen()

    tr.onkey(lst_ufo.pop, 'Up')
    


tr.update()
tr.mainloop()
