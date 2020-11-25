#!/usr/bin/env python
import requests
import hashlib
from lxml import html
from time import sleep
import datetime
# from win10toast import ToastNotifier
# from ipaddress import IPv4Address
# from pyairmore.request import AirmoreSession
# from pyairmore.services.messaging import MessagingService

def main(): 
    print("Hello")
    url = "https://ineedhemp.com/product-category/v4/"   
    bot(url)



# def sendText(message): 

#     mobileNumber ="2018358030"
#     textMessage = message
#     androidIP = IPv4Address("192.xx.xx.xx")
#     androidSession = AirmoreSession(androidIP)
#     print(androidSession.is_server_running)
#     smsService = MessagingService(androidSession)
#     smsService.send_message(mobileNumber, textMessage)


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
    #original = hash(page.text)
    treeOriginal = tree(page.content)
    while True:
        pageUpdated = requests.get(url)
        #updated = hash(pageUpdated.text)
        treeUpdated = tree(pageUpdated.content)
        diff = compareTrees(treeOriginal, treeUpdated)


        if diff:
            print("No Change")
            # toaster = ToastNotifier()
            # toaster.show_toast( "INEEDHEMP HAS BEEN UPDATED!", "go buy shit", icon_path = None, duration = 60)
            # while toaster.notification_active(): sleep(400)
        else:
            print("THIS IS NOT A DRILL GOOOOOOO")

        
        now = datetime.datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        
        
        sleep(60)



main()