from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Para exibir mensagens de erro
from django.http import HttpResponse
from .models import Message

def valida_login_adm(request):
    return render(request, 'login.html')


def cria_mensagem(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem_cliente = request.POST.get('mensagem')
        mensagem = Message(nome = nome, email = email, mensagem = mensagem_cliente).save()

        mensage_sucesso = """
            <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 rounded shadow-md">
                <p class="font-bold">Sucesso!</p>
                <p>Sua mensagem foi enviada. Entraremos em contato em breve.</p>
                <a href="" class="text-sm underline mt-2 block">Enviar nova mensagem</a>
            </div>
        """
        return HttpResponse(mensage_sucesso)

    return render(request, 'formulario.html')


def lista_mensagens(request):
    mensagens = Message.objects.all()
    #  mensagens = Message.objects.all()
     
    data_mensagem = request.GET.get('data')
    texto_mensagem = request.GET.get('texto')
    status_mensagem = request.GET.get('status')
    contato_mensagem = request.GET.get('nome')
    email_mensagem = request.GET.get('email')

    if data_mensagem:
             mensagens = mensagens.filter(data_envio = data_mensagem)

    if texto_mensagem:
             mensagens = mensagens.filter(mensagem__icontains = texto_mensagem)
             
    if status_mensagem:
             if status_mensagem == 'lida':
                    mensagens = mensagens.filter(lido=True)
             elif status_mensagem == 'Não lida':
                    mensagens = mensagens.filter(lido=False)
           
    if contato_mensagem:
             mensagens = mensagens.filter(nome__icontains = contato_mensagem)

    if email_mensagem:
             mensagens = mensagens.filter(email__icontains = email_mensagem)

    return render(request, 'listagem_mensagens.html', {'mensagens':mensagens})

# def apaga_mensagem(request, id):
#     pass


# def atualiza_mensagem(request, id):
#     pass
