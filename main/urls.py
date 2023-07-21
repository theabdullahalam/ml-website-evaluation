from django.urls import path
from . import views

urlpatterns = [
 
    path('', views.home, name='home'),

    path('website', views.website, name='website'),
    path('website/', views.website, name='website'),

    path('website/<uuid:website_uuid>', views.website, name='website'),
    path('website/<uuid:website_uuid>/', views.website, name='website'),

    path('create-review/', views.create_review, name='create_review'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),

]