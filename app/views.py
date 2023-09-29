from django.shortcuts import render, redirect
from .models import Titles, Idols
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  titles =  Titles.objects.all()
  idols = Idols.objects.all()
  return render(request, "home.html", context={
    "titles": titles,
    "idols": idols
  })

@login_required
def idols_add(request):
  if request.method == "POST":
    Idols.objects.create(
      name = request.POST["name"],
      games = request.POST["games"],
      position = request.POST["position"],
      age = request.POST["age"]
    )
    return redirect("home")
  return render(request, "forms_idols.html", context={"action":"Adicionar"})

@login_required
def idols_update(request, id):
  idols = Idols.objects.get(id = id)
  if request.method == "POST":
    
    idols.name = request.POST["name"]
    idols.games = request.POST["games"]
    idols.position = request.POST["position"]
    idols.age = request.POST["age"]
    idols.save()
    
    return redirect("home")

  return render(request, "forms_idols.html", context={"action":"Atualizar","idols": idols})

@login_required
def idols_delete(request, id):
  idols = Idols.objects.get(id = id)
  if request.method == "POST":
    if "confirmar" in request.POST:
      idols.delete()
      
    return redirect("home")
  return render(request, "delete_idols.html", context={"idols": idols})

@login_required
def titles_add(request):
  if request.method == "POST":
    Titles.objects.create(
      name = request.POST["name"],
      quantity = request.POST["quantity"],
      scorer = request.POST["scorer"],
      year = request.POST["year"]
    )
    return redirect("home")
  return render(request, "forms_titles.html", context={"action":"Adicionar"})

@login_required
def titles_update(request, id):
  titles = Titles.objects.get(id = id)
  if request.method == "POST": 
    
    titles.name = request.POST["name"]
    titles.quantity = request.POST["quantity"]
    titles.scorer = request.POST["scorer"]
    titles.year = request.POST["year"]
    titles.save()
    
    return redirect("home")
    
  return render(request, "forms_titles.html", context={"action":"Atualizar","titles": titles})

@login_required
def titles_delete(request, id):
  titles = Titles.objects.get(id = id)
  if request.method == "POST":
    if "confirmar" in request.POST:
      titles.delete()
      
    return redirect("home")
  return render(request, "delete_idols.html", context={"titles": titles})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"],
      request.POST["password"]
    )
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action":"Registrar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )
    login(request, user)
    if request.user.is_authenticated:
      return redirect("home")
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")