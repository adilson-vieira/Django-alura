# from django.http import HttpResponse

# Create your views here.

# def index(request):
#    return HttpResponse('<h1>receitas</h1>')  

from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

def index(request):

    """ receitas = {
        1: 'Lasanha',
        2: 'Sopa de Legumes',
        3: 'Sorvete'
    } """

    # receitas = Receita.objects.all() # busca as receitas no BD
    # receitas = Receita.objects.filter(publicada=True) # busca as receitas no BD com filtro   
    
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True) # data mais recente no topo
    
    dados ={
        'receitas': receitas 
    }
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id) # Model, primary key
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)