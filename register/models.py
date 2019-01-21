from django.db import models

class team(models.Model):
    team_name = models.CharField(max_length=50)
    team_email = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name
class participant(models.Model):
    team = models.ForeignKey(team,on_delete=models.CASCADE)
    member1 = models.CharField(max_length=30)
    member2 = models.CharField(max_length=30)
    member3 = models.CharField(max_length=30)

    def __str__(self):
        return self.member1+' '+self.member2+' '+self.member3
