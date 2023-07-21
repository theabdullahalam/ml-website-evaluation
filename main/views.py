from django.shortcuts import render
from django.http import JsonResponse
from .models import Website, Reviews
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home view or URL name.
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout.

# def user_signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')  # Replace 'home' with the name of your home view or URL name.
#         else:
#             print('Invalid Form')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home view or URL name.
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})



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

@login_required
def create_review(request):
    if request.method == 'POST':

        review_content = request.POST.get('reviewContent')
        website_id = request.POST.get('website_id')

        print(website_id)

        # Create a new instance of the Review model 
        review = Reviews.objects.create(
            review=review_content,
            website = Website.objects.get(website_id=website_id),
            user = request.user # just using the default user for now
        )

        review.save()

        redirect_url = reverse('website', kwargs={'website_uuid': website_id})

        # Return a JSON response indicating success
        return redirect(redirect_url)

    # Return a JSON response indicating failure
    return JsonResponse({'status': 'error'})