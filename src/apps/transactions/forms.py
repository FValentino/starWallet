from django import forms
from .models import Transaction

class DepositForm(forms.ModelForm):

    amount = forms.DecimalField(label='Ingrese el monto $', widget=forms.NumberInput(attrs={'min':'1', 'step':'0.01'}))
    
    class Meta:
        model = Transaction
        fields = ['amount']
        