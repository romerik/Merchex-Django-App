from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

from django.shortcuts import render

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def listings_list(request):
    listing_all = Listing.objects.all()

    return render(
        request,
        'listings/listings.html',
        context={'listings': listing_all}
    )


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