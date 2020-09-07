from django.shortcuts import render
from .models import Review, Querie, Dishe


# Create your views here.
def index(request):
    return render(request, 'index.html')


def menu(request):
    misc = Dishe.objects.filter(category = 'Misc')
    biryani = Dishe.objects.filter(category = 'Biryani')
    veg = Dishe.objects.filter(category = 'Veg')
    curries = Dishe.objects.filter(category = 'Curries')
    fishfry = Dishe.objects.filter(category = 'Fish Fry')

    return render(request, 'menu.html', {'misc': misc, 'biryani': biryani, 'veg': veg, 'curries': curries, 'fishfry': fishfry})


def gallery(request):
    return render(request, 'gallery.html')


def write_review(request):
    if request.method == 'POST':
        date = request.POST.get('date', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        ratings = request.POST.get('ratings', '')
        review = request.POST.get('review', '')

        reviews = Review(date=date, name=name, email=email, phone=phone, ratings=ratings, review=review)
        reviews.save()

    return render(request, 'write_review.html')


def about(request):
    return render(request, 'about.html')


def reviews(request):
    reviews = Review.objects.all()
    length = len(reviews)
    print(length)
    return render(request, 'reviews.html', {'reviews': reviews, 'length': length})


def contact(request):
    if request.method == 'POST':
        date = request.POST.get('date', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')

        query = Querie(date=date, name=name, email=email, phone=phone,  query=query)
        query.save()

    return render(request, 'contact.html')