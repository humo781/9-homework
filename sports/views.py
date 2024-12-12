from django.shortcuts import render, get_object_or_404, redirect
from .models import Sport

def sports_list(request):
    sports = Sport.objects.all()
    ctx = {'sports': sports}
    return render(request, 'sports/list.html', ctx)
def sport_detail(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    ctx = {'sport': sport}
    return render(request, 'sports/detail.html', ctx)

def sport_create(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        location = request.POST.get('location')
        sport_type = request.POST.get('sport_type')
        date = request.POST.get('date')
        if event_name and location and sport_type and date:
            Sport.objects.create(
                event_name=event_name,
                location=location,
                sport_type=sport_type,
                date=date
            )
            return redirect('sports:list')
    return render(request, 'sports/form.html')

def sport_update(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        location = request.POST.get('location')
        sport_type = request.POST.get('sport_type')
        date = request.POST.get('date')
        if event_name and location and sport_type and date:
            sport.event_name = event_name
            sport.location = location
            sport.sport_type = sport_type
            sport.date = date
            sport.save()
            return redirect(sport.get_detail_url())
    ctx = {'sport': sport}
    return render(request, 'sports/form.html', ctx)

def sport_delete(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    if request.method == 'POST':
        sport.delete()
        return redirect('sports:list')
    ctx = {'sport': sport}
    return render(request, 'sports/del_confirm.html', ctx)
