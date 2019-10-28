from django.conf import settings
from django.db import models
from django.utils import timezone


class Section(models.Model):
    title = models.CharField(max_length = 256, verbose_name = 'Section Title')
    def __str__(self):
        return self.title

class Post(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null = True, blank = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.URLField(verbose_name="Link de acesso", blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Material(models.Model):
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    autor = models.CharField(verbose_name="Autor" , max_length=256, blank = True, null = True)
    titulo = models.CharField(verbose_name= "Título", max_length=200)
    desc = models.TextField(verbose_name=  "Descrição/Referências bibliográficas", null = True, blank = True)
    paginas= models.IntegerField(verbose_name= "Páginas", blank = True, null = True)
    videos = models.IntegerField(verbose_name= "Vídeos", blank= True, null = True)
    url = models.CharField(verbose_name= "URL", max_length=200, null = True, blank= True)
    created_date = models.DateTimeField(verbose_name = "Data de criação", null = True, blank = True,  default=timezone.now)
    published_date = models.DateTimeField(verbose_name= "Data de publicação", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Video(models.Model):
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    autor = models.CharField(verbose_name="Autor" , max_length=256, blank = True, null = True)
    titulo = models.CharField(verbose_name= "Título", max_length=200)
    desc = models.TextField(verbose_name=  "Descrição/Referências bibliográficas", null = True, blank = True)
    duracao= models.FloatField(verbose_name= "Duração", blank = True, null = True)
    videos = models.IntegerField(verbose_name= "Vídeos", blank= True, null = True)
    url = models.CharField(verbose_name= "URL", max_length=200, null = True, blank= True)
    created_date = models.DateTimeField(verbose_name = "Data de criação", null = True, blank = True,  default=timezone.now)
    published_date = models.DateTimeField(verbose_name= "Data de publicação", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo