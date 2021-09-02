from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to index page.
                return HttpResponseRedirect("index")
            else:
                # Return a 'disabled account' error message
                return HttpResponse("You're account is disabled.")
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'username or password not correct')
            return render(request, 'registration/login.html', context)
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request, 'registration/login.html', context)