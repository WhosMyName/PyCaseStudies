"""Script to download and archive entire Webpages"""
import os
import subprocess
import shutil
import time
import threading

def parse_input():
    """Function to parse URL"""
    page = input('Please input the Weebpage to download: ')
    if "http://" in page:
        if not "www." in page.split("://")[1]:
            print(str(page.split("://")[1]))
            page = "http://www." + page.split("://")[1]
    elif "https://" in page:
        if not "www." in page.split("://")[1]:
            print(str(page.split("://")[1]))
            page = "https://www." + page.split("://")[1]
    else:
        page = "http://www." + page

    return str(page)

def grab_page(url):
    """function to prepare Download and get first index.html"""
    cwd = str(os.getcwd()) + "/" + url + "/"
    worker = threading.Thread(target=swegt, args=(str(url), ), daemon=False)
    worker.start()
    while worker.isAlive:
        time.sleep(1)
    found = False
    depth_level = 0
    while not found:
        depth_level = depth_level + 1
        call1 = subprocess.Popen(["find", str(cwd), "-maxdepth", depth_level], stdout=subprocess.PIPE)
        call2 = subprocess.Popen(["grep", "-w", "index.html"], stdin=call1.stdout, stdout=subprocess.PIPE)
        call1.stdout.close()
        index = call2.communicate()[0].decode('UTF-8').replace('\n', '')
        if index != "":
            found = True
    print(str(index))
    return str(index)

def swegt(url):
    """Function to download Webpage"""
    errorcode = subprocess.Popen(["wget", "--show-progress", "--continue", "--mirror", "--convert-links", "--adjust-extension", "--page-requisites", "--no-parent", "-nd", "-P", str(url), str(url)]).communicate()
    if errorcode != "0":
        print(errorcode)
        swegt(str(url))
    else:
        time.sleep(1)
        return

def check_browser():
    """Searches for common Browsers"""
    browserlist = ['google-chrome', 'opera', 'chromium', 'firefox']
    for browser in browserlist:
        witch = shutil.which(str(browser))
        if witch != "":
            witch = browser
            return str(witch)

def create_script(url, index, witch):
    """function to create execution Script"""
    name = url + '_script.sh'
    with open(name, "w") as filedescriptor:
        filedescriptor.write("#!/bin/bash\n\n")
        filedescriptor.write(str(witch) + " file://$" + index + " &")
    os.chmod(name, 0o777)
    exit(0)

def main():
    """Main"""
    url = parse_input()
    index = grab_page(str(url))
    witch = check_browser()
    create_script(str(url), str(index), str(witch))
    exit(0)

main()
