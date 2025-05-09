from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def math(request):
    return render(request, 'math.html')
def comp(request):
    return render(request, 'comp.html')
