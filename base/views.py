from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignupForm



def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')


# Inscription


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
import re
from .models import User  # Assure-toi que ce chemin est correct

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # Validation côté serveur
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{8,}$', password1):
            messages.error(request, "Mot de passe trop faible.")
            return render(request, "signup.html")

        if password1 != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, "signup.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nom d'utilisateur déjà pris.")
            return render(request, "signup.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email déjà utilisé.")
            return render(request, "signup.html")

        # Création de l'utilisateur
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        # Connexion automatique après inscription
        login(request, user)
        messages.success(request, "Bienvenue ! Inscription réussie.")
        return redirect("home")  # redirige vers la page d'accueil

    return render(request, "signup.html")



# Connexion
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            # Authentifier l'utilisateur
            user = form.get_user()
            login(request, user)
            messages.success(request, "Connexion réussie!")
            return redirect('home')  # Redirige vers la page d'accueil après la connexion
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Déconnexion
def logout_view(request):
    logout(request)
    messages.info(request, "Déconnexion réussie.")
    return redirect('login')


def powerbi_view(request):
    powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=a4d966bf-5278-4f87-bc6b-c6657faaeaf7&autoAuth=true&ctid=fab8a9e0-a3f5-4731-b7d2-97de14f95161"  # Remplace avec ton lien Power BI
    return render(request, "powerbi.html", {"powerbi_url":powerbi_url})

