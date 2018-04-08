# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from forms import ValeForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect


def index(request):
    template = loader.get_template('appIntranet/login.html')
    context = None
    return HttpResponse(template.render(context, request))


def loginIntranet(request):
    username = request.POST['user']
    password = request.POST['pwd']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('vales.html')
    else:
        return redirect('../appIntranet')


def logoutIntranet(request):
    logout(request)
    return redirect('../appIntranet')


@csrf_protect
def vales(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = ValeForm(request.POST)
            if form.is_valid():
                form.save()
                template = loader.get_template('appIntranet/vales.html')
                context = None
                return HttpResponse(template.render(context, request))
        else:
            form = ValeForm

        args = {'form': form}
        template = loader.get_template('appIntranet/vales.html')
        return HttpResponse(template.render(args, request))
    else:
        return HttpResponse(content='Para utilizar esta función debe estar logueado!')

