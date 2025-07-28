from django.shortcuts import render


def index(request):
    return render(request, 'wedding_invite.html')
