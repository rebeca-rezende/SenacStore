from django import forms
from StoreApp.models import Cliente

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.CharField()
    telefone = forms.CharField()
    remetente = forms.CharField()
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
