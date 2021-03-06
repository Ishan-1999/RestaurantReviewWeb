from django.shortcuts import render
from .models import Review, Querie, Dishe, TodaysSpecial
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    return render(request, 'index.html')


def menu(request):
    today = TodaysSpecial.objects.all()
    misc = Dishe.objects.filter(category = 'Misc')
    biryani = Dishe.objects.filter(category = 'Biryani')
    veg = Dishe.objects.filter(category = 'Veg')
    curries = Dishe.objects.filter(category = 'Curries')
    fishfry = Dishe.objects.filter(category = 'Fish Fry')

    return render(request, 'menu.html', {'misc': misc, 'biryani': biryani, 'veg': veg, 'curries': curries, 'fishfry': fishfry,
                                         'today': today})


def gallery(request):
    return render(request, 'gallery.html')


def about(request):
    return render(request, 'about.html')


def write_review(request):

    if request.method == 'POST':
        date = request.POST.get('date', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        ratings = request.POST.get('ratings', '')
        review = request.POST.get('review', '')
        uploaded_file = request.FILES.getlist('image')
        if uploaded_file:
            for f in uploaded_file:
                if f.content_type != 'image/jpeg':
                    uploaded_file.remove(f)
            length = len(uploaded_file)
            if length == 1:
                reviews = Review(date=date, name=name, email=email, phone=phone, ratings=ratings, review=review,
                                 image1=uploaded_file[0])
                reviews.save()
            elif length == 2:
                reviews = Review(date=date, name=name, email=email, phone=phone, ratings=ratings, review=review,
                                 image1=uploaded_file[0], image2=uploaded_file[1])
                reviews.save()
            elif length == 3:
                reviews = Review(date=date, name=name, email=email, phone=phone, ratings=ratings, review=review,
                                 image1=uploaded_file[0], image2=uploaded_file[1], image3=uploaded_file[2])
                reviews.save()
        else:
            reviews = Review(date=date, name=name, email=email, phone=phone, ratings=ratings, review=review)
            reviews.save()

    return render(request, 'write_review.html')


def reviews(request):
    reviews = Review.objects.all()
    length = len(reviews)

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