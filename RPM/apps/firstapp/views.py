from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Firstapp, Comment
def index(request):
    latest_list = Firstapp.objects.order_by('-pub_date')[:5]
    return render(request, 'myfirst/list.html', {'latest_list': latest_list})

def detail(request, article_id):
    try:
        a = Firstapp.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'myfirst/detail.html', {'firstapp': a, 'latest_comments_list': latest_comments_list}, )

def leave_comment(request, article_id):
    try:
        a = Firstapp.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')

    a.comment_set.create(name_author=request.POST['name'], text_comment=request.POST['text'])
    return HttpResponseRedirect(reverse('firstapp:detail', args=(a.id,)))