from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

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
               # path('wremove/',views.wish_remove,name='wremove')
               ]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)