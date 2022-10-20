from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from listings.forms import BandForm, ContactUsForm, ListingForm
from listings.models import Band, Listing
from django.shortcuts import render
from django.core.mail import send_mail

def contact(request):
    print('*'*100)
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            print('Mail envoyé avec succès')
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
        return redirect('band-list')  
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    return render(request,
          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def band_detail(request, band_id):  # notez le paramètre id supplémentaire
    band = get_object_or_404(Band, id=band_id)  # nous insérons cette ligne pour obtenir le Band avec cet id
    return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    
    return render(request,
            'listings/band_create.html',
            {'form': form})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    
    return render(request,
            'listings/listing_create.html',
            {'form': form})



def listing_list(request):
    listing_all = Listing.objects.all()

    return render(
        request,
        'listings/listing_list.html',
        context={'listings': listing_all}
    )

def listing_detail(request, listing_id):  # notez le paramètre id supplémentaire
    listing = get_object_or_404(Listing, id=listing_id)  # nous insérons cette ligne pour obtenir le Band avec cet id
    return render(request,
          'listings/listing_detail.html',
          {'listing': listing}) # nous mettons à jour cette ligne pour passer le groupe au gabarit



def bonjour(request):
    return HttpResponse("""
    <h1>Bonjour Django!</h1>
    <p> J'apprend django, les basics </p>
    <ul>
        <li>Ananas</li>
        <li> fraises </li>
    </ul>
    """)

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')