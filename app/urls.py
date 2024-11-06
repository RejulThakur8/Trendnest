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
               path('cart/',views.view_cart,name='cart'),
               path('add/<int:i_id>/',views.add_to_cart,name='add_to_cart'),
               path('remove/<int:item_id>/',views.remove_crt,name='remove_cart')
               ]
