from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<html><body>Olá Django, aleluia, o projeto foi finalizado</body></html>', content_type='text/html')
