from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello")


def about(request):
    return HttpResponse("About Hello")


def read_text(request):
    file = open("name.txt", "r+")
    return HttpResponse(file.read())


def hyper(request):
    return HttpResponse("Check out the wikipedia page: <a href = https://en.wikipedia.org/wiki/Main_Page> Wikipedia </a>")


def index(request):
    params = {'fname': 'Aryan', 'lname': 'Tandon'}
    return render(request, 'index.html', params)


def removepunc(request):
    print(request.GET.get('text', 'default'))
    return HttpResponse("Remove Punctuation")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Remove Punctuations', 'analyze_text': analyzed}
        djtext = analyzed
    if fullcaps == "on":
        analyzed = djtext.upper()
        params = {'purpose': 'Capitalize', 'analyze_text': analyzed}
        djtext = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Remove New Lines', 'analyze_text': analyzed}
        djtext = analyzed
    if extraspaceremover == "on":
        analyzed = ""
        for i in range(len(djtext)):
            if djtext[i] == " " and djtext[i + 1] == " ":
                pass
            else:
                analyzed += djtext[i]
        params = {'purpose': 'Remove Extra Spaces', 'analyze_text': analyzed}
        djtext = analyzed
    if extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on" and removepunc != "on":
        return HttpResponse("Please tick at least one box.")
    return render(request, 'analyze.html', params)

