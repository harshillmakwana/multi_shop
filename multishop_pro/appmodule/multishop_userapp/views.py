from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from appmodule.multishop_userapp import forms
from appmodule.multishop_userapp.models import Order, OrderItem, wishlist, add_to_card, RazorpayPayment
from appmodule.multishop_adminapp import models
from django.contrib import messages
from django.contrib.auth import login , logout ,get_user_model, authenticate
from django.contrib.auth.decorators import login_required
import razorpay
from django.conf import settings



# Create your views here.

def myname(request):
    return HttpResponse("this is user aplication")

#pages

def index_view(request): 
    cat = models.category_sbu.objects.all()
    context = {'cat':cat}    
    return render(request,'users_app/index.html',context)


from django.core.paginator import Paginator
from django.db.models import Q

@login_required(login_url='login_view')
def shop_view(request):
    pro = models.product.objects.all()
    cat = models.category_sbu.objects.all()
    
    # shop search 
    search = request.GET.get('search')
    
    #index page category show
    category = request.GET.get('category')
    
    #price filter 
    price = request.GET.get('price')
    
    if search:
        pro = models.product.objects.filter(
            Q(product_name__icontains=search) |
            Q(product_despcrition__icontains=search)
        )
        
        cat = models.category_sbu.objects.filter(
            Q(category_name2__icontains=search)
        )
             
    if category :
        pro = pro.filter(
            cate_two_id = category
        ) 
           
    if price:
        min_price,max_price = price.split('-')
        
        min_price = int(min_price)
        max_price = int(max_price)
        
        pro = pro.filter(
            descount_price__gte =min_price,
            descount_price__lte=max_price
        )  
    paginator = Paginator(pro, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)     
        
    context = {'page_obj':page_obj , 'cat':cat ,}
    
    return render(request,'users_app/shop.html',context)



@login_required(login_url='login_view')
def checkout_view(request):
    return render(request,'users_app/checkout.html')

@login_required(login_url='login_view')
def contact_view(request):
    return render(request,'users_app/contact.html')

def pro_deatils_view(request, id):
    product = models.product.objects.get(id=id)
    
    if product.product_price > 0:
        discount_percent = round(((product.product_price - product.descount_price) / product.product_price) * 100)
    else:
        discount_percent = 0

    
    context = {'product':product}
    return render(request,'users_app/product_details.html',context)
    
    
User = get_user_model()
def registration_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        role = request.POST.get('role')
        phone_number = request.POST.get('phone_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        city = request.POST.get('city')

        
        
        if password != password1:
            messages.warning(request,"password is not match")
            return redirect(registration_view)
        
        if User.objects.filter(email=email).exists():
            messages.warning(request,"username is are exist")
            return redirect('registration_view')
        
        user = User.objects.create_user(username=email,email=email,password=password,role=role,phone_number=phone_number,
                                        first_name=first_name,last_name=last_name,address=address,city=city)
        
        if role == 'User':
            user.is_approved =True
            user.save()
        messages.success(request,"registration successfully")
        return redirect(login_view)
    return render(request,'users_app/registration.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request,username=email,password=password)
        
        if user is not None:
                login(request,user)
                messages.success(request,f"welcome back{user.username}")
                
                if user.role == 'Admin':
                    return redirect('index_view1')
                else:
                    return redirect(index_view)
        else:
            messages.warning(request,"invalid usernamen and password")
    return render(request,'users_app/login.html')
            
def logout_view(request):
    logout(request)
    messages.info(request,"logout succesfully!")
    return redirect('login_view')




@login_required(login_url='login_view')
def list_wishlist(request):
    item = wishlist.objects.filter(username=request.user)
    context = {'item':item}
    return render(request,'users_app/wishlist.html',context)

@login_required(login_url='login_view')
def add_to_wishlist(request, product_id):
    pro = get_object_or_404(models.product , id=product_id)
    wishlist.objects.get_or_create(username=request.user,pro_name=pro)
    messages.success(request,f"{ pro.product_name } add to successfully")
    return redirect(shop_view)

@login_required(login_url='login_view')
def remove_wishlist(request, product_id):
    wishlist.objects.filter(username=request.user, pro_name_id=product_id).delete()
    return redirect(list_wishlist)






# add to cart product view
@login_required(login_url='login_view')
def cart_view(request):
    cart = request.session.get('cart',{})
    grand_total = 0
    for key, value in cart.items():
        value['total'] = float(value['price']) * int(value['quantity'])
        grand_total += value['total']
    return render(request, 'users_app/cart.html', {
        'cart':        cart,
        'grand_total': grand_total,
        'shipping':    50,
        'order_total': grand_total + 50,
    })

def cart_add(request, id):
    pro = models.product.objects.get(id=id)
    size = request.POST.get('size')
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)]['quantity'] += 1
    else:
        cart[str(id)] = {
            'name': pro.product_name,
            'price': float(pro.descount_price),
            'quantity': 1,
            'image': pro.product_image.url,
            'size':size
        }
    request.session['cart'] = cart
    request.session.modified = True
    print(request.session['cart'])
    return redirect('shop_view')


def item_clear(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
    request.session['cart'] = cart
    return redirect('cart_view')


def item_increament(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)]['quantity'] += 1
    request.session['cart'] = cart
    return redirect('cart_view')


def item_decreament(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)]['quantity'] -= 1
        if cart[str(id)]['quantity'] <= 0:
            del cart[str(id)]
    request.session['cart'] = cart
    return redirect('cart_view')


def item_clear_all(request):
    request.session['cart'] = {}
    return redirect('cart_view')





def address_view(request):
    if request.method == 'POST':
        form = forms.address_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_view')
        else:
            print(form.errors)
    return render(request,'users_app/checkout.html')


@login_required(login_url='login_view')
def payment_view(request, id=None):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, "Your cart is empty. Please add items to your cart before checking out.")
        return redirect('cart_view')
        
    grand_total = 0
    for key, value in cart.items():
        value['total'] = float(value['price']) * int(value['quantity'])
        grand_total += value['total']
    shipping = 50
    order_total = grand_total + shipping

    # Initialize Razorpay client
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    if request.method == 'POST':
        # This block is executed when Razorpay payment is completed and posts to this view
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')
        
        if not (payment_id and order_id and signature):
            messages.error(request, "Invalid payment callback details.")
            return redirect('payment_view')

        try:
            # Verify the signature to ensure payment authenticity
            client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })

            # Payment verified successfully! Save transaction to the database
            payment_record = RazorpayPayment.objects.create(
                user=request.user,
                order_id=order_id,
                payment_id=payment_id,
                signature=signature,
                amount=order_total,
                status='Success'
            )

            # Create Order and OrderItems
            # Save the order using the Razorpay order ID and link to the RazorpayPayment record
            new_order = Order.objects.create(
                user=request.user,
                order_id=razorpay_order_id,
                total_amount=order_total,
                payment=payment_record
            )
            for p_id, item_data in cart.items():
                product = models.product.objects.get(id=p_id)
                OrderItem.objects.create(
                    order=new_order,
                    product=product,
                    quantity=item_data['quantity'],
                    price_at_purchase=item_data['price']
                )

            # Clear the cart session
            request.session['cart'] = {}
            request.session.modified = True

            # Save info in session to show on success page
            request.session['last_payment'] = {
                'payment_id': payment_id,
                'order_id': order_id,
                'amount': float(order_total)
            }

            messages.success(request, "Payment verified successfully!")
            return redirect('order_history_view')

        except Exception as e:
            messages.error(request, f"Payment verification failed: {str(e)}")
            return redirect('payment_view')

    # GET request: generate Razorpay order ID and render checkout page
    try:
        amount_paisa = int(order_total * 100)
        razorpay_order = client.order.create({
            'amount': amount_paisa,
            'currency': 'INR',
            'payment_capture': 1
        })
        razorpay_order_id = razorpay_order['id']
    except Exception as e:
        messages.error(request, f"Error initializing Razorpay order: {str(e)}")
        razorpay_order_id = None

    context = {
        'cart': cart,
        'grand_total': grand_total,
        'shipping': shipping,
        'order_total': order_total,
        'razorpay_order_id': razorpay_order_id,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'amount_paisa': int(order_total * 100),
        'user_email': request.user.email if request.user.is_authenticated else '',
        'user_phone': request.user.phone_number if request.user.is_authenticated and request.user.phone_number else '',
        'user_name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username
    }
    
    return render(request, 'users_app/create_payment.html', context)


@login_required(login_url='login_view')
def payment_success_view(request):
    payment_info = request.session.get('last_payment')
    if not payment_info:
        return redirect('shop_view')

    context = {
        'payment_id': payment_info.get('payment_id'),
        'order_id': payment_info.get('order_id'),
        'amount': payment_info.get('amount')
    }
    # Clear session info so page is only accessible once
    if 'last_payment' in request.session:
        del request.session['last_payment']
        request.session.modified = True

    return render(request, 'users_app/payment_success.html', context)

@login_required(login_url='login_view')
def order_history_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'users_app/order_history.html', context)



  


    