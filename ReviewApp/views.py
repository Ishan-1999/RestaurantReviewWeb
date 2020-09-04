from django.shortcuts import render
from .models import Review, Contact, Menu


# Create your views here.
def index(request):
    return render(request, 'index.html')


def menu(request):
    menu = Menu.objects.all()
    
    return render(request, 'menu.html', {'menu': menu})


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

        query = Contact(date=date, name=name, email=email, phone=phone,  query=query)
        query.save()

    return render(request, 'contact.html')