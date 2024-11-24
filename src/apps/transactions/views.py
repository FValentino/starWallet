from django.shortcuts import render, redirect

from . import forms

def create_deposit(request):
    template_name = 'transactions/deposit.html'

    form = forms.DepositForm()

    if request.method == 'POST':
        form = forms.DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False) 
            deposit.user = request.user  
            deposit.transaction_type = 'deposito' 
            deposit.reason = 'deposito'  
            deposit.save()                    
            return redirect('home')

    return render(request, template_name, {'form': form})