from django.shortcuts import render
from StoreApp.models import Departamento, Produto
from StoreApp.forms import ContatoForm
from django.core.mail import send_mail

# Create your views here.
def index(request):
    produtos_em_destaque = Produto.objects.filter(destaque = True)
    context = {
        'produtos': produtos_em_destaque
    }
    return render(request, 'index.html', context)

def produto_lista(request):

    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
        'categoria': 'Todos Produtos',
    }
    return render(request, 'produtos.html', context)

def produto_detalhe(request, id):
    produto = Produto.objects.get(id=id)
    produtos_relacionados = Produto.objects.filter(departamento_id = produto.departamento.id).exclude(id=id)[:4]
    context = {
        'produto': produto,
        'produtos_relacionados': produtos_relacionados,
    }
    return render(request, 'produto_detalhes.html', context)

def produto_lista_por_id(request, id):
    produtos = Produto.objects.filter(departamento_id = id)
    departamento = Departamento.objects.get(id = id)
    context = {
        'produtos': produtos,
        'categoria': departamento.nome,
    }
    return render(request, 'produtos.html', context)

def empresa(request):
    return render(request, 'empresa.html')

def contato(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        assunto = request.POST['assunto']
        mensagem = request.POST['mensagem']
        remetente = request.POST['remetente']
        destinatario = ['rebeca.rezende7@gmail.com']
        corpo = f'Nome: {nome} \nTelefone: {telefone} \nMensagem: {mensagem}'

        send_mail(assunto, corpo, remetente, destinatario)

    formulario = ContatoForm()
    context = {
        'form_contato': formulario
    }
    return render(request, 'contato.html', context)