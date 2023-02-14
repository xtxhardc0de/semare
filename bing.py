import ctypes
import itertools
import random
import requests
from multiprocessing.dummy import Pool
import re
from os import path


def repeatFilePath():
    status = int(0)
    while status == 0:
        newPath = input('[>] Enter New Path File : ')

        if path.exists(newPath):
            status += 1
            return readFile(newPath)
        else:
            print(f'[!] This File "{newPath}" Not Exists !')


def readFile(fileName):
    if path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as read:
            readList = read.readlines()
            return readList
    else:
        print(f'[!] This File "{fileName}" Not Exists !')

        return repeatFilePath()


def readDork():
    filePath = input('[>] Enter Dork File Name : ')
    result = readFile(filePath)
    return result


def readProxy():
    filePath = input('[>] Enter Proxy File Name : ')
    result = readFile(filePath)
    return result


def Bing(*args):
    dork = args[0][0].strip()
    page = args[0][1]

    if int(page) == 107:
        countUsedDork.append(0)

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    }

    try:
        response = requests.get(f'https://www.bing.com/search?q={dork}&first={page}', headers=headers,
                                proxies=choiceProxy()).content.decode()

        if "There are no results for" in response:
            pass

        else:
            links = re.findall(r'<h2><a href="(.*?)"', response)
            for item in links:
                link = item.replace('&amp;', '&')

                if '=' in link:
                    save(link)
    except:
        Bing((dork, page), )


def save(link):
    if link not in duplicate:
        duplicate.append(link)

        print("[+]  " + link)
        countURL.append(0)

        ctypes.windll.kernel32.SetConsoleTitleW(
            f"Welcome To Bing Dork Searcher V 0.1 | RUNNING | URL : {len(countURL)} | USED DORK : {len(countUsedDork)} |")

        with open('result.txt', 'a', encoding='utf-8') as Save:
            Save.write(link + "\n")


def choiceProxy():
    if method == 1:
        return {
            'http': f"socks4://{random.choice(proxyList).strip()}",
            'https': f"socks4://{random.choice(proxyList).strip()}"
        }
    elif method == 2:
        return {
            'http': f"socks5://{random.choice(proxyList).strip()}",
            'https': f"socks5://{random.choice(proxyList).strip()}"
        }
    else:
        return ""


if __name__ == '__main__':
    print("""
              ____    _               _      _   _       _               _   _ 
             / ___|  (_)  _ __       / \    | | (_)   __| |   __ _    __| | (_)
             \___ \  | | | '__|     / _ \   | | | |  / _` |  / _` |  / _` | | |
              ___) | | | | |       / ___ \  | | | | | (_| | | (_| | | (_| | | |
             |____/  |_| |_|      /_/   \_\ |_| |_|  \__,_|  \__,_|  \__,_| |_|



                                 Telegram ID : @SirAlidadi
                                                                   
""")

    ctypes.windll.kernel32.SetConsoleTitleW("Welcome To Bing Dork Searcher V 0.1 | STANDING |")

    duplicate = []
    countURL = []
    countUsedDork = []

    dorkList = readDork()
    proxyList = readProxy()

    method = int(input('[1] SOCKS4\n[2] SOCKS5\n[3] NONE\n[>] SELECT PROXY METHOD : '))
    ctypes.windll.kernel32.SetConsoleTitleW(f"Welcome To Bing Dork Searcher V 0.1 | RUNNING | URL : {len(countURL)} | USED DORK : {len(countUsedDork)} |")

    with Pool(processes=10) as threads:
        threads.map(Bing, itertools.product(dorkList, [7, 17, 27, 37, 47, 57, 67, 77, 87, 97, 107]))

    input('__________________ FINISH __________________')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Welcome To Bing Dork Searcher V 0.1 | FINISH | URL : {len(countURL)} | USED DORK : {len(countUsedDork)} |")
