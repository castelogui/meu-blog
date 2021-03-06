# Generated by Django 3.2.3 on 2021-05-25 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100)),
                ('corpo', models.TextField()),
                ('publicados', models.DateTimeField(default=django.utils.timezone.now)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'publicado')], default='rascunho', max_length=9)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meublog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('-publicados',),
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('comentario', models.TextField()),
                ('criado', models.DateTimeField(default=django.utils.timezone.now)),
                ('atualizado', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo', max_length=7)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meublog.post')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ('-criado',),
            },
        ),
    ]
