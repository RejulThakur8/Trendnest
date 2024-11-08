from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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

    category1=category.objects.all()[:4]
    categories=category2.objects.all()
    return render(request,'signin.html',{'category':category1,'categories':categories})

def signin_user(request):
    category1=category.objects.all()[:4]
    categories=category2.objects.all()
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.warning(request, 'Invalid Username')
            return redirect('/signin/',{'category':category1,'categories':categories})
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/signin/',{'category':category1,'categories':categories})
        
        else:
            login(request ,user)
            messages.success(request,'successfully login')
            return redirect('/home/',{'category':category1,'categories':categories})
        
    return render('signin.html',{'category':category1,'categories':categories})

def signout_user(request):
    category1=category.objects.all()[:4]
    categories=category2.objects.all()
    logout(request)
    return redirect('/home/',{'category':category1,'categories':categories})


def profile(request):
    category1=category.objects.all()[:4]
    categories=category2.objects.all()
    return render(request, 'profile.html',{'category':category1,'categories':categories})

def home(request):
    logo1=logo.objects.all()
    bnr=banners.objects.all()
    homecard=menban.objects.all()
    smcard=brandbnnr.objects.all()
    womenbnr=wbanner.objects.all()
    womencard=hwomencard.objects.all()
    womencard2=hwomencard2.objects.all()
    shoess=shoes.objects.all()
    category1=category.objects.all()[:4]
    categories=category2.objects.all()
    for l in logo1:
        l.logo_image=os.path.basename(l.logo_image.url)
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
        
    return render(request,'index.html',{'logo':logo1,'banner':bnr,'hcard':homecard,'smallcard':smcard,'wmnbnr':womenbnr,'womencard':womencard,'womencard2':womencard2,'shoes':shoess,'category':category1,'categories':categories[:2]})


def cards(request):
        if request.method=="POST":
            title1=request.POST.get("category")
            print(title1.title())
            card1=category.objects.get(category_name=title1.title())
            print(card1,title1)
            category1=category.objects.all()[:4]
            categories=category2.objects.all()
            brands=brand.objects.all()
            if card1:
                data=card.objects.filter(category_name=card1)
                print(data)
                for i in data:
                    i.image=os.path.basename(i.image.name)
                    print(i.category_name)
            return render(request,'product.html',{'data':data,'category':category1,'categories':categories,'brands':brands})
        return render(request,'index.html')

def product_det(request,iid,ititle):
    category1=category.objects.all()[:4]
    categories=category2.objects.all()
    prod=card.objects.get(id=iid)
    if prod:
        data=card.objects.filter(title=prod)
    for i in data:
        i.image1=os.path.basename(i.image1.url)
        i.image2=os.path.basename(i.image2.url)
        i.image3=os.path.basename(i.image3.url)
        i.image4=os.path.basename(i.image4.url)
        i.image5=os.path.basename(i.image5.url)
    return render(request,'product_detail.html',{'data':data,'category':category1,'categories':categories})


def car_t(request):
    category1=category.objects.all()[:4]
    categories=category2.objects.all()
    if request.method=="POST":
        Card_info = card.objects.get(id=request.POST['iid'])
        qyt1 = request.POST['qyt']
        tprice = int(Card_info.price) * int(qyt1)
        Cartitem.objects.create(Card=Card_info,qyt=qyt1,user=request.user,price=tprice)

    cartData = Cartitem.objects.filter(user=request.user)
    Total = 0
    for cd in cartData:
        Total+=int(cd.price)

    return render(request,'cart.html',{'cartData':cartData,'Total':Total,'category':category1,'categories':categories})
# def view_cart(request):
#     category1=category.objects.all()[:4]
#     categories=category2.objects.all()
#     cart_items = Cartitem.objects.filter(user=request.user)
#     total_price = sum(item.Card.price * item.quantity for item in cart_items)
#     return render(request, 'cart.html',{'cart_items':cart_items, 'total_price':total_price,'category':category1,'categories':categories})

# @login_required

# def add_to_cart(request,i_id):
#     card1 = card.objects.get(id=i_id)
#     cartitem, created = Cartitem.objects.get_or_create(Card=card1,user=request.user)

#     cartitem.quantity += 1

#     cartitem.save()
#     return redirect('app:view_cart')

# @login_required
def remove(request):
    if request.method=="POST":
        name1 = request.POST.get('Card')

        data = Cartitem.objects.filter(Card=name1,user=request.user)
        data.delete()

        cartData = Cartitem.objects.filter(user=request.user)
        Total=0
        for cd in cartData:
            Total+=int(cd.price)

    return redirect('/cart/')

