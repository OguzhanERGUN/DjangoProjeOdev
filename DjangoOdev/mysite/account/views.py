from django.shortcuts import render

kategorilist = ["Armutlar","Karpuzlar","Kaslılar","Gizem"]


def home(request):
    data = {
        "kategoriler" : kategorilist
    }
    return render(request, "index.html", data)


def enaccount(request):
    return render(request, "enaccount.html")
