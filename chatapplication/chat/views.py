from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile
# Create your views here.
def index(request):
    if request.method == 'POST':
        obj = Profile()
        profile = ProfileForm(request.POST, instance=obj)
        profile.save()
    data = Profile.objects.all()
    params = {
        'form': ProfileForm(),
        'data': data,
    }
    return render(request, 'index.html', params)

def room(request):
    return render(request, 'room.html')
