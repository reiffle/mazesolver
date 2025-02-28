from graphics import Window, Point, Line

def main():
    win=Window(800, 600)
    win.draw_line(Line(Point(100, 100), Point(200, 200)))
    win.draw_line(Line(Point(200, 200), Point(300, 100)))
    win.draw_line(Line(Point(300, 100), Point(100, 100)))
    win.wait_for_close()

main()