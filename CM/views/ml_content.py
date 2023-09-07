from django.shortcuts import render


def mel_internationaux(request):
    return render(request, 'ml/mel_internationaux.html')


def mel_nationaux(request):
    return render(request, 'ml/mel_nationaux.html')
