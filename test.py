import curses 
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("welcome to speed test",curses.color_pair(1))
    stdscr.addstr("\n typing test.pres anykey to begin ",curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()



def wpm_test(stdscr):
    target_text = "hello world this is test text"
    current_text = []
    
    while True:
        stdscr.clear()
        stdscr.addstr(target_text, curses.color_pair(2))      

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(3)) 
        
        stdscr.refresh()  
        
        key =stdscr.getkey()

        if ord(key) == 27:
            break


        if key in ("KEY_BACKSPACE", '\b',"\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)



def main(stdscr): 
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)
