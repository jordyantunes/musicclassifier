import requests, re
from bs4 import BeautifulSoup

main_url = 'https://www.vagalume.com.br/'
tracks_number = 5
def get_data():
    bands = [
        #rock bands
        ('suricato', 0),
        ('sabonetes', 0),
        ('capital-inicial', 0),
        ('skank', 0),
        ('super-combo', 0),
        #funk
        ('anitta', 1),
        ('mc-livinho',1),
        ('ludmilla',1),
        ('mc-kevinho',1),
        ('mc-daleste',1),
        #sertanojo
        ('jorge-e-mateus',2),
        ('marilia-mendonca',2),
        ('henrique-e-juliano',2),
        ('matheus-e-kauan',2),
        ('ze-neto-e-cristiano',2)
    ]
    pattern = r'(<[\ a-zA-Z/=\'"]*>)|([\r\n\t?!])'
    lyrics = []

    for band, label in bands:
        print(main_url + band)
        # get the tracks of the band
        page = requests.get(main_url + band)
        soup = BeautifulSoup(page.content, 'html.parser')

        # get the track names
        tracks = [ music.next for music in soup.findAll('span', attrs={'itemprop':'name'})[tracks_number:]]
        # get the lyrics of those tracks
        for track in tracks:
            page = requests.get(main_url + band + '/' + track.replace(' ','-'))
            soup = BeautifulSoup(page.content, 'html.parser')
            lyric = soup.find('div', {'itemprop': 'description'})
            if lyric is not None:
                lyrics.append((re.sub(pattern, ' ', str(lyric)), label))  

    return lyrics