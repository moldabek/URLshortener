from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import ShortUrl
from .shortener import Shortener


def home(request, token):
    long_url = ShortUrl.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)


def make(request):
    form = UrlForm(request.POST)
    a = ""
    saved_urls = ShortUrl.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            new_url = form.save(commit=False)
            a = Shortener().issue_token()
            new_url.short_url = a
            new_url.save()
        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request, "index.html", {'form': form, 'a': a, 'saved_urls': saved_urls})
