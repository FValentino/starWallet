from django import forms
from .models import Transaction

from ..users.models import CustomUser

class DepositForm(forms.ModelForm):

    amount = forms.DecimalField(label='Ingrese el monto $', widget=forms.NumberInput(attrs={'min':'1', 'step':'0.01'}))
    
    class Meta:
        model = Transaction
        fields = ['amount']


class TransferForm(forms.ModelForm):

    recipient = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        label="Destinatario",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    amount = forms.DecimalField(label="Monto a transferir", max_digits=10, decimal_places=2, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'step':'0.01'}))
    
    reason = forms.CharField( label="Motivo (opcional)",  required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Transaction
        fields = ['recipient','amount', 'reason']
