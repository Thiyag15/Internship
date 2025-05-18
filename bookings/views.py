from django.shortcuts import render
from theatre.models import theatre, showtimes, seats
from movies.models import movies
from accounts.models import User
from datetime import datetime, timedelta
# Create your views here.

def theatre_show_time_view(request, slug):
    today = datetime.today().date()
    start_date = today-timedelta(days=0)
    week=[]
    for i in range(7):
        day=start_date+timedelta(days=i)
        week.append({
            'name' : day.strftime('%a').upper(),
            'day' : day.day,
            'month' : day.strftime('%b').upper(),
            'date' : day

        })



    if movies.objects.filter(slug=slug).exists():
        movie = movies.objects.get(slug=slug)
        theatre_showtimes=[
            showtimes.objects.filter(movie=movie, theatre=theatre_obj).order_by('show_time')
            for theatre_obj in theatre.objects.all() if showtimes.objects.filter(movie=movie, theatre=theatre_obj).exists()]
        context = {
            'theatre_showtimes': theatre_showtimes,
            'm': movie,
            'week': week,
            'today': today,

        }
        return render(request, 'theatre/theatre_show_time.html', context)
    return render(request, 'movies/404.html' )    
