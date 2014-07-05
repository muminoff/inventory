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


def component_add_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        total_quantity = request.POST.get('total_qty')
        purchased_quantity = request.POST.get('purchased_qty')
        used_quantity = request.POST.get('used_qty')
        repair_quantity = request.POST.get('repair_qty')
        notes = request.POST.get('notes')

        if total_quantity:
            total_quantity = int(total_quantity)
        if purchased_quantity:
            purchased_quantity = int(purchased_quantity)
        if used_quantity:
            used_quantity = int(used_quantity)
        if repair_quantity:
            repair_quantity = int(repair_quantity)

        try:
            this_component = Component()
            this_component.name = name
            this_component.category = Category.objects.get(id=category_id)
            this_component.total_quantity = total_quantity
            this_component.being_purchased = purchased_quantity
            this_component.being_used = used_quantity
            this_component.being_repaired = repair_quantity
            this_component.available_quantity = ((total_quantity + purchased_quantity) - used_quantity) - repair_quantity
            this_component.notes = notes 
            this_component.save()

        except Exception as e:
            context = {
                "form_message": { 
                    "error": "Save error",
                    "message": str(e),
                    "type": "danger"
                }
            }
            print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', str(e)
            return render(request, "component_add.html", context)

        return HttpResponseRedirect(reverse('component_list_page'))


    else:
        context = { 'categories': Category.objects.all() }
        return render(request, 'component_add.html', context) 


def component_delete_page(request, pk):
    if Component.objects.filter(id=pk).exists():
        try:
            this_component = Component.objects.get(id=pk)
            this_component.delete()

        except Exception as e:
            print '>>>>>>>>>', str(e)
            return HttpResponseRedirect(reverse('component_list_page'))

    return HttpResponseRedirect(reverse('component_list_page'))


def component_edit_page(request, pk):
    if request.method == "POST":

        component_name = request.POST.get('name')
        total_quantity = int(request.POST.get('total_qty'))
        purchased_quantity = int(request.POST.get('purchased_qty'))
        used_quantity = int(request.POST.get('used_qty'))
        repair_quantity = int(request.POST.get('repair_qty'))
        notes = request.POST.get('notes')

        try:
            this_component = Component.objects.get(id=pk)
            this_component.name = component_name
            this_component.total_quantity = total_quantity
            this_component.being_purchased = purchased_quantity
            this_component.being_used = used_quantity
            this_component.being_repaired = repair_quantity
            this_component.available_quantity = ((total_quantity + purchased_quantity) - used_quantity) - repair_quantity
            this_component.notes = notes
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
