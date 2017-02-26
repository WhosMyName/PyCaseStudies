import os
import sys
#----WIP
#Full Controller Support aka generate_contisupp
#Full Keyboard Support aka generate_keysupp
#Full Multithreading Support aka generate_multit
#Check my Contoller Script extend and ask for Cross-Embedding
#Find out how to finally klose a File!!!!! aka klose_file
#----
#fd = filedescriptor

def generate_file(name):
    name = name + '.py'
    fifo = open(name, "a+")
    return fifo

def klose_file(name):
    #close(name)
    pass

#Scriptz----------------------------------------------------------------

def generate_imports(f, array):
    pass

def generate_func(f, famnt):
    for num in range(1, famnt+1):
        f.write("def ")
        name = "function_" + str(num)
        f.write(name + ":\n" + "\t" + "pass" + "\n")
    
def generate_multit(f, tamnt, daemons):
    #Basics of MT
    
    if daemons == True:
        #Add Daemon Functionallity
        pass
    else:
        #No Daemon Stuff
        pass


#PyGames----------------------------------------------------------------

def pygameinit(f, w, h):
    f.write('import sys' + "\n" + 'import pygame' + "\n" + 'from pygame.locals import *' + "\n\n" + 'pygame.init()' + "\n")
    f.write("\n" + "size = [" + w + ", " + h + "]" + "\n")
    f.write('speed = [0,0]' + "\n" + 'color = [0,0,0]' + "\n" + 'screen = pygame.display.set_mode(size)' + "\n")
    
def generate_contisupp(f):
    f.write('Stuff')

#Main-------------------------------------------------------------------

name = input('Choose the FileName: ')
fd = generate_file(name)
typo = input(' Please choose from "script" or "pygame": ')
#Imports

#Script-Stuff
if typo == "script" or typo == "Script":
    #import Routines
    num = input('Choose the Amount of Functions: ')
    generate_func(fd, int(num))
    threading = input('Would you like to use Multithreading? [Yes] or [No]: ')
    if threading == "Yes" or threading == "yes" or threading == "YES" or threading == "1":
        #Add Multithreading Routines here, including Daemons and threaded Functions
        pass
    elif threading == "No" or threading == "no" or threading == "NO" or threading == "0":
        print('Ok, I can understand...')
    else:
        print('Your Input does not match any supported Pattern!')
    
    print('All Routines have been finished. Have fun coding!\n' + 'Exiting...')
    
#Pygema-Stuff
if typo == "pygame" or typo == "Pygame" or typo == "PyGame":
    width = input('Which initial Width would you like to configure [in px]: ')
    heigth = input('Which initial Heigth would you like to configure [in px]: ')
    pygameinit(fd, int(width), int(heigth))
    joystikz = input('Would you like to have XBox360 - Controller Support? [Yes] or [No]: ')
    if joystikz == "Yes" or joystikz == "yes" or joystikz == "YES" or joystikz == "1":
        generate_contisupp(fd)
    elif joystikz == "No" or joystikz == "no" or joystikz == "NO" or joystikz == "0":
        print('Ok, I can understand...')
    else:
        print('Your Input does not match any supported Pattern!')
    #Pygame Stuff

