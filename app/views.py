
from django.shortcuts import render, HttpResponse

import googlesearch

import requests
from bs4 import BeautifulSoup

# Create your views here.


def home(request):
    return render(request, 'home.html')


def result(request):

    if request.method == 'POST':
        usersearch = request.POST.get('usersearch')
                
        try:
            from googlesearch import search
        except ImportError:
            # print("No module named 'google' found")
            return HttpResponse("Server Is Currently Busy!")

        search_list = []
        title_list = []
        resultdict = {}
        resultarr = []
        title = ''
    
        for j in search(usersearch, tld="co.in", num=10, stop=10, pause=2, lang="en"):
            
            search_list.append(j)
            url = j
            reqs = requests.get(url)
            soup = BeautifulSoup(reqs.text, 'html.parser')
            
            # print("Title of the website is : ")

            for title in soup.find_all('title'):
                title_list.append(title.get_text())

            
            # temp_dict = {'link' : j, 'title' : title.get_text()}
            temp_arr = [j,title.get_text()]
            # resultdict.update(temp_dict)
            resultarr.append(temp_arr)

        # resultdict = dict(zip(title_list, search_list))
        # print(resultdict)
        print(resultarr)
    context = {
        'usersearch': usersearch,
        'title_list': title_list,
        'search_list': search_list,
        'resultdict': resultdict,
        'resultarr': resultarr,
    }

    return render(request, 'result.html', context=context)


