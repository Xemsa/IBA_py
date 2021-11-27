#7.1
#OS
import sys
import platform

def saymyOS():
    print(platform.system(),platform.release())
    if platform.system() == "Linux":
        print('Wow, you a mamkin hacker!')

def saymyPy():
    print( (sys.version[0:6]))

def saymyprocessor():
    print(platform.processor())

def printmyinfo():
    fii = open('info.txt', 'w')
    fii.write( sys.version + ' \n')
    fii.write( platform.system() + " " + platform.release() + ' \n')
    fii.write(platform.processor() + ' \n')
    fii.close()

def readmyinfo():
    fii = open('info.txt', 'r')
    print(fii.read())
    fii.close()

while True:
    hoom = input("Чего изволите? ")
    if hoom == "os":
        saymyOS()
    elif hoom == "ver":
        saymyPy()
    elif hoom == "amd":
        saymyprocessor()
    elif hoom == "exit":
        break
    elif hoom == "print":
        printmyinfo()
    elif hoom == "file":
        readmyinfo()
    else:
        print("wat?!")
    




