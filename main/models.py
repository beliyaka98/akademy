from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    users = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Video(models.Model):
    url = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.url

class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Test(models.Model):
    input = models.TextField()
    output = models.TextField()
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.input
    
class Code(models.Model):
    code = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.code

