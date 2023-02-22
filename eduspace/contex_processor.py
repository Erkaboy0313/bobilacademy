from .models import Contact

def contactRenderer(request):
    context={
        'contact':Contact.objects.all().first()
    }
    return context