from django.shortcuts import render
from .models import Website, Reviews

# Create your views here.
def home(request):

    websites = Website.objects.all()

    context = {
        "websites": websites
    }

    return render(request, 'index.html', context=context)

def website(request, website_uuid):
    
    website = Website.objects.get(website_id=website_uuid)
    reviews = Reviews.objects.filter(website=website)

    context = {
        "website": website,
        "reviews": reviews
    }

    return render(request, 'website_info.html', context=context)