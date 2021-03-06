from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    if request.method =='POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password2']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo e-mail não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('as senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuario já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuario cadastrado com sucesso')
        print(nome + ' ' + email + ' ' + senha + ' ' + senha2)
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method =='POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if senha == "" or email == "":
            print('Senha e e-mail devem ser informados') 
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat = True).get() 
            user = auth.authenticate(request, username=nome, password=senha)
        if user is not None :
            auth.login(request, user)
            print ('Login realizado com sucesso')
            return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return render('index.html')
