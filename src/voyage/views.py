from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    context = {'name': 'Render'}
    return render(request, 'home.html', context)

    # name = 'HttpResponse'
    # html = '''<html><body>
    #                 <h1>Request {}</h1>
    #                 </body></html>
    #             '''.format(name)
    # return HttpResponse(html)
