import feedparser
import requests
import time
def getit():
    maxid=0
    pushdict=[]
    blocklist=["chancat","SamKu","misakano","0fb6bya","nodevps","bombman","414522569","妖言惑众","UallenQbit","ywsx","master319","Hi-Hello","perfect-data","ccah","苞米地里吃过亏","别开枪我怕死-001","alekseyqin","哆啦B梦"],
    while True:
        time.sleep(5)
        NewsFeed = feedparser.parse("https://rss.nodeseek.com/")
        w=NewsFeed["entries"]
        for i in w:
            if "summary" in i:
                link=i["link"]
                summary=i["summary"]
                title=i["title"]
                id=i["id"]
                author=i["author"]
                pushdict.append([id,author,title,link,summary])
            else:
                link=i["link"]
                title=i["title"]
                id=i["id"]
                author=i["author"]
                pushdict.append([id,author,title,link])
        pushdict.sort(reverse=True)
        maxinid=int(pushdict[0][0])
        if maxinid>maxid:
            for listname in pushdict:
                idin=int(listname[0])
                if idin>maxid and listname[1] not in blocklist:
                    print(listname)
                    r = requests.post(f'https://api.telegram.org/bot6726523646:AAHxHf1H7fSgtZibWuBLJnXeargA2d5z_CI/sendMessage', json={"chat_id": 6256565801, "text": f"*[{listname[2]}]({listname[3]})*","parse_mode":"MarkdownV2"})

        else:
            continue
        maxid=maxinid
try:
    getit()
except:
    getit()