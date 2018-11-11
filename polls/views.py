from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,man. You're at the polls index.")