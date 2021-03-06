# Generated by Django 3.0.6 on 2020-12-15 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('p_name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Technical', 'Technical'), ('Consumable', 'Consumable'), ('Sports', 'Sports'), ('Fashion', 'Fashion')], max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('user', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=254)),
                ('rate', models.IntegerField()),
                ('review', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RatingApp.Product')),
            ],
        ),
    ]
