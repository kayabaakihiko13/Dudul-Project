from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    developer="Iqbal Ramadhan A"
    univer="UPN Veteran Jatim"
    context={"univer":univer,'developer':developer}
    return render(request,'index.html',context)
    #return HttpResponse ('testing')