from django.shortcuts import render, redirect, get_object_or_404
from web.models import Produit, Cart, CartItem
from web.forms import ContactForm


def home(request):
    produits = Produit.objects.all()
    return render(request, 'home.html', {'produits': produits})



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


def categorie(request, nom_categorie):
    produits = Produit.objects.filter(categorie=nom_categorie)  # Filtrer par catégorie
    return render(request, 'categorie.html', {'produits': produits, 'nom_categorie': nom_categorie})


def recherche(request):
    query = request.GET.get('q', '')  # Obtient le terme de recherche de l'URL
    selected_categorie = request.GET.get('categorie', 'all')

    if selected_categorie != 'all':
        produits = Produit.objects.filter(categorie=selected_categorie, 
                                          nom__icontains=query)
    else:
        produits = Produit.objects.filter(nom__icontains=query)

    return render(request, 'resultats_recherche.html', {'produits': produits})

def detail_produit(request, nom_du_produit):
    produit = get_object_or_404(Produit, nom__iexact=nom_du_produit.replace('-', ' '))
    return render(request, 'produit.html', {'produit': produit})


from django.http import JsonResponse



def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    cart_data = [{"id": item.product.id, "name": item.product.nom, "quantity": item.quantity, "price": item.product.prix, "images": item.product.get_images(), "n": cart.get_number_produits()} for item in cart_items]
    return JsonResponse({"products": cart_data})





from django.views.decorators.http import require_POST


@require_POST



def add_to_cart(request, product_id):
    product = get_object_or_404(Produit, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    quantity = int(request.POST.get('quantity', 1))
    cart_item.quantity = quantity  
    cart_item.save()
    return redirect('http://127.0.0.1:8000/products/'+product.get_slug())

def incrementer_quantity(request, product_id):
    product = get_object_or_404(Produit, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return JsonResponse({"quantity": cart_item.quantity, "price":product.prix})

def decrementer_quantity(request, product_id):
    product = get_object_or_404(Produit, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity -= 1
    cart_item.save()
    return JsonResponse({"quantity": cart_item.quantity, "price":product.prix})



@require_POST
def remove_from_cart(request, product_id):
    product = get_object_or_404(Produit, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart_detail')


def ma_vue(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'produit.html', {'cart': cart})


def cart_item_count(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item_count = cart.cartitem_set.all().count()  
    return JsonResponse({"count": item_count})