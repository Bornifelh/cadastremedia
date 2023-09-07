from django.shortcuts import render


def whatsapp_content(request):
    return render(request, 'frm/frm_whatsapp.html')


def autres_content(request):
    return render(request, 'frm/frm_autres.html')
