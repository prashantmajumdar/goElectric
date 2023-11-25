from django.shortcuts import render

# Create your views here.
def index(request):
    current = { 'home': 'active'}
    return render(request, 'index.html', current)

def cars(request):
    current = { 'cars': 'active'}
    return render(request, 'cars.html', current)

def carsDetails(request):
    current = { 'cars': 'active'}
    return render(request, 'cars-details.html', current)

def contact(request):
    current = { 'contact': 'active'}
    return render(request, 'contact.html', current)

def blog(request):
    current = { 'blog': 'active'}
    return render(request, 'blog.html')

def testimonial(request):
    current = { 'blog': 'active'}
    return render(request, 'testimonials.html')

def team(request):
    current = { 'blog': 'active'}
    return render(request, 'team.html')

def teams(request):
    current = { 'blog': 'active'}
    return render(request, 'teams.html')

def about(request):
    current = { 'about': 'active'}
    return render(request, 'about-us.html')