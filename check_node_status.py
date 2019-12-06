#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: alexliu

"""


import requests
import time
import threading



main_net = "https://api.trongrid.io"
shasta_net = "https://api.shasta.trongrid.io"
full_node = "/wallet/getnowblock"
solidity_node = "/walletsolidity/getnowblock"


def slack_send_message(data):
    url = "your slack  url"
    create_tran=requests.post(url,json=data)


def send_error_message(tag,block_height):
    data1 = tag + ":节点不同步啦，快来看看吧!!! block高度:" +  str(block_height)
    slack_send_message(data1)


def send_ok_message(tag):
    #pass
    print(tag + ":=======It's ok!!!=======")


def check_node_status(tag,url):
    while True:
        data1 = requests.post(url).json()["block_header"]["raw_data"]["number"]
        time.sleep(6)
        data2 = requests.post(url).json()["block_header"]["raw_data"]["number"]
        if data1 == data2:
            send_error_message(tag,data1)
            send_error_message(tag, data1)
            send_error_message(tag, data1)
            time.sleep(259200)
        else:
            send_ok_message(tag)



def main():

    # urls
    main_full_url = main_net + full_node
    main_solidity_url = main_net + solidity_node
    shasta_full_url = shasta_net + full_node
    shasta_solidity_url = shasta_net + solidity_node

    t1 = threading.Thread(target=check_node_status, name='main_full_node', args=("main_full_node", main_full_url))
    t1.start()

    t2 = threading.Thread(target=check_node_status, name='main_solidity_node', args=("main_solidity_node", main_solidity_url))
    t2.start()

    t3 = threading.Thread(target=check_node_status, name='shasta_full_node', args=("shasta_full_node", shasta_full_url))
    t3.start()

    t4 = threading.Thread(target=check_node_status, name='shasta_solidity_node', args=("shasta_solidity_node", shasta_solidity_url))
    t4.start()




if (__name__ == "__main__"):
    main()





