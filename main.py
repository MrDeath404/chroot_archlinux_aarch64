import curses
import time

from ConsoleUI import ConsoleUI
from ConsoleUI import Label
from ConsoleUI import Button

def main(screen):
    ui = ConsoleUI(screen)
    label = Label("ArchLinux Manager")
    label = ui.add_label(label)

    button = Button("Start")
    button = ui.add_button(button)

    while True:
        ui.render()
        time.sleep(2)

if __name__ == "__main__":
    curses.wrapper(main)