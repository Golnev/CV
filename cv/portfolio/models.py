from django.db import models


class Education(models.Model):
    title = models.CharField(
        max_length=48,
        verbose_name='title'
    )
    description = models.TextField(
        verbose_name='description'
    )
    number = models.CharField(
        max_length=9,
        verbose_name='String number of education'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Education'
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'


class WorkExperience(models.Model):
    title = models.CharField(
        max_length=48,
        verbose_name='title'
    )
    years_work = models.CharField(
        max_length=9,
        verbose_name='years of work'
    )
    description = models.TextField(
        verbose_name='description'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Work Experience'
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experiences'


class Contact(models.Model):
    name = models.CharField(
        max_length=48,
        verbose_name='name'
    )
    email = models.EmailField(
        verbose_name='email'
    )
    message = models.TextField(
        verbose_name='message'
    )

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'contact'
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
