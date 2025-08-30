from django.db import models

class Bases(models.Model):
    criação = models.DateTimeField(auto_now_add=True)
    atualização = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class meta: 
        abstract = True
class cursos(Bases):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta: 
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']
    def __str__(self):
        return self.titulo
class avaliações(Bases): 
    curso = models.ForeignKey(cursos, related_name='avaliações', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliação = models.DecimalField(max_digits=4,decimal_places=2)

    class Meta: 
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['nome','curso']
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliação}'