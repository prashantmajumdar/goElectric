from django.shortcuts import redirect, render
from goElectricApp.models import UserCredentials
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password

# Create your views here.

def index(request):
    current = { 'home': 'active'}
    return render(request, 'index.html', current)

def cars(request):
    current = { 'cars': 'active'}
    return render(request, 'cars.html', current)

def TataNexonEv(request):
    return render(request, 'TataNexonEv.html')    

def carsDetails(request):
    current = { 'cars': 'active'}
    return render(request, 'car-details.html', current)

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

def terms(request):
    current = { 'blog': 'active'}
    return render(request, 'terms.html')

def privacypolicy(request):
    #current = { 'blog': 'active'}
    return render(request, 'privacy-policy.html')

def about(request):
    current = { 'about': 'active'}
    return render(request, 'about-us.html')

def dashboard(request):
    current = { 'about': 'active'}
    return render(request, 'dashboard/index.html')

def form(request):
    current = { 'login': 'active'}
    return render(request, 'form.html')

def kia(request):
    return render(request, 'kia.html')

def bmwi7(request):
    return render(request, 'bmwi7.html')

def registration(request):
    if request.method == "POST":
        name = request.POST.get('RegiName')
        email = request.POST.get('RegiEmailAddres')
        password = request.POST.get('RegiPassword')
        confirmPassword = request.POST.get('RegiConfirmPassword')
        if password == confirmPassword:
            success = {'success': 'success'}
            registration = UserCredentials(first_name=name, email=email, credentail=password)
            registration.save()
            # messages.success(request, "You're finally Registered with us, Hurray!!!")
            return render(request, 'form.html', success)
    return render(request, 'form.html')

def userLogin(request):
    if request.method == "POST":
        uemail = request.POST.get('logEmail')
        upassword = request.POST.get('logPassword')
        user = authenticate(username=uemail, password=upassword)

        if user is not None:
            login(request, user)
            userDetails = {
                'uemail': uemail
            }
            return render(request, 'dashboard/index.html', userDetails)
        else:
            messages.error(request, "Bad Credentials!!!")
            return redirect('/')

    return render(request, 'form.html')

def resetPassword(request):
    if request.method == "POST":
        email = request.POST.get('RegiEmailAddres')
        password = request.POST.get('RegiPassword')
        login = UserCredentials(email=email, credentail=password)
        # login.save()
    return render(request, 'form.html')


# dashboard functions

def signup(request):
    return render(request, 'dashboard/auth/sign-up.html')

def signin(request):
    return render(request, 'dashboard/auth/sign-in.html')

def confirmmail(request):
    return render(request, 'dashboard/auth/confirm-mail.html')

def lockscreen(request):
    return render(request, 'dashboard/auth/lock-screen.html')

def recoverpw(request):
    return render(request, 'dashboard/auth/recoverpw.html')

def userprofile(request):
    return render(request, 'dashboard/app/user-profile.html')

def useradd(request):
    return render(request, 'dashboard/app/user-add.html')

def userlist(request):
    return render(request, 'dashboard/app/user-list.html')

def userprivacysetting(request):
    return render(request, 'dashboard/app/user-privacy-setting.html')

def error404(request):
    return render(request, 'dashboard/errors/error404.html')

def error500(request):
    return render(request, 'dashboard/errors/error500.html')