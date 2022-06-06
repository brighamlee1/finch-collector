from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('dogs/', views.Dogs.as_view(), name='dogs'),
    path('dogs/new/', views.DogCreate.as_view(), name='dog_create'),
    path('dogs/<int:pk>/', views.DogDetail.as_view(), name='dog_detail'),
    path('dogs/<int:pk>/update', views.DogUpdate.as_view(), name="dog_update"),
    path('dogs/<int:pk>/delete', views.DogDelete.as_view(), name="dog_delete"),
    path('artists/<int:pk>/puppies/new', views.PuppyCreate.as_view(), name="puppy_create"),
    path('litters/<int:pk>/pupppies/<int:puppy_pk>/', views.LitterPuppyAssoc.as_view(), name="litter_puppy_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]
