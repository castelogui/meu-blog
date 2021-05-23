from django import forms
from django.core.mail import EmailMessage


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
