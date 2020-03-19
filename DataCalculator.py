from datetime import datetime
from pynput import keyboard
import sys
import time
import os
file = open("Temp","r+")
file.truncate(0)
file.close()
file = open("Temp2","r+")
file.truncate(0)
file.close()
Num = 0
def Keylogger(key):
    global Num
    global firstiszero
    global firstiszero2
    global firstiszero3
    global firstis3
    global Data1
    global Data2
    global is30or31
    global firstis1
    global day
    global month
    global year
    global file
    global file2

    try:
        k = key.char
    except:
        k2 = key.name
        if k2 == 'backspace' and Num > 0 and Num != 3 and Num != 6:
            Num -= 1
            sys.stdout.write("\b")
            sys.stdout.write(" ")
            sys.stdout.write("\b")
            sys.stdout.write("")
            sys.stdout.flush()
            with open('Temp', 'rb+') as filehandle:
                filehandle.seek(-1, os.SEEK_END)
                filehandle.truncate()
        elif k2 == 'backspace' and Num == 3 or k2 == 'backspace' and Num == 6:
            Num -= 2
            sys.stdout.write("\b")
            sys.stdout.write(" ")
            sys.stdout.write("\b")
            sys.stdout.write("")
            sys.stdout.write("\b")
            sys.stdout.write(" ")
            sys.stdout.write("\b")
            sys.stdout.write("")
            sys.stdout.flush()
            with open('Temp', 'rb+') as filehandle:
                filehandle.seek(-1, os.SEEK_END)
                filehandle.truncate()
            with open('Temp', 'rb+') as filehandle:
                filehandle.seek(-1, os.SEEK_END)
                filehandle.truncate()

    try:
        filetxt = open('Temp', 'r+')
        file = str(filetxt.readline())
        days = file[:2]
        month = file[3:5]
        year = file[6:10]

        if Num == 0 and int(k) in [1, 2]:
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
            firstis3 = 'no'
            firstiszero = 'no'
        elif Num == 0 and int(k) in [3]:
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
            firstiszero = 'no'
            firstis3 = 'yes'
        elif Num == 0 and int(k) in [0]:
            print(k, end = '', flush=True)
            Num +=1
            firstiszero = 'yes'
            firstis3 = 'no'
            open("Temp","a").write(k)
        elif Num == 1 and firstiszero == 'no' and firstis3 == 'no' and int(k) in list(range(0, 10)):
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
            is30or31 = 'no'
        elif Num == 1 and firstiszero == 'no'and firstis3 == 'yes' and int(k) in [0, 1]:
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
            is30or31 = 'yes'
        elif Num == 1 and firstiszero == 'yes' and firstis3 == 'no' and int(k) in list(range(1, 10)):
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
            is30or31 = 'no'
        elif Num == 3 and int(k) in [0]:
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
            firstiszero2 = 'yes'
            firstis1 = 'no'
        elif Num == 3 and int(k) in [1]:
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
            firstiszero2 = 'no'
            firstis1 = 'yes'
        elif Num == 4 and days == '30' and month != '0' and int(k) in [1]:
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
        elif Num == 4 and days == '30' and month == '0' and int(k) in [4, 6, 9]:
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
        elif Num == 4 and int(days) < 30 and firstiszero2 == 'yes' and int(k) in list(range(1, 10)):
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
        elif Num == 4 and int(days) < 30 and firstiszero2 == 'no' and int(k) in list(range(0, 3)):
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
        elif Num == 4 and days == '31' and month == '0' and int(k) in [1, 3, 5, 7, 8]:
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
        elif Num == 4 and days == '31' and month != '0' and int(k) in [0, 2]:
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
        elif Num == 6 and int(k) in list(range(1, 10)):
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
            firstiszero3 = 'no'
        elif Num == 6 and int(k) in list(range(0, 10)):
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
            firstiszero3 = 'yes'
        elif Num == 7 and int(k) in list(range(0, 10)):
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
        elif Num == 8 and int(k) in list(range(0, 10)):
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
        elif Num == 9 and firstiszero3 == 'yes' and int(k) in list(range(1, 10)):
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)
        elif Num == 9 and firstiszero3 == 'no' and int(k) in list(range(0, 10)):
            print(k, end = '', flush=True)
            Num +=1
            open("Temp","a").write(k)

        if Num == 2 or Num == 5:
            Num +=1
            print('/', end = '', flush=True)
            open("Temp","a").write('/')
        if Num == 10:
            print(' ')
            return False
    except:
        pass

def Main():

    def UInput1():
        global Data1
        global Num
        Num = 0
        print('(gg/mm/aaaa): ', end = '', flush = True)
        listener = keyboard.Listener(on_press=Keylogger)
        listener.start()
        listener.join()
        filetxt = open("Temp", 'r')
        Data1 = str(filetxt.read())
        file2txt = open('Temp2', 'w')
        file2txt.write(str(Data1))

    def UInput2():
        global Num
        global Data2
        Num = 0
        print('(gg/mm/aaaa): ', end = '', flush = True)
        file = open("Temp","r+")
        file.truncate(0)
        file.close()
        listener = keyboard.Listener(on_press=Keylogger)
        listener.start()
        listener.join()
        filetxt = open("Temp", 'r')
        Data2 = str(filetxt.read())


    UInput1()
    UInput2()
    formato = "%d/%m/%Y"
    a = datetime.strptime(Data1, formato)
    b = datetime.strptime(Data2, formato)
    Calcolo = b - a
    print('')
    print('Sono passati esattamente ' + str(Calcolo.days) + ' giorni!')
    os.system('pause')
    print('')
Run = True
while Run:
    Main()
