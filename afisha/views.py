import requests
from django.shortcuts import HttpResponse
from afisha.models import Bitcoin
from django.shortcuts import render
#from pytmdb3.tmdb3 import set_key
#set_key('your_api_key')
from tmdb3.tmdb_api import Movie
#import tmdb3

from tmdb3 import set_cache
# set_cache('null')
# set_cache(filename='/home/alex/PycharmProjects/kino/') # the 'file' engine is assumed
# set_cache(filename='tmdb3.cache')         # relative paths are put in /tmp
# set_cache(engine='file', filename='~/.tmdb3cache')

def api(request):
    r = requests.get("https://api.blockchain.info/stats")
    if r.status_code == 200:
        btc = Bitcoin()
        for i in r.json():
            print(i, r.json()[i])
            if i == "total_fees_btc":
                btc.total = r.json()[i]
            if i == "blocks_size":
                btc.blocks = r.json()[i]
        btc.save()
        return HttpResponse(r.json())
    else:
        return HttpResponse("Afisha error")


# вывод страницы стписка фильмов
def list(request):
    muvie = Movie()
    test = muvie.nowplaying()
    print(test)
    return render(request, 'index.html')
