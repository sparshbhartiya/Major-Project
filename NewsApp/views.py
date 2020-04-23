
from newsapi import NewsApiClient
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
import requests

import datetime as d
date = d.date.today()
# Create your views here.

from .forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
            

        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('categories')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('categories')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def categories(request):
    return render(request,'categories.html')

@login_required(login_url='login')
def home(request):
    newsapi = NewsApiClient(api_key="325e7b40140a42988aa908878a6d6c41")

    all_articles = newsapi.get_top_headlines(page=5)

    all_art = all_articles['articles']
    source_name = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []
    
    for j in range(len(all_art)):
        myarticles = all_art[j]
        if(myarticles['author']!=None):
            author.append(myarticles['author'])
        else:
            author.append('Unknown')

        y = myarticles['source']['name']
        source_name.append(y)
        title.append(myarticles['title'])
        description.append(myarticles['description'])
        urlToImage.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        content.append(myarticles['content'])
        publishedAt.append(myarticles['publishedAt'])

    list2 = zip(author,source_name,title,description,urlToImage,url,content,publishedAt)
    return render(request, 'home.html', context={'list':list2})



@login_required(login_url='login')
def Health(request):
    newsapi = NewsApiClient(api_key="325e7b40140a42988aa908878a6d6c41")

    all_articles = newsapi.get_everything(q='health',
                                      sources='bbc-news,the-verge,the-hindu,the-times-of-india',
                                      domains='bbc.co.uk,Indiatvnews.com,thehindu.com,timesofindia.indiatimes.com',
                                      language='en',
                                      sort_by='relevancy',
                                      to=date,
                                      page=1)

    all_art = all_articles['articles']
    source_name = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []
    
    for j in range(len(all_art)):
        myarticles = all_art[j]
        if(myarticles['author']!=None):
            author.append(myarticles['author'])
        else:
            author.append('Unknown')

        y = myarticles['source']['name']
        source_name.append(y)
        title.append(myarticles['title'])
        description.append(myarticles['description'])
        urlToImage.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        content.append(myarticles['content'])
        publishedAt.append(myarticles['publishedAt'])

    list2 = zip(author,source_name,title,description,urlToImage,url,content,publishedAt)
    return render(request, 'health.html', context={'list':list2})

@login_required(login_url='login')
def Sports(request):
    newsapi = NewsApiClient(api_key="325e7b40140a42988aa908878a6d6c41")

    all_articles = newsapi.get_everything(q='sports',
                                      sources='bbc-news,the-verge,the-hindu,the-times-of-india',
                                      domains='bbc.co.uk,Indiatvnews.com,thehindu.com,timesofindia.indiatimes.com',
                                      language='en',
                                      sort_by='relevancy',
                                      to=date,
                                      page=1)

    all_art = all_articles['articles']
    source_name = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []
    
    for j in range(len(all_art)):
        myarticles = all_art[j]

        if(myarticles['author']!=None):
            author.append(myarticles['author'])
        else:
            author.append('Unknown')

        y = myarticles['source']['name']
        
        source_name.append(y)
        title.append(myarticles['title'])
        description.append(myarticles['description'])
        urlToImage.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        content.append(myarticles['content'])
        publishedAt.append(myarticles['publishedAt'])

    list2 = zip(author,source_name,title,description,urlToImage,url,content,publishedAt)
    return render(request, 'sports.html', context={'list':list2})


@login_required(login_url='login')
def Entertainment(request):
    newsapi = NewsApiClient(api_key="325e7b40140a42988aa908878a6d6c41")

    all_articles = newsapi.get_everything(q='entertainment',
                                      sources='bbc-news,the-verge,the-hindu,the-times-of-india',
                                      domains='bbc.co.uk,Indiatvnews.com,thehindu.com,timesofindia.indiatimes.com',
                                      language='en',
                                      sort_by='relevancy',
                                      to=date,
                                      page=1)

    all_art = all_articles['articles']
    source_name = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []
    
    for j in range(len(all_art)):
        myarticles = all_art[j]

        if(myarticles['author']!=None):
            author.append(myarticles['author'])
        else:
            author.append('Unknown')

        y = myarticles['source']['name']
        
        source_name.append(y)
        title.append(myarticles['title'])
        description.append(myarticles['description'])
        urlToImage.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        content.append(myarticles['content'])
        publishedAt.append(myarticles['publishedAt'])

    list2 = zip(author,source_name,title,description,urlToImage,url,content,publishedAt)
    return render(request, 'entertainment.html', context={'list':list2})


@login_required(login_url='login')
def General(request):
    newsapi = NewsApiClient(api_key="325e7b40140a42988aa908878a6d6c41")

    all_articles = newsapi.get_everything(q='general',
                                      to=date,
                                      language='en',
                                      sort_by='relevancy',
                                      page=3)

    all_art = all_articles['articles']
    source_name = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []
    
    for j in range(len(all_art)):
        myarticles = all_art[j]

        if(myarticles['author']!=None):
            author.append(myarticles['author'])
        else:
            author.append('Unknown')

        y = myarticles['source']['name']
        
        source_name.append(y)
        title.append(myarticles['title'])
        description.append(myarticles['description'])
        urlToImage.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        content.append(myarticles['content'])
        publishedAt.append(myarticles['publishedAt'])

    list2 = zip(author,source_name,title,description,urlToImage,url,content,publishedAt)
    return render(request, 'general.html', context={'list':list2})


@login_required(login_url='login')
def Bussiness(request):
    newsapi = NewsApiClient(api_key="325e7b40140a42988aa908878a6d6c41")

    all_articles = newsapi.get_everything(q='business',
                                      language='en',
                                      sort_by='relevancy',
                                      to=date,
                                      page=3)

    all_art = all_articles['articles']
    source_name = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []
    
    for j in range(len(all_art)):
        myarticles = all_art[j]

        if(myarticles['author']!=None):
            author.append(myarticles['author'])
        else:
            author.append('Unknown')

        source_name.append(myarticles['source']['name'])
        title.append(myarticles['title'])
        description.append(myarticles['description'])
        urlToImage.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        content.append(myarticles['content'])
        publishedAt.append(myarticles['publishedAt'])

    list2 = zip(author,source_name,title,description,urlToImage,url,content,publishedAt)
    return render(request, 'bussiness.html', context={'list':list2})


@login_required(login_url='login')
def Technology(request):
    newsapi = NewsApiClient(api_key="325e7b40140a42988aa908878a6d6c41")

    all_articles = newsapi.get_everything(q='technology',
                                      sources='bbc-news,the-verge,the-hindu,the-times-of-india,Hitc',
                                      domains='bbc.co.uk,Hitc.com,timesofindia.indiatimes.com',
                                      language='en',
                                      sort_by='relevancy',
                                      to=date,
                                      page=1)

    all_art = all_articles['articles']
    
    source_name = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []
    
    for j in range(len(all_art)):
        myarticles = all_art[j]
        if(myarticles['author']!=None):
            author.append(myarticles['author'])
        else:
            author.append('Unknown')

        y = myarticles['source']['name']
        source_name.append(y)
        title.append(myarticles['title'])
        description.append(myarticles['description'])
        urlToImage.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        content.append(myarticles['content'])
        publishedAt.append(myarticles['publishedAt'])

    list2 = zip(author,source_name,title,description,urlToImage,url,content,publishedAt)
    return render(request, 'technology.html', context={'list':list2})


@login_required(login_url='login')
def Science(request):
    newsapi = NewsApiClient(api_key="325e7b40140a42988aa908878a6d6c41")

    all_articles = newsapi.get_everything(q='science',
                                      sources='bbc-news,the-verge,the-hindu,the-times-of-india',
                                      domains='bbc.co.uk,Indiatvnews.com,thehindu.com,Indianexpress.com,Thewire.in,timesofindia.indiatimes.com',
                                      language='en',
                                      sort_by='relevancy',
                                      to=date,
                                      page=1)

    all_art = all_articles['articles']

    source_name = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []
    
    for j in range(len(all_art)):
        myarticles = all_art[j]
        if(myarticles['author']!=None):
            author.append(myarticles['author'])
        else:
            author.append('Unknown')

        y = myarticles['source']['name']
        
        source_name.append(y)
        title.append(myarticles['title'])
        description.append(myarticles['description'])
        urlToImage.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        content.append(myarticles['content'])
        publishedAt.append(myarticles['publishedAt'])

    list2 = zip(author,source_name,title,description,urlToImage,url,content,publishedAt)
    return render(request, 'science.html', context={'list':list2})

@login_required(login_url='login')
def Search(request):
    if request.method == "POST":
        search_word = request.POST.get('search')
    url = "http://newsapi.org/v2/everything?"

    api_key = "325e7b40140a42988aa908878a6d6c41"

    parameters = {
        'q' : search_word,
        'pageSize':50,
        'apiKey':api_key,
        'sortBy':'relevancy',
         'to':date,
        'language':'en'
    }

    response = requests.get(url,params=parameters )

    response_json = response.json()


    response_json.keys()

    bitcoin_articles = response_json['articles']


    def getArticles(file):
        articles_result = []
        for i in range(len(file)):
            article_dict = {}
            article_dict['title'] = file[i]['title']
            article_dict['author'] = file[i]['author']
            article_dict['source'] = file[i]['source']
            article_dict['description'] = file[i]['description']
            article_dict['pub_date'] = file[i]['publishedAt']
            article_dict['url'] = file[i]['url']
            article_dict['pic_url'] = file[i]['urlToImage']
            articles_result.append(article_dict)
        return articles_result

    s = getArticles(bitcoin_articles)
    s[0].keys()
        

    title = []
    author = []
    source = []
    description = []
    pub_date = []
    url = []
    pic_url = []

    for i in range(len(s)):
        title.append(s[i]['title'])
        author.append(s[i]['author'])
        source.append(s[i]['source']['name'])
        description.append(s[i]['description'])
        pub_date.append(s[i]['pub_date'])
        url.append(s[i]['url'])
        pic_url.append(s[i]['pic_url'])
    l_f = list(zip(title, author, source, description,  pub_date, url, pic_url))

    return render(request,'search.html',{'list':l_f,'search':search_word})