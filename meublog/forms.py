from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from meublog.models import Comentario


class EmailPost(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    destino = forms.EmailField()
    coments = forms.CharField(required=False, widget=forms.Textarea)

    def enviar_email(self, meupost):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        destino = self.cleaned_data['destino']
        coments = self.cleaned_data['coments']

        conteudo = f"Recomendo Ler o Post: {meupost.titulo}/n" \
                   f"Comentários: {coments}"
        mail = EmailMessage(
            subject=f"Recomendo este Post",
            body=conteudo,
            from_email='contato@meublog.com',
            to=[destino,],
            headers={'Reply-to': email}
        )
        mail.send()


class ComentarioModelForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'email', 'comentario']

    def comentar(self, post):
        new_comment = self.save(commit=False)
        new_comment.post = post
        new_comment.nome = self.cleaned_data['nome']
        new_comment.email = self.cleaned_data['email']
        new_comment.comentario = self.cleaned_data['comentario']
        return new_comment.save()


class CadUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
