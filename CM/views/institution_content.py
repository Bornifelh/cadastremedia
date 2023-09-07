from django.shortcuts import render

def in_internationale(request):
    return render(request, 'in/in_internationale.html')


def in_nationale(request):
    return render(request, 'in/in_nationale.html')