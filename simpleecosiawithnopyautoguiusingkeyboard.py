import random
import webbrowser
import time
import keyboard

def create_search():
    query = ""
    for x in range(4):
        query += str(random.randint(1, 9))
    print(query)
    return query

while True:
    url = "https://www.ecosia.org/search?q={}".format(create_search())
    webbrowser.open(url, new=0)
    time.sleep(3)

    keyboard.press_and_release('ctrl+w')
