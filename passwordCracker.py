import random
import pyautogui

import sys
import time

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, u"█"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()


chars = "abcdefghijklmnopqrstuvwxyz0123456789"
chars_list = list(chars)

password = pyautogui.password("Password: ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("<=" + str(guess_password)+ "=>")

    if (guess_password == list(password)):
        print("")
        for i in progressbar(range(100), "Desencriptando: ", 50):
           time.sleep(0.00001)
        print("A tua password é: "+ "".join(guess_password))

        break




