import sqlite3
import urllib.request
import urllib.parse

import xlwt
from bs4 import BeautifulSoup
import re


def main():
    # 爬取网页
    baseUrl = "https://movie.douban.com/top250?start="
    dataList = getData(baseUrl)
    # 逐一解析数据
    # 保存数据
    savepath = "./doubantop250.xls"
    dbpath = "movie.db"
    # saveData(dataList, savepath)

    print("movie len=", len(dataList))
    saveData2DB(dataList, dbpath)


# 影片详情链接规则
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片链接规则
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
# 影片片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*?)</span>')
# 影片的相关内容<span c
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0, 10):
        url = baseUrl + str(i * 25)
        html = askUrl(url)

        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            item = str(item)
            data = []

            # 获取影片详情的超链接
            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)  # 中文名
                otitle = titles[1].replace("/", "")
                data.append(otitle)  # 外文名
            else:
                data.append(titles[0])
                data.append(' ')  # 外文名留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")  # 留空

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 替换
            data.append(bd.strip())  # 去掉空格

            dataList.append(data)
    return dataList


# 获取指定url的内容
def askUrl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('豆瓣电影top250', cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])

    for i in range(0, len(datalist)):
        print("第%d条" % i)
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + i, j, data[j])
    book.save(savepath)


def saveData2DB(dataList, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in dataList:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie250 
            (info_link,pic_link,cname,ename,score,rated,instroduction,info)
            values(%s)''' % ",".join(data)
        #print(sql)
        cur.execute(sql)

    conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    print("init db", dbpath)
    sql = '''
        create table if not exists movie250 (
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname vchar,
            ename vchar,
            score numeric,
            rated numeric,
            instroduction text,
            info text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    print("爬取完毕！")
