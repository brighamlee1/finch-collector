from multiprocessing import reduction
from django.shortcuts import redirect, render
from django.views import View # <- View class to handle requests
from django.views.generic.base import TemplateView
from .models import Dog, Puppy, Litter
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["litters"] = Litter.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class Dogs(TemplateView):
    template_name = "dogs.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dogs"] = Dog.objects.all()
        return context

class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'image', 'verified_dog']
    template_name = "dog_create.html"
    success_url = "/dogs/"

class DogDetail(DetailView):
    model = Dog
    template_name = "dog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["litters"] = Litter.objects.all()
        return context

class DogUpdate(UpdateView):
    model = Dog
    fields = ['name', 'image', 'verified_dog']
    template_name = "dog_update.html"
    success_url = "/dogs/"

class DogDelete(DeleteView):
    model = Dog
    template_name = "dog_delete_confirmation.html"
    success_url = "/dogs/"

class PuppyCreate(View):
    
    def post(self, request, pk):
        name = request.POST.get('name')
        dog = Dog.objects.get(pk=pk)
        age = request.POST.get('age')
        Puppy.objects.create(name=name, dog=dog, age=age)

        return redirect('dog_detail', pk=pk)

class LitterPuppyAssoc(View):
    
    def get(self, request, pk, puppy_pk):
        assoc = request.GET.get('assoc')
        if assoc == "remove":
            Litter.objects.get(pk=pk).puppies.remove(puppy_pk)
        if assoc == "add":
            Litter.objects.get(pk=pk).puppies.add(puppy_pk)
        return redirect('home')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dogs")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)