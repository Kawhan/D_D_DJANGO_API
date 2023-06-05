from django.db import models


class Character(models.Model):
    nome = models.CharField(max_length=250)
    raca = models.CharField(max_length=70)
    forca = models.FloatField()
    destreza = models.FloatField()
    construcao = models.FloatField()
    inteligencia = models.FloatField()
    sabedoria = models.FloatField()
    classe_armadura = models.FloatField()
    iniciativa = models.FloatField()
    deslocamento = models.FloatField()
    ponto_vida_max = models.FloatField()
    pontos_vida_atual = models.FloatField()
    pontos_vida_temp = models.FloatField()
    equipamentos = models.TextField()
    tracos_personalidade = models.TextField()
    ideais = models.TextField()
    vinculos = models.TextField()
    fraquezas = models.TextField()

    def __str__(self):
        return self.nome + ' - ' + self.raca
