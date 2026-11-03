from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'

    def __str__(self):
        return self.nome


class Instrutor(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    especialidade = models.CharField(max_length=100, blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'instrutor'
        verbose_name_plural = 'instrutores'

    def __str__(self):
        return self.nome


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    duracao_dias = models.PositiveSmallIntegerField(
        default=30,
        validators=[MinValueValidator(1)],
        help_text='Duração do plano em dias.',
    )
    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'plano'
        verbose_name_plural = 'planos'

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    class Status(models.TextChoices):
        ATIVA = 'ativa', 'Ativa'
        PAUSADA = 'pausada', 'Pausada'
        ENCERRADA = 'encerrada', 'Encerrada'

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.PROTECT,
        related_name='matriculas',
    )
    plano = models.ForeignKey(
        Plano,
        on_delete=models.PROTECT,
        related_name='matriculas',
    )
    data_inicio = models.DateField(default=timezone.localdate)
    data_fim = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ATIVA,
    )
    observacoes = models.TextField(blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_inicio']
        verbose_name = 'matrícula'
        verbose_name_plural = 'matrículas'

    def __str__(self):
        return f'{self.aluno} — {self.plano}'


class Pagamento(models.Model):
    class Status(models.TextChoices):
        PENDENTE = 'pendente', 'Pendente'
        PAGO = 'pago', 'Pago'
        ATRASADO = 'atrasado', 'Atrasado'
        CANCELADO = 'cancelado', 'Cancelado'

    class Forma(models.TextChoices):
        PIX = 'pix', 'Pix'
        DINHEIRO = 'dinheiro', 'Dinheiro'
        CARTAO = 'cartao', 'Cartão'
        TRANSFERENCIA = 'transferencia', 'Transferência'

    matricula = models.ForeignKey(
        Matricula,
        on_delete=models.PROTECT,
        related_name='pagamentos',
    )
    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    forma = models.CharField(
        max_length=15,
        choices=Forma.choices,
        blank=True,
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDENTE,
    )
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_vencimento']
        verbose_name = 'pagamento'
        verbose_name_plural = 'pagamentos'

    def __str__(self):
        return f'{self.matricula.aluno} — R$ {self.valor}'
