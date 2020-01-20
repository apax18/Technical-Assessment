import curses
import time
from curses import textpad

# u: 117, d: 100, r: 114, l: 108, e: 101, p: 112

class CommndLineApplication:
    """
    Creates a grid on command line and navigates the cursor on it. The grid can be created
    in any size and any location, by default the size is 10*10 and top left corner is at
    y=2 & x=0.
    """

    def __init__(self, square_size=10, corner_y=2, corner_x=0):
        """
        :param square_size: size of the square grid.
        :param corner_y: y value of the top left corner or the border.
        :param corner_x: x value of the top left corner or the border.
        """
        self.square_size = square_size
        self.corner_y = corner_y
        self.corner_x = corner_x


    def trackcursor(self, stdscr):
        """
        Draws a grid, with a cursor in the top left corner. Waits for the
        input from the user. Moves up with p, down with d, left with l and right
        with r. Prints the visited locations with p, and exits the program with e.
        It returns a error message if any other key is entered.
        :param stdscr: The main window.
        """

        reset = False
        y, x = self.corner_y + 1, self.corner_x + 1

        # scr_y, scr_x = stdscr.getmaxyx() # gets the terminal size

        stdscr.addstr(0, 0, 'press u, d, l, r, p OR e.')
        textpad.rectangle(stdscr, self.corner_y, self.corner_x, self.corner_y + self.square_size + 1,
                          self.corner_x + self.square_size + 1)
        stdscr.addstr(y, x, "*")

        curses.curs_set(0)
        visited_set = {(y, x)}

        while True:
            key = stdscr.getch()
            if reset is True:
                stdscr.clear()
                stdscr.addstr(0, 0, 'press u, d, l, r, p OR e.')
                textpad.rectangle(stdscr, self.corner_y, self.corner_x, self.corner_y + self.square_size + 1,
                                  self.corner_x + self.square_size + 1)
                stdscr.addstr(y, x, "*")
                reset = False

            if key in [114, 108, 117, 100]:
                stdscr.addstr(y, x, " ")

            if key == 114: # r
                if x == self.corner_x + self.square_size:
                    y, x = y + 1, self.corner_x + 1
                else:
                    x += 1
                visited_set.add((y, x))
            elif key == 108: # l
                if x == self.corner_x + 1:
                    y, x = y - 1, self.corner_x + self.square_size
                else:
                    x -= 1
                visited_set.add((y, x))
            elif key == 117: # u
                if y != self.corner_y + 1:
                    y -= 1
                    visited_set.add((y, x))
            elif key == 100: # d
                if y != self.corner_y + self.square_size:
                    y += 1
                    visited_set.add((y, x))
            elif key == 112: # p for print
                reset = True
                for loc in visited_set:
                    stdscr.addstr(loc[0], loc[1], "*")
            elif key == 101: # e for exit
                stdscr.addstr(1, 0, 'Exiting the program')
                stdscr.refresh()
                break
            else:
                reset = True
                stdscr.addstr(1, 0, 'Unknown Command')

            if y == self.corner_y:
                visited_set.remove((y, x))
                y, x = self.corner_y + 1, self.corner_x + 1

            if y == self.corner_y + self.square_size + 1:
                visited_set.remove((y, x))
                y, x = self.corner_y + self.square_size, self.corner_x + self.square_size

            stdscr.addstr(y, x, "*")
            stdscr.refresh()

        time.sleep(2)

# SQR_SIZE = 10 # 10*10 grid
# COR_Y, COR_X = 2, 0 # top left corner of the border

def main():
    # cursor_instance = CommndLineApplication(SQR_SIZE, COR_Y, COR_X)
    cursor_instance = CommndLineApplication()
    curses.wrapper(cursor_instance.trackcursor)

if __name__ == "__main__":
    main()