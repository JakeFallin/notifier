#!/usr/bin/env python
import requests
import hashlib
from lxml import html
from time import sleep
import datetime
from ifttt_webhook import IftttWebhook

import secretkey

def main(): 
    print("Hello")
    url = secretkey.url   
    bot(url)

def ifttt(val): 
    IFTTT_KEY = secretkey.IFTTT_KEY
    ifttt = IftttWebhook(IFTTT_KEY)
    ifttt.notification(title='tacobellisawayoflife420notification', message=val)

def hash(text):

    myHash = hashlib.sha256()
    myHash.update(text.encode('utf-8'))
    myHash.hexdigest()
    return myHash

def tree(contents):
    return html.fromstring(contents)

def compareTrees(tree1, tree2):
    oos1 = '//*[@id="main"]/div/div/div/div[3]/div[8]/div/div[2]/div[1]/div[5]/text()'
    oos2 = '//*[@id="main"]/div/div/div/div[3]/div[9]/div/div[2]/div[1]/div[5]/text()'
    oos3 = '//*[@id="wrapper"]/div/div/div[2]/p/text()'
    tree1Data1 = tree1.xpath(oos1)
    tree1Data2 = tree1.xpath(oos2)
    tree1Data3 = tree1.xpath(oos3)
    tree2Data1 = tree2.xpath(oos1)
    tree2Data2 = tree2.xpath(oos2)
    tree2Data3 = tree2.xpath(oos3)
    if tree1Data1 == tree2Data1 and tree1Data2 == tree2Data2 and tree1Data3 == tree2Data3:
        return True
    else:
        return False

def bot(url):

    page = requests.get(url)
    treeOriginal = tree(page.content)
    count = 0
    while True:
        pageUpdated = requests.get(url)
        treeUpdated = tree(pageUpdated.content)
        diff = compareTrees(treeOriginal, treeUpdated)

        if diff:
            print("No Change")
        else:
            print("THIS IS NOT A DRILL GOOOOOOO")
            ifttt("time to buy!!!!!!!!")

        now = datetime.datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        if count <= 20 :
            count = count + 1
        else :
            count = 0
            ifttt("healthy, there has been no change in the last hour")

        sleep(300)


main()