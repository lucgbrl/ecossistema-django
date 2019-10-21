# Generated by Django 2.2.6 on 2019-10-17 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materiais', '0002_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(blank=True, max_length=256, null=True, verbose_name='Autor')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Descrição/Referências bibliográficas')),
                ('duracao', models.FloatField(blank=True, null=True, verbose_name='Duração')),
                ('videos', models.IntegerField(blank=True, null=True, verbose_name='Vídeos')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data de criação')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Data de publicação')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
