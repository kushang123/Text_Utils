# i have started working
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')

def analyze(request):
    djtext = (request.POST.get('text', 'default'))
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('fullcaps', 'off'))
    newlineremover = (request.POST.get('newlineremover', 'off'))
    spaceremover = (request.POST.get('spaceremover', 'off'))
    countcharacter = (request.POST.get('countcharacter', 'off'))
    print(removepunc)
    print(djtext)
    if removepunc =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)



    if(spaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed+char

        params = {'purpose': 'Extra space remover ', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

        if (newlineremover == "on"):
            analyzed = ""
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext  = analyzed
        #return render(request, 'analyze.html', params)



    if(countcharacter=="on"):
        analyzed=""
        analyzed = len(djtext)

        params = {'purpose': 'Count Character ', 'analyzed_text': analyzed}

    if(removepunc !="on" and fullcaps !="on" and newlineremover != "on" and spaceremover !="on" and countcharacter !="on"):
        return HttpResponse("Please select any operation and try again")


    return render(request, 'analyze.html', params)


