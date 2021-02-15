from django.shortcuts import render, redirect, reverse, HttpResponse


# Create your views here.

def view_trolley(request):
    """ View to connect and return the shopping trolley page """
    return render(request,'trolley/trolley.html')


def add_to_trolley(request, item_id):
    """ Add a quantity of the specified product to the shopping trolley """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    trolley = request.session.get('trolley', {})

    if item_id in list(trolley.keys()):
        trolley[item_id] += quantity
    else:
        trolley[item_id] = quantity

    request.session['trolley'] = trolley
    return redirect(redirect_url)

def adjust_trolley(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    trolley = request.session.get('trolley', {})
    
    if quantity > 0:
        if quantity < 100:
            trolley[item_id] = quantity
        else:
            trolley[item_id] =  99
    else:
        trolley.pop(item_id)

    request.session['trolley'] = trolley
    return redirect(reverse('view_trolley'))


def remove_from_trolley(request, item_id):
    """Remove the item from the shopping trolley"""

    try:
        trolley = request.session.get('trolley', {})
        trolley.pop(item_id)
        request.session['trolley'] = trolley
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)