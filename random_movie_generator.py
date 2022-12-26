import requests
from bs4 import BeautifulSoup
import random

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent" : USER_AGENT}
correct = False
# inputs
while (correct == False):
    watchType = ''
    watchInput = input('Movie or TV show? ')
    genre = input('Enter genre: ')
    if (watchInput == 'movie'):
        watchType = 'feature'
        correct = True
    elif (watchInput == 'show' or watchInput == 'tv show' or watchInput == 'tv'):
        watchType = 'tv_series,mini_series'
        watchInput = 'show'
        correct = True
    else:
        print('Sorry, please enter movie or tv show')        
if (genre == 'rom-com' or genre == 'rom com'):
    genre = 'romance,comedy'
elif (genre == 'action-comedy' or genre == 'action comedy'):
    genre = 'action,comedy'
repeat = True
while repeat == True:
    # movie number in top ratings to start at
    start = random.random()*300
    start = round(start)
    numVotes=10000
    success = False
    while success == False:
        # search URL
        url = "https://www.imdb.com/search/title/?genres={0}&sort=user_rating,desc&title_type={1}&num_votes={2},&start={3}".format(genre, watchType, numVotes, start) 
        # send HTTP request
        req = requests.get(url, headers=headers, timeout=5)
        # pull HTTP data
        sor = BeautifulSoup(req.text, "html.parser")
        hits = []
        for a in sor.find_all('h3', class_='lister-item-header'):
                hits.append(a.a.string)
        if len(hits) == 0:
            numVotes = numVotes/2
        else:
            success = True
    choice = random.random()*(len(hits)-1)
    choice = round(choice)
    print(hits[choice])
    indecisive = input('Want another? ')
    if (indecisive == 'yes' or indecisive == 'y'):
        repeat = True
    else:
        repeat = False
        print('Enjoy the {} :)'.format(watchInput))