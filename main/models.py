from django.db import models


class Slider(models.Model):
    img = models.ImageField(upload_to="Slider/")
    title = models.CharField(max_length=70)
    text = models.CharField(max_length=230)


class Info(models.Model):
    img = models.ImageField(upload_to="Info/")
    title = models.CharField(max_length=70)
    text = models.CharField(max_length=230)
    tit1 = models.CharField(max_length=20)
    tit2 = models.CharField(max_length=20)
    tit3 = models.CharField(max_length=20)
    tit4 = models.CharField(max_length=20)

class PracticesAreas(models.Model):
    flatication = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    text1 = models.CharField(max_length=150)
    text2 = models.TextField()


class OurExpertise(models.Model):
    title = models.CharField(max_length=80)
    img = models.ImageField(upload_to="OurExpertise/")
    

class Flatication(models.Model):
    expertise = models.ForeignKey(OurExpertise, on_delete=models.CASCADE)
    flatication = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=150)


class Blog(models.Model):
    img = models.ImageField(upload_to="Blog/")
    janr = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    date = models.DateField()
    description = models.TextField()


class TeamMembers(models.Model):
    img = models.ImageField(upload_to="TeamMembers/")
    facebook = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    twitter = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)
    job = models.CharField(max_length=20)
    bio = models.TextField()

class AboutUs(models.Model):
    logo = models.ImageField(upload_to="AboutUs/")
    location = models.CharField(max_length=300)
    email1 = models.EmailField()
    email2 = models.EmailField()
    phone1 = models.CharField(max_length=100)
    phone2 = models.CharField(max_length=100)


class ContactUS(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    description = models.TextField()

class Newsletter(models.Model):
    email = models.EmailField()



