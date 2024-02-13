from django.shortcuts import render, redirect
from web.models import Produit
from web.forms import ContactForm


def home(request):
    return render(request, 'home.html')



def show_products(request):
    produits = Produit.objects.all()  # Récupérer tous les produits
    return render(request, 'products.html', {'produits': produits})

def about(request):
    return render(request, 'about.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['message_sent'] = True
            return redirect('/success')  # Redirige vers une URL de succès après l'envoi
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success(request):
    if request.session.get('message_sent'):
        request.session['message_sent'] = False  # Réinitialiser la variable de session
        return render(request, 'success.html')
    else:
        return redirect('contact')