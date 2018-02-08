from requests import Session as Browser
from bs4 import BeautifulSoup as Parser
import random
def Songs(querry):
    tab=Browser()
    url='http://tubidy.mobi/search.php?q={}&sid=83541ee{}b4bc0{}0ff5{}34fb46'.format(querry,str(random.randint(100000,999999)),str(random.randint(0,9)),str(random.randint(100,999)))
    response=tab.get(url)
    soup=Parser(response.text,'html.parser')
    songs_html=soup.findAll('div',{'class':"col-xs-12"})[1].findAll('div',{'class':"col-xs-12"})
    song_list=[]
    for song in songs_html :
        if songs_html.index(song)==2:
            print('broke the loop')
            break
        else:
            song_list.append(('http://tubidy.mobi'+song('a')[0].attrs['href'],song('a')[0]('img')[0].attrs['src']))
    return Inner(song_list)


def Inner(songs_list):
    tab=Browser()
    Inner_details=[('http://tubidy.mobi'+Parser(tab.get(song[0]).text,'html.parser').findAll('a',{'class':'title'})[4].attrs['href'],song[1])for song in songs_list]
    tab=Browser()
    final=[]
    for detail in Inner_details:
        tab=Browser()
        link=Parser(tab.get(detail[0]).text,'html.parser').find('a',{'class':'title'}).attrs['href']
        print('getting response')
        response=tab.get(link)
        print('got response')
        final.append((response.content,detail[1]))
        print('got a song')
    for song in final:
        with open('./music'+str(final.index(song)+1)+'.mp3','wb') as f:
            f.write(song)
            
