from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    moti={
        "name":"moti",
        "age": 2,
        "breed": "pug"
    }
    return render (request,'index.html',moti)
#get method for text 
    #return HttpResponse("Hel
    # lo, World!"+'<a href="http://127.0.0.1:8000/page1/">next page</a>')

def analyze(request):
    my_text = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charactercounter = request.POST.get('charcount', 'off')
    numberremover = request.POST.get('numberremover', 'off')

    analyzed = my_text
    if (
        removepunc != "on"
        and fullcaps != "on"
        and newlineremover != "on"
        and spaceremover != "on"
        and charactercounter != "on"
        and numberremover != "on"
    ):

        return HttpResponse("Please select at least one operation")
   

    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        temp = ""

        for char in analyzed:

            if char not in punctuations:

                temp = temp + char

        analyzed = temp


    if fullcaps == "on":

        analyzed = analyzed.upper()


    if newlineremover == "on":

        temp = ""

        for char in analyzed:

            if char != "\n" and char != "\r":

                temp = temp + char

        analyzed = temp


    if spaceremover == "on":

        temp = ""

        for index, char in enumerate(analyzed):

            if not(
                analyzed[index] == " "
                and index + 1 < len(analyzed)
                and analyzed[index + 1] == " "
            ):

                temp = temp + char

        analyzed = temp


    if charactercounter == "on":

        count = 0

        for char in analyzed:

            if char != " ":

                count = count + 1

        analyzed = analyzed + "\n\nCharacter Count = " + str(count)


    if numberremover == "on":

        temp = ""

        for char in analyzed:

            if char not in "0123456789":

                temp = temp + char

        analyzed = temp


    params = {

        'purpose': 'Text Analysis',
        'analyzed_text': analyzed
    }

    return render(request, 'analyze.html', params)