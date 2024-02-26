from django.db import models

# Create your models here.
class Jobstatus(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class RsponsiblePerson(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Jobrequest(models.Model):
    request_name = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    job_topic = models.CharField(max_length=200, blank=True, null=True)
    job_detail = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Jobstatus, on_delete=models.CASCADE, related_name="status")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="place")
    rsponsible_person = models.ForeignKey(RsponsiblePerson, on_delete=models.CASCADE, related_name="rsponsible_person")

    def __str__(self):
        return self.job_topic