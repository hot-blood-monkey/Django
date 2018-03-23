from decimal import Decimal
from django.shortcuts import render



# Create your views here.
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from .task import order_created

def order_create(request):
    #获取到当前会话中的购物车
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])


                #清空购物车
                cart.clear()

                #调用异步任务
                order_created.delay(order.id)
                return render(request,
                              'orders/order/created.html',
                              {'order':order})

    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart':cart,'form':form})


