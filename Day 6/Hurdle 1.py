def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6
while number_of_hurdles > 0:
    hurdle()
    number_of_hurdles -= 1
    print(number_of_hurdles)
    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
