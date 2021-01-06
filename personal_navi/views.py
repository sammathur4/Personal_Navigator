# I created this file
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Home</h1>")


def youtube(request):
    return HttpResponse('''<a href = "https://www.youtube.com/"> Youtube  </a>''')


def quora(request):
    return HttpResponse('''<a href = "https://www.quora.com/"> Quora  </a>''')


def reddit(request):
    return HttpResponse('''<a href = "https://www.reddit.com/"> Reddit  </a>''')


def facebook(request):
    return HttpResponse('''<a href = "https://www.facebook.com/"> Facebook  </a>''')
