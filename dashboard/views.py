from django.shortcuts import render
from movies.models import movies
# Create your views here.


def movies_listview(request):
    
    context ={
        'movies': movies.objects.all()
    }
    return render(request, 'movies/movies.html', context)




def movies_by_genre(request, genre):
    movie_list = movies.objects.filter(genre__iexact=genre)
    return render(request, 'movies/movies.html', {
        'movies': movie_list,
        'selected_genre': genre,
    })