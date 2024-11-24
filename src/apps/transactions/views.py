from django.shortcuts import render, redirect

from . import forms

def create_deposit(request):
    template_name = 'transactions/deposit.html'

    form = forms.DepositForm()

    if request.method == 'POST':
        form = forms.DepositForm(request.POST)
        user = request.user
        if form.is_valid():
            deposit = form.save(commit=False) 
            deposit.user = request.user  
            deposit.transaction_type = 'deposito' 
            deposit.reason = 'deposito'  
            deposit.save()                  

            user.balance += deposit.amount
            user.save()
            return redirect('home')

    return render(request, template_name, {'form': form})