# Generated by Django 5.1.1 on 2024-11-22 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_brand_brand_name_alter_card_brnd_bn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='frag_name',
        ),
        migrations.CreateModel(
            name='mbanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbanner_name', models.CharField(default='frag', max_length=110)),
                ('mbanner_image', models.ImageField(upload_to='statics/image')),
                ('brand_name', models.ForeignKey(default='men', on_delete=django.db.models.deletion.CASCADE, related_name='h', to='app.brand')),
            ],
        ),
        migrations.DeleteModel(
            name='fragrance',
        ),
    ]