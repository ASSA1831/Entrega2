from django.http import Http404,  HttpResponse
from django.template import Context 
import datetime
from django.template.loader import get_template
from django.shortcuts import render

def hello(request):
    return HttpResponse("hello world")

def current_datetime(request):
    now= datetime.datetime.now()
    #t= Template("<html><body>it is now {{ currenttime }}</body></html>")
    #t= get_template('current_datetime.html')
    #html= t.render(Context({'currenttime':now}))
   
    return render(request, 'current_datetime.html',{'currenttime':now})

def hours_ahead(request, offset):
    try:
        offset=int(offset)
    except valueError:
        raise http404()
    dt= datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html= "<html><body>in %s It will be %s</body></html>" %(offset, dt)
   
    return render(request,'hours_ahead.html', {'time':dt})
