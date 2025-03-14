from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Customer,Restaurants,Menu,Cart
from .forms import ResForm,AddMenu
import razorpay
from django.conf import settings
def home(req):
    return render(req,'delivery/index.html')

def index(req):
    return render(req,'delivery/index.html')

def signin(req):
    return render(req,'delivery/signin.html')

def signup(req):
    return render(req,'delivery/signup.html')

def handle_signin(req):
    li = Restaurants.objects.all()
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        try:
            cus = Customer.objects.get(username=username, password=password)
            if username == "admin":
                return render(req, 'delivery/success.html')
            else:
                return render(req, 'delivery/cusdisplay.html', {'username': username, 'li': li})
        except Customer.DoesNotExist:
            return render(req, 'delivery/failure.html')
    else:
        return render(req, 'delivery/signin.html')

def handle_signup(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        email = req.POST.get('email')
        mobile = req.POST.get('mobile')
        address = req.POST.get('address')
        
        try:
            cus = Customer.objects.get(username=username)
            # return HttpResponse("Customer with this username already exists.")
        except Customer.DoesNotExist:
            cus = Customer(username=username, password=password, email=email, mobile=mobile, address=address)
            cus.save()
        
        data = {
            'username': username,
            'password': password,
            'email': email,
            'mobile': mobile,
            'address': address
        }
        
        return render(req, 'delivery/signin.html', data)
    else:
        return HttpResponse('Invalid request')
    
def add_res(req):
    form = ResForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        try:
            res = Restaurants.objects.get(res_name=form.cleaned_data['res_name'])
            return HttpResponse("Restaurant with this name already exists.")
        except Restaurants.DoesNotExist:
            form.save()
            return render(req, 'delivery/display_res.html')
    return render(req, 'delivery/add_res.html', {'form': form})

def display_res(req):
    li = Restaurants.objects.all()
    return render(req,'delivery/display_res.html',{'li':li})

def view_menu(req, id):
    res = get_object_or_404(Restaurants, pk=id)
    menu = Menu.objects.filter(res=res)
    return render(req, 'delivery/menu.html', {'res': res, 'menu': menu})

def add_menu(req, id):
    res = get_object_or_404(Restaurants, pk=id)
    if req.method == 'POST':
        form = AddMenu(req.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.res = res
            menu_item.save()
            return redirect('delivery:view_menu', id=id)
    else:
        form = AddMenu()
    return render(req, 'delivery/menufrom.html', {'form': form, 'res': res})



def delete(req, id):
    try:
        item = Menu.objects.get(pk=id) 
        res = item.res  
        item.delete()   
        return render(req, 'delivery/menu.html', {'res': res})
    except Menu.DoesNotExist:
        return render(req, 'delivery/menu.html', {'res':res})

def update_menu(req,id):
    menu_item = Menu.objects.get(pk=id)
    if(req.method == "POST"):
        form = AddMenu(req.POST)
        if req.method == "POST":
            form = AddMenu(req.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('delivery:view_menu', id=menu_item.res.id)  
    else:
        form = AddMenu(instance=menu_item)
    return render(req, 'delivery/update_menu.html', {'form': form, 'menu_item': menu_item})  


def cusdisplay(req,username):
    res = Restaurants.objects.all()
    return render(req,'delivery/cusdisplay_res',{'username':username, 'res':res})

def cusview_menu(req,id,username):
    res = Restaurants.objects.get(pk=id)
    menu  = Menu.objects.filter(res=res)
    return render(req, 'delivery/cusview_menu.html', {'res': res, 'menu': menu, 'username': username})

    
def show_cart(req, username):
    customer = Customer.objects.get(username = username)
    cart = Cart.objects.filter(customer=customer).first()
    items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0
    return render(req, 'delivery/show_cart.html', {'items':items, 'total_price':total_price, 'username': username})


def add_to_cart(request,username,menuid):
    customer = Customer.objects.get(username = username)
    item = Menu.objects.get(pk=menuid)
    cart, created = Cart.objects.get_or_create(customer = customer)
    cart.items.add(item)
    messages.success(request,f"{item.item_name} added")
    return redirect('delivery:cusview_menu', id = item.res.id,username=username)



def checkout(request, username):
    customer = Customer.objects.get(username = username)
    cart = Cart.objects.filter(customer = customer).first()
    cart_items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0

    if total_price == 0:
        return render(request, 'delivery/checkout.html',{'error':'Your cart is Empty'})

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    order_data = {
        'amount':int(total_price * 100),
        'currency':'INR',
        'payment_capture':'1',
    }
    order = client.order.create(data = order_data)
    return render(
        request, 'delivery/checkout.html',
        {'username':username,
        'cart_items':cart_items,
        'total_price':total_price,
        'razorpay_key_id':settings.RAZORPAY_KEY_ID,
        'order_id':order['id'],
        'amount':total_price,
        }
    )
    
    
def orders(request, username):
        customer = Customer.objects.get(username = username)
        cart = Cart.objects.filter(customer=customer).first()
        cart_items = cart.items.all() if cart else []
        total_price = cart.total_price() if cart else 0

        if cart:
            cart.items.clear()

        return render(request, 'delivery/orders.html',{
        'username':username,
        'cart_items':cart_items,
        'total_price':total_price,
        'customer':customer
        })

