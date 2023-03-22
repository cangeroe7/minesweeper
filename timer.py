from turtle import *

from threading import Thread, Timer
import time

window = Screen()
window.tracer(0)
timer_text = Turtle()
timer_text.hideturtle()




def start_timer():
    start = time.time()
    while int(time.time() - start) < 999:
        time.sleep(1)
        timer_text.clear()
        timer_text.write(int(time.time() - start), font=("Courier", 30))
        window.update()



thread = Thread(target=start_timer)
thread.start()

mainloop()