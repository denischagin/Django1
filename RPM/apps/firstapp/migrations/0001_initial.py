# Generated by Django 4.0.2 on 2022-03-16 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firstapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simple_title', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('simple_text', models.TextField(verbose_name='текст статьи')),
                ('pub_date', models.DateTimeField(verbose_name='дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_author', models.CharField(max_length=50, verbose_name='Имя автора комментария')),
                ('text_comment', models.CharField(max_length=200, verbose_name='Текст комментария')),
                ('firstapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.firstapp')),
            ],
        ),
    ]
