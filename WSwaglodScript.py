import sys 
import os
import operator
import subprocess
import shutil
import time
import threading

def parse_input():
    page = input('Please input the Weebpage to download: ')
    pwd = str(subprocess.check_output(["pwd"]).decode('UTF-8').replace('\n', ''))
    if "http://" in page:
        if not "www." in page.split("://")[1]:
            print(str(page.split("://")[1]))
            page = "http://www." + page.split("://")[1]

    if "https://" in page:
        if not "www." in page.split("://")[1]:
            print(str(page.split("://")[1]))
            page = "https://www." + page.split("://")[1]

    else:
        page = "http://www." + page
        
    url = "" + str(page.split('www.')[1])
    return str(url)

def grab_page(url):
    cwd = str(os.getcwd()) + "/" + url + "/"
    worker = threading.Thread(target=swegt, args=(str(url)), daemon=False)
    worker.start()
    while worker.isAlive:
        time.sleep(1)
    call1 = subprocess.Popen(["find", str(cwd),"-maxdepth", "2"], stdout=subprocess.PIPE)
    call2 = subprocess.Popen(["grep", "-w", "index.html"], stdin=call1.stdout, stdout=subprocess.PIPE)
    call1.stdout.close()
    found = call2.communicate()[0].decode('UTF-8').replace('\n', '')
    print(str(found))
    return str(found)

def swegt(url):
    errorcode = subprocess.check_output(["time", "wget", "--show-progress",  "--continue", "--no-clobber",  "--mirror", "--convert-links", "--adjust-extension", "--page-requisites", "--no-parent", "-nd", "-P", str(url), str(url)])
    if errorcode != 0:
        print(errorcode)
        swegt(str(url))
    else:
        time.sleep(1)
        return

def check_browser():
    browser = ['google-chrome', 'opera', 'chromium', 'firefox']
    for x in browser:
        witch = shutil.which(str(x))
        if witch != None:
            witch = x
            return str(witch)

def create_script(url, found, witch):
    name = url + '_script.sh'
    with open(name, "a+") as f:
        f.write('#!/bin/bash' + "\n" + "\n")
        f.write(str(witch) + " file://$" + found + " &")
    os.chmod(name, 0o777)
    execcute = "./" + str(name)
    os.system(execcute)
    exit(0)

def main(): 
    url = parse_input()
    found = grab_page(str(url))
    witch = check_browser()
    create_script(str(url), str(found), str(witch))
    exit(0)

main()
