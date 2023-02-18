from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Welcome to my new website")


def course(request):
    return HttpResponse("[java ,python , php  and django]")

