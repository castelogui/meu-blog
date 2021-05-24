from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class PublicadosManager(models.Manager):
    def get_queryset(self):
        return super(PublicadosManager, self).get_queryset().filter(status='publicado')


class Post(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'publicado')
    )
    objects = models.Manager()
    publicado = PublicadosManager()

    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100)
    corpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meublog_posts')
    publicados = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='rascunho')

    def gwt_absolute_url(self):
        return reverse('meublog:detalhe',
                       args=[self.publicados.year,
                             self.publicados.month,
                             self.publicados.day,
                             self.slug])

    class Meta:
        ordering = ('-publicados',)
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo')
    )
    objects = models.Manager()
    publicado = PublicadosManager()

    nome = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    comentario = models.TextField()
    criado = models.DateTimeField(default=timezone.now)
    atualizado = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='ativo')

    class Meta:
        ordering = ('-criado',)
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.nome