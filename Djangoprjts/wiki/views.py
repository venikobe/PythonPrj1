from django.shortcuts import render
from .models import Page

def mainPage(request):

    navObjects = Page.objects.values('id','PageUrl', 'PagePriority').filter(PagePriority__gt=0).order_by('-PagePriority')
    
    template = '3base.html'
    context = {'navObjects': navObjects,}
    return render(request, template, context)

def page(request, pk):
    contentObject = Page.objects.values().filter(PagePriority=pk).first()
    navObjects = Page.objects.values('id','PageUrl', 'PagePriority').filter(PagePriority__gt=0).order_by('-PagePriority')
    template = 'page.html'
    context = {'contentObject': contentObject,
               'navObjects': navObjects,}
    return render(request, template, context)
