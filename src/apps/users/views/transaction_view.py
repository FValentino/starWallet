from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...transactions.models import Transaction

@login_required
def transaction_history(request):
    template_name = 'transactions/history.html'
    
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    
    return render(request, template_name, {'transactions': transactions})