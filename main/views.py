from django.shortcuts import render
from django.http import JsonResponse
from .models import Website, Reviews
from django.contrib.auth import get_user_model

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

def create_review(request):
    if request.method == 'POST':

        review_content = request.POST.get('reviewContent')
        website_id = request.POST.get('website_id')

        print(website_id)

        # Create a new instance of the Review model 
        review = Reviews.objects.create(
            review=review_content,
            website = Website.objects.get(website_id=website_id),
            user = get_user_model().objects.all().first() # just using the default user for now
        )

        review.save()

        # Return a JSON response indicating success
        return JsonResponse({'status': 'success'})

    # Return a JSON response indicating failure
    return JsonResponse({'status': 'error'})