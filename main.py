from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(200,200), Point(400,200)), "black")
    win.draw_line(Line(Point(400,200), Point(400,400)), "black")
    win.draw_line(Line(Point(400,400), Point(200,400)), "black")
    win.draw_line(Line(Point(200,400), Point(200,200)), "black")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()