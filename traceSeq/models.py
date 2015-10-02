from django.db import models

# Create your models here.
class Seq(models.Model):
    seq      = models.TextField()#sequence
    state    = models.TextField(null=True)#done(.), not done(x), skipped(!)
    struct   = models.TextField(null=True)#nothing(.) helix(h), beta sheet(b), loop (l)
    seqName  = models.CharField(max_length=64,default="noname")

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.seq

class Comment(models.Model):
    seq = models.ForeignKey(Seq)
    position   = models.IntegerField()
    comment = models.TextField()

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return "not implemented"

