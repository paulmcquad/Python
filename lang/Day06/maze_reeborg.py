def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear and right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    elif front_is_clear():
        move()
    elif wall_on_right():
        move()
    else:
        turn_left()