from django.db import models



class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Major(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    description = models.TextField()
    min_unt_score = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    languages = models.CharField(max_length=400)
    majors = models.ManyToManyField(Major, related_name='universities')
    tuition_fee = models.IntegerField()
    internships = models.BooleanField(default=True)
    scholarships = models.BooleanField(default=True)
    image_url = models.URLField()

    def __str__(self):
        return f'{self.name} - {self.city}'
