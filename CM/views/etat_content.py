from django.shortcuts import render


def etat_nat_content(request):
    return render(request, 'etat/et_etat.html')