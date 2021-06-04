from django.contrib import admin
from .models import Post, Comentario


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'publicados', 'status')
    list_filter = ('status', 'criado', 'publicados', 'autor')
    search_fields = ('titulo', 'corpo')
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicados'
    ordering = ('status', '-publicados')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'post', 'email', 'criado', 'status')
    list_filter = ('status', 'criado')
    ordering = ('status', 'post', 'criado')
