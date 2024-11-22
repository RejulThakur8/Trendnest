from django.contrib import admin
from .models import brand,banners,menban,brandbnnr,wbanner,hwomencard,hwomencard2,shoes,category,category2,product,mbanner,card,sign,logo,Cartitem,Contactus,wishlist
# Register your models here.


class cardModelAdmin(admin.ModelAdmin):
    list_display=['id','title','price','image','brand_name']


admin.site.register(brand)#
admin.site.register(banners)#
admin.site.register(menban)#
admin.site.register(brandbnnr)#
admin.site.register(wbanner)#
admin.site.register(hwomencard)#
admin.site.register(hwomencard2)#
admin.site.register(shoes)#
admin.site.register(category) #
admin.site.register(category2) #
admin.site.register(product)#
admin.site.register(mbanner)#
admin.site.register(card)#
admin.site.register(sign)
admin.site.register(logo)
admin.site.register(Cartitem)
admin.site.register(Contactus)
admin.site.register(wishlist)