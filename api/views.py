from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import ShortUrl
from .shortener import shortener

def Home(request, token):
    long_url = ShortUrl.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

def Make(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            newUrl = form.save(commit=False)
            a = shortener().issue_token()
            newUrl.short_url = a
            newUrl.save()
        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request,"index.html", {'form': form,'a': a})