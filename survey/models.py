from django.db import models


class Questions(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice


class SurveyResponse(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    responses_data = models.JSONField()
    completed_at = models.DateTimeField(auto_now_add=True)
    ai_analysis = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f'{self.completed_at}'
