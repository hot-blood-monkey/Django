from django.shortcuts import render

# Create your views here.


def index(request):
    said = "欢迎来到这个世界--用图说话"
    return render(request,'door/index.html',{'said':said})