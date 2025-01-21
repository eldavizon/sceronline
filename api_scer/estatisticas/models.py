from django.db import models

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
    
