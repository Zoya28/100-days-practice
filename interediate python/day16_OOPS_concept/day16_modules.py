# from turtle import Turtle, Screen
# timmy = Turtle("turtle",500)
# timmy.shape("turtle")
# timmy.color('red', 'red')
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.backward(100)
# my_screen = Screen()
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokaemon",["Alcremie","Alakazam","Aipom","Aggron","Aerodactyl","Altaria"],"l")
table.add_column("type",["water","fire","electric","wind","stone","water"])
print(table)