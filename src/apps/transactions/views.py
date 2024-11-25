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

def create_transfer(request):
    
    template_name = 'transactions/transfer.html'

    form = forms.TransferForm()

    if request.method == 'POST':
        form = forms.TransferForm(request.POST)
        user = request.user
        if form.is_valid():
            transfer = form.save(commit=False) 
            recipient = transfer.recipient

            transfer.user = request.user  
            transfer.transaction_type = 'transferencia'
            transfer.save()                  
            

            user.balance -= transfer.amount
            recipient.balance += transfer.amount
            user.save()
            recipient.save()

            return redirect('home')

    return render(request, template_name, {'form': form})

def create_reason(request):
    template_name = 'transactions/reason/reason.html'

    form = forms.ReasonForm()

    if request.method == 'POST':
        form = forms.ReasonForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False) 
            deposit.save()

            return redirect('home')

    return render(request, template_name, {'form': form})