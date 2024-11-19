from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Cadastro(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=128)  # Aumentei o tamanho para suportar o hash
    
    def __str__(self):
        return f'{self.nome} - {self.email}'
    
    def set_password(self, raw_password):
        self.senha = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.senha)


class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Confirmado', 'Confirmado'),
        ('Remarcado', 'Remarcado'),
        ('Recusado', 'Recusado'),
    ]

    cliente = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data = models.DateField()
    servico = models.CharField(max_length=255)
    periodo = models.CharField(max_length=20)
    convenio = models.CharField(max_length=255, blank=True, null=True)
    detalhes_extras = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return f'{self.nome} - {self.data} - {self.status}'
