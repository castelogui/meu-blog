from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView

from .forms import EmailPost
from .models import Post


class ListarPostView(ListView):
    queryset = Post.publicado.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = "meublog/post/listarposts.html"

class DetalharPostView(DetailView):
    template_name = "meublog/post/detalharpost.html"
    model = Post


class FormContatoView(FormView):
    template_name = 'meublog/post/sharepost.html'
    form_class = EmailPost
    success_url = reverse_lazy('meublog:listar_posts')

    def get_post(self, id_post):
        try:
            return Post.publicado.get(pk=id_post)
        except Post.DoesNotExist:
            messages.error(self.request, 'O post não existe!')
            reverse_lazy('meublog:listar_posts')

    def get_context_data(self, **kwargs):
        context = super(FormContatoView, self).get_context_data(**kwargs)
        context['post'] = self.get_post(self.kwargs['pk'])
        return context

    def form_valid(self, form, *args, **kwargs):
        meupost = self.get_context_data()['post']
        form.enviar_email(meupost)
        messages.success(self.request, f"Post {meupost.titulo} enviado com sucesso!")

        return super(FormContatoView,self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        meupost = self.get_context_data()['post']
        messages.error(self.request, f"Post {meupost.titulo} Não enviado!")

        return super(FormContatoView,self).form_invalid(form, *args, **kwargs)
