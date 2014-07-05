from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from components.models import Component, Category
from datetime import datetime


def components_page(request):
    context = {
        'components': Component.objects.all(),
        'time': datetime.now()
    }
    return render(request, 'components.html', context)


def component_edit_page(request, pk):
    if request.method == "POST":

        total_quantity = int(request.POST.get('total_qty'))
        purchased_quantity = int(request.POST.get('purchased_qty'))
        used_quantity = int(request.POST.get('used_qty'))
        repair_quantity = int(request.POST.get('repair_qty'))

        try:
            this_component = Component.objects.get(id=pk)
            this_component.total_quantity = total_quantity
            this_component.being_purchased = purchased_quantity
            this_component.being_used = used_quantity
            this_component.being_repaired = repair_quantity
            this_component.available_quantity = ((total_quantity + purchased_quantity) - used_quantity) - repair_quantity
            this_component.save()

        except Exception as e:
            context = {
                "form_message": { 
                    "error": "Save error",
                    "message": str(e),
                    "type": "danger"
                }
            }
            return render(request, "component_edit.html", context)

        return HttpResponseRedirect(reverse('component_list_page'))


    else:
        context = { 'component': Component.objects.get(id=pk) }
        return render(request, 'component_edit.html', context) 


def categories_page(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'categories.html', context)
