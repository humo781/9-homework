from django.shortcuts import render, get_object_or_404, redirect
from .models import Music

def musics_list(request):
    musics = Music.objects.all()
    ctx = {'musics': musics}
    return render(request, 'musics/list.html', ctx)
def music_detail(request, pk):
    music = get_object_or_404(Music, pk=pk)
    ctx = {'music': music}
    return render(request, 'musics/detail.html', ctx)

def music_create(request):
    if request.method == 'POST':
        album_title = request.POST.get('album_title')
        artist = request.POST.get('artist')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release_date')
        if album_title and artist and genre and release_date:
            Music.objects.create(
                album_title=album_title,
                artist=artist,
                genre=genre,
                release_date=release_date
            )
            return redirect('musics:list')
    return render(request, 'musics/form.html')

def music_update(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'POST':
        album_title = request.POST.get('album_title')
        artist = request.POST.get('artist')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release_date')
        if album_title and artist and genre and release_date:
            music.album_title = album_title
            music.artist = artist
            music.genre = genre
            music.release_date = release_date
            music.save()
            return redirect(music.get_detail_url())
    ctx = {'music': music}
    return render(request, 'musics/form.html', ctx)

def music_delete(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'POST':
        music.delete()
        return redirect('musics:list')
    ctx = {'music': music}
    return render(request, 'musics/del_confirm.html', ctx)
