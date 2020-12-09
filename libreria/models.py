from django.db import models
    
class Genere_ArducaDiego(models.Model):
    nome= models.CharField(max_length=20)

    def __str__(self):
        return self.nome 
    
    class Meta:
        verbose_name="Genere"
        verbose_name_plural="Generi"

class Autore_ArducaDiego(models.Model):
    nome= models.CharField(max_length=20)
    cognome= models.CharField(max_length=20) 

    def __str__(self):
        return self.nome + " " + self.cognome

    class Meta:
        verbose_name="Autore"
        verbose_name_plural="Autori"
        
    

class Libro_ArducaDiego(models.Model):
    titolo= models.CharField(max_length=20)
    autore= models.ForeignKey(Autore_ArducaDiego, on_delete=models.CASCADE, related_name="libri")
    genere = models.ManyToManyField(Genere_ArducaDiego)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name="Libro"
        verbose_name_plural="Libri"

