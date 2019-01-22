from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'kurumsalysite/index.html', {'nbar' : 'index'})


def about(request):
    return render(request, 'kurumsalysite/hakkimizda.html', {'nbar' : 'about'})


def services(request):
    return render(request, 'kurumsalysite/hizmetlerimiz.html', {'nbar' : 'services'})

def process(request):
    return render(request, 'kurumsalysite/surec.html', {'nbar' : 'process'})

def faq(request):
    return render(request, 'kurumsalysite/faq.html', {'nbar' : 'faq'})

def contact(request):
    if request.method == "POST":
        adsoyad = request.POST.get('adsoyad')
        email = request.POST.get('email')
        mesaj = request.POST.get('mesaj')

        iletisim = Contact(iletisim_adsoyad=adsoyad, iletisim_ulasim=email, iletisim_mesaj=mesaj)
        iletisim.save()

        return redirect('/?gonder=ok')

    return render(request, 'kurumsalysite/iletisim.html', {'nbar' : 'contact'})