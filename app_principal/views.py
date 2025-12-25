from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Para exibir mensagens de erro
from django.http import HttpResponse
from .models import Aluno, Mensagemrequired

def valida_login_adm(request):
    pass


def cria_mensagem_(request):
    pass


def lista_mensagens(request):
    pass
    

def apaga_mensagem(request, id):
    pass


def atualiza_mensagem(request, id):
    pass
