from django.shortcuts import render, get_object_or_404
from .models import Cryptocurrency


def index(request):
    request_get_search = request.GET.get('search')
    request_get_order_param = request.GET.get('order_param')
    request_get_order_dir = request.GET.get('order_direction')
    coins = Cryptocurrency.objects.all().order_by('rank')
    
    if request_get_search:
        coins = coins.filter(name__icontains=request_get_search)
    
    if request_get_order_param:
        if request_get_order_dir == 'dsc':
            coins = coins.order_by(('-'+request_get_order_param))
        else:
            coins = coins.order_by(request_get_order_param)
    

    
    return render(request, 'index.html', {
        'coins': coins,
        'request_get_search': request_get_search,
        'order_param': request_get_order_param,
        'order_direction': request_get_order_dir
    })

def detail(request,id):
    coin = get_object_or_404(Cryptocurrency,id=id)
    return render(request,'detail.html',{
        'coin':coin
    })