from django.db import models

# Create your models here.
class  Persona(models.Model):
    nombre = models.CharField( max_length = 50, null = False)
    dni = models.CharField(max_length = 8, null = False)

    def __str__(self):
        return '{}'.format(self.nombre)

class CentroEstudio(models.Model):
    DescCentEst = models.CharField( max_length = 100, null = False)
    estados = ((1, 'S'), (2, 'N'))
    Vigente = models.IntegerField(choices=estados, default=2)

    def __str__(self):
        return '{}'.format(self.DescCentEst)

class Profesiones(models.Model):
    Grado = models.CharField(max_length = 10, null = False)
    DesProf= models.CharField(max_length = 30, null = False)
    estados = ((1,'S'),(2,'N'))
    Vigente = models.IntegerField(choices=estados,default=2)

    def __str__(self):
        return '{}'.format(self.DesProf)

class Capacitacion(models.Model):
    CodPers = models.ForeignKey(Persona, null = False, blank = True, on_delete = models.CASCADE)
    CodCentEst = models.ForeignKey(CentroEstudio, null = False, blank = True, on_delete = models.CASCADE)
    CodProf = models.ForeignKey(Profesiones, null = False, blank = True, on_delete = models.CASCADE)
    NombreInst = models.CharField(max_length = 80,null = False)
    DesCap = models.CharField(max_length = 500,null = False)
    FecIni = models.DateField(null = False)
    FecFin = models.DateField(null = False)
    NroHoras = models.IntegerField()
    estados = ((1, 'S'), (2, 'N'))
    Vigente = models.IntegerField(choices=estados, default=2)

class PerProfesion(models.Model):
    CodPers = models.ForeignKey(Persona, null = False, blank = True, on_delete=models.CASCADE)
    CodProf = models.ForeignKey(Profesiones, null = False, blank = True, on_delete=models.CASCADE)
    CodCentEst = models.ForeignKey(CentroEstudio, null = False, blank = True, on_delete=models.CASCADE)
    NroCIP = models.CharField(max_length = 10, null = False)
    FecCIPVig = models.DateField(null = False)
    estados = ((1, 'S'), (2, 'N'))
    Vigente = models.IntegerField(choices=estados, default=2)



class Experiencia(models.Model):
    CodPers = models.ForeignKey(Persona, null = False, blank= True, on_delete = models.CASCADE)
    LugarTrabajo = models.CharField(max_length = 30, null = False)
    DesTrabajo = models.CharField(max_length = 800, null = False)
    CodCargo = models.CharField(max_length = 4, null = False )
    FecIni = models.DateField(null = False)
    FecFin = models.DateField(null = False)
    NroConv = models.CharField(max_length = 6,null = False)
    Contrato = models.CharField(max_length = 400, null = False)
    MotivoRetiro = models.CharField(max_length = 30, null = False)
    CodProf = models.ForeignKey(Profesiones, null = False, blank = True, on_delete = models.CASCADE)
    estados = ((1, 'S'), (2, 'N'))
    Vigente = models.IntegerField(choices=estados, default=2)

