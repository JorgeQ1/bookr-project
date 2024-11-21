from django.shortcuts import render

def index(request):
    name = 'Jorgeeyy'
    return render(request, "base.html", {"name": name})

def search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search.html", {"search_text": search_text})