# Generated by Django 3.2.3 on 2021-06-02 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meublog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='atualizado',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(verbose_name='Comentário'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data Criação'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Ativo'),
        ),
    ]
