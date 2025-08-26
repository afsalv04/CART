from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import UserProfile,Product,CartItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def members(request):
    return HttpResponse("Hello World")


def afsal(request):
    return HttpResponse("hello Afsal")


def  index(request):
    return render (request,"index.html")

# def user_login(request):
#     return render (request,"login.html")

# def signup(request):
#     return render (request,"signup.html")

def shop(request):
    return render (request,"shop.html")

def services(request):
    return render (request,"services.html")

def contactus(request):
    return render (request,"contactus.html")

def checkout(request):
    return render (request,"checkout.html")

def cart(request):
    return render (request,"cart.html")

# def singleproduct(request):
#     return render (request,"singleproduct.html")

def thankyou(request):
    return render (request,"thankyou.html")

def about(request):
    return render (request,"about.html")










def signup(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Basic validation
        if password != confirm_password:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})

        # Check if username (which is email) already exists
        if User.objects.filter(username=email).exists():
            return render(request, 'signup.html', {'error_message': 'Email already exists'})

        try:
            # Create user, setting username to email
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = fullname
            user.save()

            # Create profile linked to user
            UserProfile.objects.create(user=user, mobile=mobile)

            # Log the user in immediately (optional)
            login(request, user)

            # Redirect to login page or home page as you want
            return redirect('user_login')

        except Exception as e:
            # Log the error for debugging and show a friendly message
            print(f"Error creating user or profile: {e}")
            return render(request, 'signup.html', {'error_message': 'An error occurred during registration. Please try again.'})

    # If GET request, just render signup form
    return render(request, 'signup.html')



def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # authenticate expects username, which you set as email
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})

    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')



def  single1(request):
    return render (request,"single1.html")


def  single2(request):
    return render (request,"single2.html")

def  single3(request):
    return render (request,"single3.html")



def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html',{'products':products})


def singleproduct(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'singleproduct.html', {'product': product})



def cart(request):
    cart_items = CartItem.objects.all()
    cart_total = sum(item.total() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'cart_total': cart_total})

from django.shortcuts import get_object_or_404, redirect
from .models import Product, CartItem

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')



def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')


def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()  # if set to 0 → remove item
    return redirect('cart')
