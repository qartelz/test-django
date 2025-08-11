from django.http import HttpResponse

def test(request):
    return HttpResponse("Hello, this is the test view!")