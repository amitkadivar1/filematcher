from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class HashType(models.Model):
    idHashType = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    
    #if you use python 2 then use unicode
    def __unicode__(self):
        return self.description

    #if use python 3 then use str 
    
    def __str__(self):
        return self.description

    class Admin:
        pass

class HashFile(models.Model):
    idHashFile = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="hash/%y/%m/%d-%H%M")
    #django 1.8 or lower version use this
    idHashType = models.ForeignKey(HashType)    
    #above django 2.0 or upper version use this
    idHashType = models.ForeignKey(HashType,on_delete=models.CASCADE)
    description = models.TextField()

    #if you use python 2 then use unicode
    def __unicode__(self):
	    return self.file + " (" + self.idHashType.description + ")"

    #if use python 3 then use str 
    def __str__(self):
        return self.file + " (" + self.idHashType.description + ")"
    
    class Admin:
	    pass

class FileInstance(models.Model):
    idFile = models.AutoField(primary_key=True)
    hash = models.CharField(max_length=128)
    fileLength = models.IntegerField()
    machine = models.CharField(max_length = 20)
    fullPath = models.CharField(max_length = 300)
    fileName = models.CharField(max_length = 100)
    #django 1.8 or lower version use this
    idHashType = models.ForeignKey(HashType)    
    #above django 2.0 or upper version use this
    idHashType = models.ForeignKey(HashType,on_delete=models.CASCADE)
    
    #python 2 in use unicode 
    def __unicode__(self):
	    return "{} on {} ".format(self.fileName,self.machine)

    #python 3 in use str
    def __str__(self):
        return "{} on {} ".format(self.fileName,self.machine)
    
    class Admin:
	    pass
