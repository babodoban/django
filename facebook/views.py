from django.shortcuts import render
from facebook.models import Article

# Create your views here.

def play(request):
    return render(request, 'play.html')

def play2(request):
    return render(request, 'play2.html')

def profile(request):
    return render(request, 'profile.html')

count = 0
def test(request):
    sean = '김승환'
    age = 35
    global count #바깥 영역의 변수를 사용할 때 global, test 함수 밖에 count가 있다.
    count = count + 1 #접속할 때 마다 방문자 1 증가

    if age > 19:
        status = '성인'
    else:
        status = '청소년'
    
    date = ['2월 23일', '3월 2일', '3월 9일']

    return render(request, 'test.html', {'name' : sean, 'cnt' : count, 'status' : status, 'date' : date,})

def event(request):
    sean = '김승환'
    age = 35
    global count #바깥 영역의 변수를 사용할 때 global, test 함수 밖에 count가 있다.
    count = count + 1 #접속할 때 마다 방문자 1 증가

    if age > 19:
        status = '성인'
    else:
        status = '청소년'
    
    if count is 7:
        lottery = '당첨!'
    else:
        lottery = '꽝!'

    return render(request, 'event.html', {'name' : sean, 'cnt' : count, 'status' : status, 'lottery' : lottery,})

def fail(request):
    return render(request, 'fail.html')

def help(request):
    return render(request, 'help.html')

def warn(request):
    return render(request, 'warn.html')

def newsfeed(request):
    articles = Article.objects.all()

    return render(request, 'newsfeed.html', { 'articles': articles })

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'detail_feed.html', { 'feed': article})

def new_feed(request):
    return render(request, 'new_feed.html')