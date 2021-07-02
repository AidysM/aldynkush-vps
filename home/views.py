from django.shortcuts import render

from news.models import New


def index(request):
    news = New.objects.filter(is_active=True)[:3]
    context = {'news': news}
    return render(request, 'home/index.html', context)


