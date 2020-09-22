from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        mailadress2 = request.POST['mailadress']
        password2 =  request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, mailadress2, password2)
            return redirect('login')
    return render(request, 'signup.html')


def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        mailadress2 = request.POST['mailadress']
        password2 =  request.POST['password']
        user = authenticate(request, username=username2, mailadress=mailadress2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'loginerror':'ログイン情報が間違っています'})
    return render(request, 'login.html')

def logoutfunc(request):
    logout(request)
    return redirect('login')

def index(request):
    try:
        profile = request.user.userprofile
    except:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        form.save()
    data = Profile.objects.all()
    params = {
        'form': ProfileForm(),
        'data': data,
    }
    return render(request, 'index.html', params)

def room(request, pk):
    # if request.method == 'POST':
    #     obj = Room()
    #     room = RoomForm(request.POST, instance=obj)
    #     room.save()
    object = Profile.objects.get(pk=pk)
    return render(request, 'room.html', {'object':object})
