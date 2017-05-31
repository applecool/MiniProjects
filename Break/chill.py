import time
import webbrowser

default_count = 0
take_a_break = 3

print("Current machine time", time.ctime());
while(default_count < take_a_break):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=3gD1woa_Cbw");
    print("Laugh!!")
    default_count = default_count + 1

