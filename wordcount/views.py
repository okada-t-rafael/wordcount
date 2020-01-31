from django.http import HttpResponse
from django.shortcuts import render
import operator


def home_view(request):
    return render(request, 'home.html')


def count_view(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    items = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    params = {
        'fulltext':fulltext,
        'number':len(word_list),
        'items':items
    }

    return render(request,'count.html', params)


def about_view(request):
    return render(request, 'about.html')
