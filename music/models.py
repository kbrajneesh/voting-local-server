from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator


class Round1(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    con1 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con2 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con3 = models.PositiveIntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5) ])
    con4 = models.PositiveIntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5) ])
    con5 = models.PositiveIntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5) ])
    con6 = models.PositiveIntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5) ])
    con7 = models.PositiveIntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5) ])
    con8 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con9 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con10 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def get_absolute_url(self):
        return u'/'

    def __str__(self):
        return str(self.con1) +  ' - ' + str(self.con2) + ' - ' + str(self.con3) +  ' - ' + str(self.con4) + ' - ' +str(self.con5)  +  ' - ' + str(self.con6) + ' - ' + str(self.con7)+ ' - ' + str(self.con8)+ ' - ' + str(self.con9)+ ' - ' + str(self.con10)
class Round2(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    con1 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con2 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con3 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con4 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con5 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con6 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con7 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con8 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con9 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con10 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def get_absolute_url(self):
        return u'/'

    def __str__(self):
        return str(self.con1) +  ' - ' + str(self.con2) + ' - ' + str(self.con3) +  ' - ' + str(self.con4) + ' - ' +str(self.con5)  +  ' - ' + str(self.con6) + ' - ' + str(self.con7)+ ' - ' + str(self.con8)+ ' - ' + str(self.con9)+ ' - ' + str(self.con10)


class Round3(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    con1 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con2 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con3 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con4 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con5 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con6 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con7 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con8 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con9 = models.PositiveIntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5) ])
    con10 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.con1) +  ' - ' + str(self.con2) + ' - ' + str(self.con3) +  ' - ' + str(self.con4) + ' - ' +str(self.con5)  +  ' - ' + str(self.con6) + ' - ' + str(self.con7)+ ' - ' + str(self.con8)+ ' - ' + str(self.con9)+ ' - ' + str(self.con10)


def get_absolute_url(self):
    return u'/'