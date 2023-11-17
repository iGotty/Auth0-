from django.shortcuts import render
from .forms import ActivoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_activo import create_activo, get_activos
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

@login_required
def activo_list(request):
    role = getRole(request)
    if role == "Financiero":
        activos = get_activos()
        context = {
            'activo_list': activos
        }
        return render(request, 'Activo/activos.html', context)
    
    else:
        return HttpResponse("Unauthorized User")

@login_required
def activo_create(request):
    if request.method == 'POST':
        form = ActivoForm(request.POST)
        if form.is_valid():
            create_activo(form)
            messages.add_message(request, messages.SUCCESS, 'Activo create successful')
            return HttpResponseRedirect(reverse('activoCreate'))
        else:
            print(form.errors)
    else:
        form = ActivoForm()

    context = {
        'form': form,
    }

    return render(request, 'Activo/activoCreate.html', context)

