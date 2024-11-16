from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class sign(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.username

class logo(models.Model):
    logo_image=models.ImageField(upload_to='statics/image',default='Trendnest')


class brand(models.Model):
    brand_name = models.CharField(max_length=50,default='H&M')
    def __str__(self):
        return self.brand_name

class banners(models.Model):
    brand_name = models.ForeignKey(brand,related_name='brand5',on_delete=models.CASCADE,default="men")
    banner = models.ImageField(upload_to='statics/image',default='bn')
    
    
class menban(models.Model):
    menban_name = models.CharField(max_length=50,default="kids")
    men_ban = models.ImageField(upload_to='statics/image',default='cs')       
    def __str__(self):
        return self.menban_name
    
    
class brandbnnr(models.Model):
    brand_name = models.ForeignKey(brand,related_name='brand4',on_delete=models.CASCADE,default="women")
    titleb=models.CharField(max_length=50,default='brands')
    s_card = models.ImageField(upload_to='statics/image',default='s')       # wait
    def __str__(self):
        return self.titleb
    

class wbanner(models.Model):
    brand_name = models.ForeignKey(brand,related_name='brand3',on_delete=models.CASCADE,default="levis")
    women_banner = models.ImageField(upload_to='statics/image',default='Ab')

class hwomencard(models.Model):
    brand_name = models.ForeignKey(brand,related_name='brand2',on_delete=models.CASCADE,default="polo")
    wcard_name = models.CharField(max_length=20,default="women")
    wcard_image = models.ImageField(upload_to='statics/image',default="kj")
    def __str__(self):
        return self.wcard_name
    

class hwomencard2(models.Model):
    brand_name = models.ForeignKey(brand,related_name='brand1',on_delete=models.CASCADE,default="trend")
    wcard2_name = models.CharField(max_length=20,default="boys")
    wcard2_image = models.ImageField(upload_to='statics/image',default="b")
    def __str__(self):
        return self.wcard2_name
    

class shoes(models.Model):
    brand_name = models.ForeignKey(brand,related_name='brands',on_delete=models.CASCADE,default="asian")
    shoes_cat = models.CharField(max_length=22)
    shoes_banner = models.ImageField(upload_to='statics/image',default='sho')
    def __str__(self):
        return self.shoes_cat
    
class category(models.Model):
    category_name = models.CharField(max_length=20,default='Male')
    def __str__(self):
        return self.category_name
    
class category2(models.Model):
    category2_name = models.CharField(max_length=39)
    def __str__(self):
        return self.category2_name
    
    
class product(models.Model):
    pro_name = models.CharField(max_length=100,default="products")
    def __str__(self):
        return self.pro_name
    
    
class fragrance(models.Model):
    brand_name = models.ForeignKey(brand,related_name='brand6',on_delete=models.CASCADE,default="men")
    frag_name = models.CharField(max_length=110,default='frag')
    def __str__(self):
        return self.frag_name
    
SIZE_CHOICE=(
    ('NA', 'NA'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL','Xtra Large'),
    ('XXl','Double Xtra Lagre'),
)


class card(models.Model):
    image = models.ImageField(upload_to='statics/image',default="ab")
    brand_name = models.ForeignKey(brand,related_name='brand',on_delete=models.CASCADE)
    pro_name = models.ForeignKey(product,related_name="prod",on_delete=models.CASCADE)
    frag_name = models.ForeignKey(fragrance,related_name='fragname',on_delete=models.CASCADE)
    shoes_cat = models.ForeignKey(shoes,related_name='shoes',on_delete=models.CASCADE)
    category_name = models.ForeignKey(category,related_name='categoriesname',on_delete=models.CASCADE)
    category2_name = models.ForeignKey(category2,related_name='cat2name',on_delete=models.CASCADE)
    title = models.TextField()
    size = models.CharField(choices=SIZE_CHOICE,max_length=20)
    product_title = models.CharField(max_length=103,default='women') 
    rating = models.CharField(max_length=31)
    price = models.IntegerField(null=True)
    image1 = models.ImageField(upload_to='statics/image')
    image2 = models.ImageField(upload_to='statics/image')
    image3 = models.ImageField(upload_to='statics/image')
    image4 = models.ImageField(upload_to='statics/image')
    image5 = models.ImageField(upload_to='statics/image')
    image6 = models.ImageField(upload_to='statics/image')
    def __str__(self):
        return self.title
    
# class product_card(models.Model):
#     image = models.ImageField(upload_to="statics/image")
#     title = models.TextField()
#     product_title = models.CharField(max_length=100,default="AB")

class Cartitem(models.Model):
    Card = models.ForeignKey(card, on_delete=models.CASCADE)
    qyt = models.CharField(max_length=100,default=0)
    Size = models.CharField(max_length=50,default="s")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Size
    

class wishlist(models.Model):
    product_name = models.ForeignKey(card, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='statics/image')
    price = models.IntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    

class Contactus(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(default='There is good service')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
   


