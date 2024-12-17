from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account {username} was created successfully.")
            new_user = authenticate(username=form.cleaned_data.get("email"), password=form.cleaned_data.get("password1"))
            login(request, new_user)
            return redirect("core:index")
    else:
        form = UserRegisterForm()
        print("User cannot be registered.")
    
    context = {
        'form': form,
    }
    return render(request, "userauths/sign-up.html", context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except:
            print("User doesn't exist")
            messages.warning(request, f"User with {email} does not exist.")
        
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            messages.success(request, f"Loggged in.")
            return redirect("core:index")
        else:
            messages.warning(request, "User does not exist")
    return render(request, "userauths/login.html")       

def logout_view(request):
        logout(request)
        messages.warning(request, "You logged out.")
        return redirect("userauths:login")