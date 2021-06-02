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
        return reverse('meublog:detalhe', args=[self.slug])

    class Meta:
        ordering = ('-publicados',)
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo


class Comentario(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail')
    comentario = models.TextField('Comentário')
    criado = models.DateTimeField('Data Criação', auto_now_add=True)
    status = models.BooleanField('Ativo', default=False)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return 'Comentado por: ' + self.nome