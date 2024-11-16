from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import hashers
from .models import * 
import os

# Create your views here.

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=hashers.make_password(password)
        user = User.objects.filter(email=email)

        if user.exists():
            messages.info(request, 'Email already exist! Use different mail')
            return redirect('/signin/')
        
        User.objects.create(username=username,email=email,password=password1)
        
        messages.success(request, 'Account Created succesfully')

    category1=category.objects.all()[:2]
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    return render(request,'signin.html',{'category':category1,'categories':categories,'brand':brands,'product':products})

def signin_user(request):
    category1=category.objects.all()[:2]
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.warning(request, 'Invalid Username')
            return redirect('/signin/',{'category':category1,'categories':categories,'brand':brands,'product':products})
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/signin/',{'category':category1,'categories':categories,'brand':brands,'product':products})
        
        else:
            login(request ,user)
            messages.success(request,'successfully login')
            return redirect('/home/',{'category':category1,'categories':categories,'brand':brands,'product':products})
        
    return render('signin.html',{'category':category1,'categories':categories,'brand':brands,'product':products})

def signout_user(request):
    category1=category.objects.all()[:3]
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    logout(request)
    return redirect('/home/',{'category':category1,'categories':categories,'brand':brands,'product':products})


def profile(request):
    category1=category.objects.all()[:2]
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    return render(request, 'profile.html',{'category':category1,'categories':categories,'brand':brands,'product':products})

def home(request):
    bnr=banners.objects.all()
    homecard=menban.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    smcard=brandbnnr.objects.all()
    womenbnr=wbanner.objects.all()
    womencard=hwomencard.objects.all()
    womencard2=hwomencard2.objects.all()
    shoess=shoes.objects.all()
    category1=category.objects.all()[:2]
    categories=category2.objects.all()
    for b in bnr:
        b.banner=os.path.basename(b.banner.url)
    for hcrd in homecard:
        hcrd.men_ban=os.path.basename(hcrd.men_ban.url)
    for scard in smcard:
        scard.s_card=os.path.basename(scard.s_card.url)
    for wbnr in womenbnr:
        wbnr.women_banner=os.path.basename(wbnr.women_banner.url)
    for wcrd in womencard:
        wcrd.wcard_image=os.path.basename(wcrd.wcard_image.url)
    for wcrd2 in womencard2:
        wcrd2.wcard2_image=os.path.basename(wcrd2.wcard2_image.url)
    for s in shoess:
        s.shoes_banner=os.path.basename(s.shoes_banner.url)
        
    return render(request,'index.html',{'banner':bnr,'hcard':homecard,'smallcard':smcard,'wmnbnr':womenbnr,'womencard':womencard,'womencard2':womencard2,'shoes':shoess,'category':category1,'categories':categories[:2],'brand':brands,'product':products})


def cards(request):
        if request.method=="POST":
            title1=request.POST.get("category")
            print(title1.title())
            card1=category.objects.get(category_name=title1.title())
            print(title1.title())

            category1=category.objects.all()[:4]
            categories=category2.objects.all()
            brands=brand.objects.all()
            products=product.objects.all()
            if card1:
                data=card.objects.filter(category_name=card1)
                print(data)
                for i in data:
                    i.image=os.path.basename(i.image.name)
                    print(i.category_name)
            return render(request,'product.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products})
        return render(request,'index.html')

def sec_card(request):
    brands=brand.objects.all()
    products=product.objects.all()
    if request.method=="POST":
        title2=request.POST.get("brand_name")
        c_ard=brand.objects.get(brand_name=title2)
        if c_ard:
            card_brand=card.objects.filter(brand_name=c_ard)
            for i in card_brand:
                i.image=os.path.basename(i.image.url)
        return render(request,"/products/",{'card_brand':card_brand,'brand':brands,'product':products})
    return render(request,{'card_brand':card_brand,'brand':brands,'product':products})


def product_det(request,iid,ititle):
    category1=category.objects.all()[:4]
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    prod=card.objects.get(id=iid)
    if prod:
        data=card.objects.filter(title=prod)
    for i in data:
        i.image1=os.path.basename(i.image1.url)
        i.image2=os.path.basename(i.image2.url)
        i.image3=os.path.basename(i.image3.url)
        i.image4=os.path.basename(i.image4.url)
        i.image5=os.path.basename(i.image5.url)
        i.image6=os.path.basename(i.image6.url)
    return render(request,'product_detail.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products})


def car_t(request):
    category1=category.objects.all()[:4]
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    if request.method=="POST":
        Card_info = card.objects.get(id=request.POST['iid'])
        qyt1 = request.POST['qyt']
        si_ze = request.POST['si-ze']
        tprice = int(Card_info.price) * int(qyt1)
        Cartitem.objects.create(Card=Card_info,qyt=qyt1,user=request.user,price=tprice,Size=si_ze)

    cartData = Cartitem.objects.filter(user=request.user)
    Subtotal = 0
    for cd in cartData:
        Subtotal+=int(cd.price)

    return render(request,'cart.html',{'cartData':cartData,'Subtotal':Subtotal,'category':category1,'categories':categories,'brand':brands,'product':products})

def remove(request):
    if request.method=="POST":
        name1 = request.POST.get('Card')

        data = Cartitem.objects.filter(Card=name1,user=request.user)
        data.delete()

        
        cartData = Cartitem.objects.filter(user=request.user)
        Total=0
        for cd in cartData:
            Total+=int(cd.price)

    # return render(request,'index.html',{'cartData':cartData,'wishdata':wishdata})
    return redirect('/cart/')

def wish(request):
    try:
        category1=category.objects.all()[:4]
        categories=category2.objects.all()
        brands=brand.objects.all()
        products=product.objects.all()
    
    except AttributeError as e:
        return render(request, "wishlist.html", {'error' : f"database issue {str(e)}"})

    wishdata = wishlist.objects.filter(user=request.user) if request.user.is_authenticated else None

    if request.method=="POST":

        try:
            wish = card.objects.get(id=request.POST['wiid'])
            price = int(wish.price)

            if request.user.is_authenticated:
                if not wishlist.objects.filter(product_name=wish,user=request.user).exists():
                    wishlist.objects.create(product_name=wish,price=price,user=request.user)

            wishdata = wishlist.objects.filter(user = request.user)
        except ObjectDoesNotExist:
            return render(request, 'wishlist.html',{'error':'This product not exist','wishdata':wishdata,'category':category1,'categories':categories,'brand':brands,'product':products})
        

        except ValueError:
            return render(request,'wishlist.html',{'error':'Invalid price value.','wishdata':wishdata,'category':category1,'categories':categories,'brand':brands,'product':products}
                          )
        
        # for i in wishdata:
        #     i.price
    return render(request, 'wishlist.html',{'wishdata':wishdata,'category':category1,'categories':categories,'brand':brands,'product':products})

@login_required
def wremove(request):
    if request.method == "POST":
        item_id = request.POST.get('product_name')

        data1 = wishlist.objects.filter(product_name=item_id,user = request.user)
        data1.delete()
        
        return redirect('/wishlist')


def contact(request):
    category1=category.objects.all()[:4]
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    logo1=logo.objects.all()
    if request.method=="POST":
        name = request.POST.get('name1')
        email = request.POST.get('email1')
        message = request.POST.get('message')
        Contactus.objects.create(name=name,email=email,message=message,user=request.user)
    for l in logo1:
        l.logo_image=os.path.basename(l.logo_image.url)
    return render(request,'contact.html',{'logo':logo1,'category':category1,'categories':categories,'brand':brands,'product':products})   