#SELF MADE FILE
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'Pri','place':'Ind'}
    return render(request,'index.html',params)

#def index(request):
#   return HttpResponse("Hello")

def about(request):
    return HttpResponse("WELCOME")

def analyze(request):

    #Get the text
    djtext = request.POST.get('text','default')


    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to upper case ', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover =="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'new lines removed ', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (extraspaceremover =="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):

                analyzed = analyzed + char
        params = {'purpose': 'new lines removed ', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover !="on" and fullcaps != "on"):
        return HttpResponse('Please select the operation and try again')

    return render(request,'analyze.html',params)

