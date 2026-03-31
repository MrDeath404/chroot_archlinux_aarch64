import curses
import time

class ConsoleUI:
    def __init__(self, stdscr):
        self.buffer = stdscr
    def add_label():
        pass
    def remove_label():
        pass

def main(stdscr):
    stdscr.nodelay(True)
    stdscr.addstr(0, 0, "Status: q")
    stdscr.refresh()
    time.sleep(2)
    
    # Move to y=0, x=9 (where 'q' is) and overwrite with 's'
    stdscr.move(0, 8)
    stdscr.addch('s')
    stdscr.refresh()
    
    time.sleep(2)

if __name__ == "__main__":
    curses.wrapper(main)