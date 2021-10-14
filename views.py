from django.shortcuts import render

# Create your views here.

def sport(request):
    if request.GET:
        sport = request.GET["sport"]
        player = request.GET["player"]
        return render(request, "sport.html", {"sport": sport, "player": player})
    else:
        return render(request, "sport.html")