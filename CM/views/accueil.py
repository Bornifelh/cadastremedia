from django.shortcuts import render


def main_content(request):
    return render(request, 'index.html')
