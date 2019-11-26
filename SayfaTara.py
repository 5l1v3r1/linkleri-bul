import urllib.request
from bs4 import BeautifulSoup

links = []
frames = []

#print("Taranılacak Web Sayfasının Adresini Giriniz: ")
#site=input()
site = "https://docs.docker.com/get-started/part2/"

sayfa = urllib.request.urlopen(site)
html = sayfa.read().decode('utf-8')


def link():
    if len(html) > 0:
        sayfa.close()

        gc = BeautifulSoup(html, 'html.parser')

        for i in gc.find_all("a"):
            a = i.get("href")
            links.append(a)
    else:
        print("Siteye Bağlanılamadı.")
        exit()


def frame():
    # <iframe> ya da <frame> tag'leri için arama
    if len(html) > 0:
        sayfa.close()

        gc = BeautifulSoup(html, 'html.parser')

        for i in gc.find_all("iframe"):
            a = i.get("src")
            frames.append(a)
        for j in gc.find_all("frame"):
            b = j.get("src")
            frames.append(b)
    else:
        print("Siteye Bağlanılamadı.")
        exit()


def javascript():
    # javascript içinde arama
    if len(html) > 0:
        sayfa.close()

        gc = BeautifulSoup(html, 'html.parser')

        for i in gc.find_all("script"):
            a = i.get("src")
            #print(a)

    else:
        print("Siteye Bağlanılamadı.")
        exit()


link()
frame()
#javascript()

a = open("a.txt", "w")
f = open("frame.txt", "w")

for i in frames:
    f.write(str(i) + "\n")

for j in links:
    #a.write(str(j) + "\n")
    print(str(j)+"\n")

a.close()
f.close()
