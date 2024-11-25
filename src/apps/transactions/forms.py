from django import forms
from .models import Transaction, Reason

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
    
    reason = forms.ModelChoiceField(
        queryset=Reason.objects.all(),
        label="Motivo",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Transaction
        fields = ['recipient','amount', 'reason']


class ReasonForm(forms.ModelForm):
    reason = forms.CharField(label='Ingrese el motivo nuevo', widget=forms.TextInput())
    
    class Meta:
        model = Reason
        fields = ['reason']
