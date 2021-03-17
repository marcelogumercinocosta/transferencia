from django.db import models


class Satelite(models.Model):
    satelite = models.CharField('Satélite', max_length=255)

    class Meta :
        ordering = ['satelite']

    def __str__(self):
        return self.satelite


class Servidor(models.Model):
    servidor = models.CharField(max_length=255)
    montagem = models.CharField('Montagem', max_length=255)
    formato_diretorio = models.CharField('Formato do diretorio', max_length=255)
    satelite = models.ForeignKey("core.Satelite", verbose_name="Satélite", on_delete=models.PROTECT)

    class Meta :
        ordering = ['servidor']
        verbose_name_plural = "Servidores"

    def __str__(self):
        return f"{self.satelite.satelite}/{self.servidor}"


class Antena(models.Model):
    LOCAL = (
        ("Cacheira Paulista", "Cacheira Paulista"),
        ("Cuiabá", "Cuiabá"),
    )

    antena = models.CharField(max_length=255)
    metragem = models.CharField(max_length=255)
    local = models.CharField(choices=LOCAL, max_length=255)

    class Meta :
        ordering = ['local','antena']

    def __str__(self):
        return f"{self.local}/{self.antena}"


class Passagem(models.Model):
    antena = models.ForeignKey("core.Antena",  on_delete=models.PROTECT)
    servidor = models.ForeignKey("core.Servidor",  on_delete=models.PROTECT)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    qt_passagem = models.IntegerField('Quant. Passagem', blank=True, null=True)
    qt_arquivos = models.IntegerField('Quant. Arquivo',  blank=True, null=True)

    #Metadata
    class Meta :
        ordering = ['-inicio']
        verbose_name_plural = "Passagens"

    def __str__(self):
        return f"{self.inicio} / {self.fim} / {self.servidor}"