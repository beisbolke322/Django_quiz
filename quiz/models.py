from django.db import models

# Create your models here.


class Generatorius(models.Model):
    amount = models.IntegerField("Kiekis")
    category = models.IntegerField("Kategorija")
    difficulty = models.CharField("Kategorija", max_length=10)

    class Meta:
        verbose_name = 'Generatorius'
        verbose_name_plural = 'Generatoriai'

    def __str__(self):
        return self.amount
        return self.category
        return self.difficulty
