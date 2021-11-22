from ursina import *

app = Ursina()

input_handler.bind('s', 'arrow down')  # 's'-key will now be registered as 'arrow down'-key

def test():
    print('----')
def input(key):
    print(key)
    if key == 'left mouse down':
        print('pressed left mouse button')

    if key == Keys.left_mouse_down:   # same as above, but with Keys enum.
        print('pressed left mouse button')


def update():
    for key, value in held_keys.items():
        if value != 0:
            print(key, value)

app.run()