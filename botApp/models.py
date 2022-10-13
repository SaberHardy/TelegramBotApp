from django.db import models


class Words(models.Model):
    class Meta:
        verbose_name = "Word"

    GENDERS = (
        ('MAS', 'MAS'),
        ('FEM', 'FEM'),
        ('GEN', 'GEN'),
    )
    word = models.CharField(max_length=100, verbose_name="word")
    gender = models.CharField(max_length=4, verbose_name="Gender", choices=GENDERS)

    def __str__(self):
        return self.word + " " + self.gender
