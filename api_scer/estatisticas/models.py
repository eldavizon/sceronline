from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CLASSIFICACAO = (
    ('category', 'category'),
    ('food', 'food'),
    ('eletronico', 'eletronico'),
)

class Produto(models.Model):
    nome = models.CharField(max_length=200, null=True)
    classificacao = models.CharField(max_length=200, choices=CLASSIFICACAO , null=True)
    quantidade = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f'{self.nome}-{self.quantidade}'
    
class Retirada(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    
    quantidade_retirada = models.PositiveIntegerField(null=True)
    
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.produto} retirado por {self.staff.username}'
    
    
