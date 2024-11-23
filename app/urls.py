from django.urls import path,include
from app import views


urlpatterns = [path('home/',views.home,name='home'),
               path('signin/',views.signin,name='signin'),
               path('products/',views.cards,name="products"),
               path('i/<str:ititle>/<int:iid>',views.product_det,name="productd"),
               path('signin/',views.signin,name='signin'),
               path('login/',views.signin_user,name='login'),
               path('logout/',views.signout_user,name='logout'),
               path('profile/',views.profile,name='profile'),
               path('cart/',views.car_t,name='cart'),
               path('remove/',views.remove,name='remove'),
               path('wishlist/',views.wish,name='wishlist'),
               path('contact/',views.contact,name='contact'),
               path('wremove/',views.wremove,name='wremove'),
               path('br_pro/',views.br_card,name='br_pro'),
               path('product%name/',views.product_cart,name='product%name'),
               path('baners/',views.baners,name='baners'),
               path('trends/',views.Trends,name='trends'),
               path('Men%clothing/',views.Menclothing,name='Men%clothing'),
               path('Women%clothing/',views.Wenclothing,name='Women%clothing'),
               path('top%brand/',views.Topbrand,name='top%brand'),
               path('women%brand/',views.Womenbrand,name='women%brand'),
               path('star%brand/',views.Starbrand,name='star%brand'),
               path('shoes%brand/',views.Shoesbanner,name='shoes%brand'),
               ]