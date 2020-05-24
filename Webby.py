import os
import time
from datetime import datetime
try:
    import requests
    import urllib.request
    from bs4 import BeautifulSoup
    print('All Libraries Installed.\nStarting Scraper')
except:
    print('All Libraries not installed')
    a = input('Please Install All libraries And Come Back')
    exit(0)

def scraper(url,t):
    try:
        os.remove('RAW_1')
        os.remove('RAW_2')
        print('Cleared Chached Data')
    except:
        print('Cleared Chached Data')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    file = open('RAW_1','wb')
    file.write(str(soup.findAll()).encode("utf-8"))
    file.close()
    print('Fetched')
    time.sleep(t)
    file2 = open('RAW_2','wb')
    file2.write(str(soup.findAll()).encode("utf-8"))
    file2.close()
    print('Started Comparing')
    f1 = open('RAW_1', 'rb')
    a = str(f1)
    c = a.split()
    f1.close()
    f2 = open('RAW_2','rb')
    b = str(f2)
    d = b.split()
    f2.close()
    with open("RAW_1",'rb') as f:
      lines = f.read()
    with open("RAW_2",'rb') as f:
      lines2 = f.read()
    l1 = []
    l2 = []
    for a in lines:
        c = str(a)
        words = c.strip().split()
        l1.append(words)
    for b in lines2:
        d = str(b)
        w = d.strip().split()
        l2.append(w)
    print('Compared')
    if l1!=l2:
        return yes
    os.remove('RAW_1')
    os.remove('RAW_2')
    time.sleep(1)

#main_block
url = input('Enter The URL To Scrape\n>>')
ask  = input('Do you Want To Run The Script Infinetly(y/n)\n>>')
content = 'A Change Was Detected On Given URL'

if ask == 'y' or ask == 'Y' or ask == 'Yes':
    t = int(input('Enter Time Interval B/W 2 Scraps(in sec):\n>>'))
    while True:
        if scraper(url,t)=='Yes':
            print(content)
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open("Logs.txt",'a') as log:
                log.write("A change has been detected at",url,"on",dt_string)
                log.close()
            print("A log has been created in Logs file.")
        else:
            print('No Changes Detected')
        
else:
    print("Default Time Interval Is 10 Sec")
    if scraper(url,10)=='Yes':
            print(content)
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open("Logs.txt",'a') as log:
                log.write("A change has been detected at",url,"on",dt_string)
                log.close()
            print("A log has been created in Logs file.")
            a = input('Hit Enter To Exit')
    else:
        print('No Changes Detected')
        a = input('Hit Enter To Exit')
    
