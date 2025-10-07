from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Olá Django")