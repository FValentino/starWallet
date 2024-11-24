from django.db import models
from ..users.models import CustomUser

class Transaction(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='recipient')
    transaction_type = models.CharField(null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    reason = models.CharField(null=True, default='otros')
    date = models.DateTimeField(auto_now_add=True, null=False)