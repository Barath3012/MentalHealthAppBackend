from django.db import models

# Create your models here.
class Questionare(models.Model):
    depressedMood = models.IntegerField()
    feelingsOfGuilt = models.IntegerField()
    suicide = models.IntegerField()
    initialInsomnia = models.IntegerField()
    insomniaDuringTheNight = models.IntegerField()
    delayedInsomnia = models.IntegerField()
    workAndInterests = models.IntegerField()
    retardation = models.IntegerField()
    agitation = models.IntegerField()
    psychiatricAnxiety = models.IntegerField()
    somaticAnxiety = models.IntegerField()
    gastrointestinalSomaticSymptoms = models.IntegerField()
    generalSomaticSymptoms = models.IntegerField()
    hypochondriasis = models.IntegerField()
    weightLoss = models.IntegerField()
    insight = models.IntegerField()
