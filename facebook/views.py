from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Page
from facebook.models import Comment

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

    if request.method == 'POST':
        Comment.objects.create(
            article = article,
            author = request.POST['author'],
            text = request.POST['text'],
            password = request.POST['password']
        )
        return redirect(f'/feed/{article.pk}')

    return render(request, 'detail_feed.html', { 'feed': article})

def new_feed(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드 실행
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '' :
            new_article = Article.objects.create(
                author = request.POST['author'],
                title = request.POST['title'],
                text = request.POST['content'],
                password = request.POST['password']
            ) # 새 글 등록 종료 
            return redirect(f'/feed/{new_article.pk}')
    return render(request, 'new_feed.html')

def pages(request):
    pages = Page.objects.all()

    return render(request, 'pages.html', { 'pages': pages})

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']        
            article.save()
            return redirect(f'/feed/{article.pk}') # 수정사항 반영된 자세히 보기 페이지로 이동하기 
        else:
            return redirect('/fail/') # 비밀번호 오류 페이지로 이동하기 
    return render(request, 'edit_feed.html', { 'feed': article})

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/') # 첫 페이지로 이동하기 
        else:
            return redirect('/fail/') # 비밀번호 오류 페이지로 이동하기
    return render(request, 'remove_feed.html', { 'feed': article})

def new_page(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드 실행
        if request.POST['master'] != '' and request.POST['name'] != '' and request.POST['content'] != '' and request.POST['category'] != '' :
            new_page = Page.objects.create(
                master = request.POST['master'],
                name = request.POST['name'],
                text = request.POST['content'],
                category = request.POST['category']
            ) # 새 글 등록 종료 
            return redirect('/pages/')
    return render(request, 'new_page.html')

def edit_page(request, pk):
    page = Page.objects.get(pk=pk)
    if request.method == 'POST':
        page.master = request.POST['master']
        page.name = request.POST['name']
        page.text = request.POST['content']        
        page.save()
        return redirect('/pages/') # 수정사항 반영된 자세히 보기 페이지로 이동하기 
    return render(request, 'edit_page.html', { 'page': page})

def remove_page(request, pk):
    page = Page.objects.get(pk=pk)
    if request.method == 'POST':
        page.delete()
        return redirect('/pages/') # 첫 페이지로 이동하기 
    return render(request, 'remove_page.html', { 'page': page})