from django.db import models


class Coder(models.Model):
    name = models.CharField(unique=True, max_length=255)
    avatar = models.ImageField(upload_to='avatars')
    description = models.TextField(blank=True)
    units = models.ManyToManyField('Unit', help_text='studied unites')

    def __str__(self):
        return self.name

    def get_score(self):
        return self.units.aggregate(sum=models.Sum('score'))['sum'] or 0


class Course(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    course = models.ForeignKey(Course, related_name='unites', on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)
    score = models.PositiveSmallIntegerField(help_text='unit rating score')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    unit = models.ForeignKey(Unit, related_name='lessons', on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
