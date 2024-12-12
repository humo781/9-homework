from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie

def home(request):
    return render(request, 'home.html')
def movies_list(request):
    movies = Movie.objects.all()
    ctx = {'movies': movies}
    return render(request, 'movies/list.html', ctx)
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    ctx = {'movie': movie}
    return render(request, 'movies/detail.html', ctx)

def movie_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        release_year = request.POST.get('release_year')
        if title and director and genre and release_year:
            Movie.objects.create(
                title=title,
                director=director,
                genre=genre,
                release_year=release_year
            )
            return redirect('movies:list')
    return render(request, 'movies/form.html')

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        release_year = request.POST.get('release_year')
        if title and director and genre and release_year:
            movie.title = title
            movie.director = director
            movie.genre = genre
            movie.release_year = release_year
            movie.save()
            return redirect(movie.get_detail_url())
    ctx = {'movie': movie}
    return render(request, 'movies/form.html', ctx)

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:list')
    ctx = {'movie': movie}
    return render(request, 'movies/del_confirm.html', ctx)
