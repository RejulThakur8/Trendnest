# Generated by Django 5.1.1 on 2024-11-22 11:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(default='H&M', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='Male', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='category2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category2_name', models.CharField(max_length=39)),
            ],
        ),
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_image', models.ImageField(default='Trendnest', upload_to='statics/image')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(default='products', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_name', models.CharField(max_length=50)),
                ('banner', models.ImageField(default='bn', upload_to='statics/image')),
                ('brand_name', models.ForeignKey(default='men', on_delete=django.db.models.deletion.CASCADE, related_name='brand5', to='app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='brandbnnr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brnd_bn', models.CharField(max_length=50)),
                ('s_card', models.ImageField(default='s', upload_to='statics/image')),
                ('brand_name', models.ForeignKey(default='women', on_delete=django.db.models.deletion.CASCADE, related_name='bbr', to='app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='ab', upload_to='statics/image')),
                ('title', models.TextField()),
                ('size', models.CharField(choices=[('NA', 'NA'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Xtra Large'), ('XXl', 'Double Xtra Lagre'), ('UK', '5'), ('UK', '6'), ('UK', '7'), ('UK', '8'), ('UK', '9'), ('UK', '10'), ('UK', '11')], max_length=20)),
                ('product_title', models.CharField(default='women', max_length=103)),
                ('rating', models.CharField(max_length=31)),
                ('price', models.IntegerField(null=True)),
                ('image1', models.ImageField(upload_to='statics/image')),
                ('image2', models.ImageField(upload_to='statics/image')),
                ('image3', models.ImageField(upload_to='statics/image')),
                ('image4', models.ImageField(upload_to='statics/image')),
                ('image5', models.ImageField(upload_to='statics/image')),
                ('image6', models.ImageField(upload_to='statics/image')),
                ('banner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_n', to='app.banners')),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='app.brand')),
                ('brnd_bn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='br_b', to='app.brandbnnr')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoriesname', to='app.category')),
                ('category2_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat2name', to='app.category2')),
            ],
        ),
        migrations.CreateModel(
            name='Cartitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qyt', models.CharField(default=0, max_length=100)),
                ('Size', models.CharField(default='s', max_length=50)),
                ('price', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(default='There is good service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='fragrance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frag_name', models.CharField(default='frag', max_length=110)),
                ('brand_name', models.ForeignKey(default='men', on_delete=django.db.models.deletion.CASCADE, related_name='b', to='app.brand')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='frag_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fragname', to='app.fragrance'),
        ),
        migrations.CreateModel(
            name='hwomencard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wcard_name', models.CharField(default='women', max_length=20)),
                ('wcard_image', models.ImageField(default='kj', upload_to='statics/image')),
                ('brand_name', models.ForeignKey(default='polo', on_delete=django.db.models.deletion.CASCADE, related_name='hw2', to='app.brand')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='wcard_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wc_nm', to='app.hwomencard'),
        ),
        migrations.CreateModel(
            name='hwomencard2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wcard2_name', models.CharField(default='boys', max_length=20)),
                ('wcard2_image', models.ImageField(default='b', upload_to='statics/image')),
                ('brand_name', models.ForeignKey(default='trend', on_delete=django.db.models.deletion.CASCADE, related_name='hw', to='app.brand')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='wcard2_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wc2_n', to='app.hwomencard2'),
        ),
        migrations.CreateModel(
            name='menban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menban_name', models.CharField(default='kids', max_length=50)),
                ('men_ban', models.ImageField(default='cs', upload_to='statics/image')),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='m_bnr', to='app.brand')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='menban_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='m_bn', to='app.menban'),
        ),
        migrations.AddField(
            model_name='card',
            name='pro_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod', to='app.product'),
        ),
        migrations.CreateModel(
            name='shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoes_cat', models.CharField(max_length=22)),
                ('shoes_banner', models.ImageField(default='sho', upload_to='statics/image')),
                ('brand_name', models.ForeignKey(default='asian', on_delete=django.db.models.deletion.CASCADE, related_name='sb', to='app.brand')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='shoes_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sh_cat', to='app.shoes'),
        ),
        migrations.CreateModel(
            name='wbanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wbanner_name', models.CharField(max_length=50)),
                ('women_banner', models.ImageField(default='Ab', upload_to='statics/image')),
                ('brand_name', models.ForeignKey(default='levis', on_delete=django.db.models.deletion.CASCADE, related_name='w_b4', to='app.brand')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='wbanner_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wb_n', to='app.wbanner'),
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='statics/image')),
                ('price', models.IntegerField(null=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
