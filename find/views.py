from django.shortcuts import render
from .modul import getData
# Create your views here.

def index(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            query = str(query).lower()
            data = getData(query)
        else:
            data = {
                'facebook': 'False',
                'tumblr': 'False',
                'instagram': 'False',
                'twitter': 'False',
                'steam': 'False',
                'snapchat': 'False',
                'twitch': 'False',
                'tiktok': 'False',
            }

    context = {
        'query': query,
        'data': data
    }

    return render(request, 'index.html', context)