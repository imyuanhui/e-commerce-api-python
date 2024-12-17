from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Q
from .models import User

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
        identifier = request.POST.get("identifier")
        password = request.POST.get("password")

        user = None
        try:
            user_object = User.objects.get(Q(email=identifier) | Q(username=identifier))
            user = authenticate(request, username=user_object.email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return redirect("core:index")
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        except:
            messages.error(request, "Invalid user or password. Please try again.")
    return render(request, "userauths/login.html")    

def logout_view(request):
        logout(request)
        messages.warning(request, "You logged out.")
        return redirect("userauths:login")