from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html', {})


def admin_view(request):
    return render(request, 'admin.html', {})





