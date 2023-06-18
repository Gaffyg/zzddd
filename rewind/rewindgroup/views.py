from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import *
from .forms import BuyBilet


class NewsListView(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    paginate_by = 10


class ConcertsListView(ListView):
    model = Concert
    template_name = 'concerts.html'
    context_object_name = 'concerts'
    paginate_by = 10


class AboutGroupListView(View):
    def get(self, request):
        return render(request, 'about_group.html', context={'group': Group.objects.first()})


class LinksListView(ListView):
    model = Links
    template_name = 'links.html'
    context_object_name = 'socials'


class ClipsListView(ListView):
    model = Clips
    template_name = 'clips.html'
    context_object_name = 'clips'
    paginate_by = 10


def buy_ticket(request, concert_slug):
    model_concert = Concert.objects.get(slug=concert_slug)
    if model_concert.count < 1:
        context = {
            'messege': 'К сожалению, билеты закончились...'
        }
        return render(request, 'buy.html', context=context)
    if request.method == "POST":
        form = BuyBilet(request.POST)
        if form.is_valid():
            form_count = int(request.POST['count_bilet'])
            model_count = model_concert.count
            model_concert.count = model_count - form_count
            model_concert.save()
            form.save()
            model_buyer = Buyer.objects.latest('id')
            model_buyer.city = model_concert.city
            model_buyer.place = model_concert.place
            model_buyer.price = model_concert.price
            model_buyer.save()
            return redirect('success')
    else:
        form = BuyBilet()

    context = {
        "title": "Купить билет",
        "form": form,
        "model": Concert.objects.get(slug=concert_slug),
        "slug": concert_slug
    }
    return render(request, 'buy.html', context=context)


def success_buy(request):
    context = {'title': 'Спасибо'}
    return render(request, 'success_buy.html', context=context)
