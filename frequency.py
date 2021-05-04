import urllib.request, urllib.error
from bs4 import BeautifulSoup
from datetime import datetime as dt
import japanize_matplotlib
import matplotlib.pyplot as plt

url = "https://ncode.syosetu.com/n5378gc/"

html = urllib.request.urlopen(url=url)

soup = BeautifulSoup(html, "lxml")

title_tag = soup.title
title = title_tag.string

soup.find("span").decompose()

html_date = soup.find_all("dt", attrs={"class": "long_update"})

date = []
y = []
cnt = 0

for datum in html_date:
    t = datum.text[:17].strip()
    date.append(dt.strptime(t, "%Y/%m/%d %H:%M"))
    y.append(cnt)
    cnt = cnt + 1

fig = plt.figure()
ax = fig.add_subplot()

ax.grid(which="major", axis="x", linestyle="--")
ax.grid(which="major", axis="y", linestyle="--")
ax.plot(date, y)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=25)
plt.title(title + "の更新頻度のグラフ")
plt.xlabel("日付")
plt.ylabel("話数")
fig.subplots_adjust(left=0.13, right=0.95, bottom=0.15, top=0.9)

plt.savefig(title + "_frequency.png")
