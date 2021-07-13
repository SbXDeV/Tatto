from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
import telebot
# Create your views here.
from index.forms import NameForm
from index.models import WriteToMaster


def post_new(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            bot = telebot.TeleBot("1813985630:AAEzvK-NU2bc_wHul4T8s-a7wY4vlbzfouo")
            post = form.save(commit=False)
            bot.send_message(chat_id=-1001266158611, text=post)
            post.save()
    else:
        form = NameForm()
    return render(request, 'index/index.html', {'form': form})


class Catalog(TemplateView):
    template_name = "index/catalog.html"


class About(TemplateView):
    template_name = "index/index.html"


class Privocy(TemplateView):
    template_name = "index/privacy.html"


class Contact(TemplateView):
    template_name = "index/index.html"
