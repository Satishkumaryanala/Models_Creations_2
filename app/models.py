from django.db import models

# Create your models here.

class Dept(models.Model):
    Deptno = models.IntegerField(primary_key=True)
    Dname = models.CharField(max_length=100)
    Dloc = models.CharField(max_length=100)

    def __str__(self):
        return self.Dname

class Emp(models.Model):
    Empno = models.IntegerField(primary_key=True)
    Ename = models.CharField(max_length=100)
    Ejob = models.CharField(max_length=100)
    Esal = models.IntegerField()
    Ecomm = models.IntegerField(null=True,blank=True)
    Edeptno = models.ForeignKey(Dept,on_delete=models.CASCADE)


    def __str__(self):
        return self.Ename


